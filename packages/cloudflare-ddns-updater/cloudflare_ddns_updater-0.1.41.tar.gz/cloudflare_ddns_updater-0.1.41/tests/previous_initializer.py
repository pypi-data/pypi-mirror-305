import argparse
import json
import shutil
import sys
import requests
from crontab import CronTab
from cloudflare_ddns_updater.constants import *

cron_comment = "Cloudflare DDNS ip-updater"


def check_for_crontab():
    try:
        CronTab(user=True)
        return
    except OSError as e:
        print("crontab not found.\n "
              "To activate crontab run 'crontab -e' and insert a comment "
              "(anything will do, (like '# This is my crontab').")
        sys.exit(0)


def verify_token():
    count = 3
    while count > 0:
        tkn = input('Input your Cloudflare token\n')

        url = "https://api.cloudflare.com/client/v4/user/tokens/verify"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {tkn}"
        }
        response = requests.request("GET", url, headers=headers)
        r = response.status_code
        if r == 200:
            return tkn
        print(f"Token not valid.")
        count -= 1
    sys.exit()


def toggle_cron_job(toggle):
    check_for_crontab()
    cron = CronTab(user=True)
    for job in cron:
        if job.comment == cron_comment:
            job.enable(toggle)
            cron.write()
            if job.is_enabled():
                print(f"{job.comment} cron job started")
            else:
                print(f"{job.comment} cron job stopped. "
                      f"You may run ip-updater manually.\n"
                      f"To resume the cron job use --start")
            return
    print("No cron job found. Run --cron or --setup")
    return


def delete_cron_job():
    check_for_crontab()
    # Access the user's crontab
    cron = CronTab(user=True)
    # Remove jobs if comment
    for job in cron:
        if job.comment == cron_comment:
            cron.remove(job)
            cron.write()
            print(f"Removed {job.comment} cron job.")
            return
    print("No cron jobs to remove")
    return


def cleanup():
    shutil.rmtree(CONFIG_DIR, ignore_errors=True)
    print(f"Removed {CONFIG_FILE_PATH}")
    shutil.rmtree(LOG_DIR, ignore_errors=True)
    print(f"Removed {LOG_FILE_PATH}")
    delete_cron_job()
    print('All files created by script have been removed.\n'
          'To uninstall package use "pip (or pipx) uninstall cloudflare-ddns-updater"\n'
          'To reinstall from scratch run "cloudflare-ddns-updater --setup"')
    return


def create_log_file():
    # Check if the log file exists
    if not os.path.exists(LOG_FILE_PATH):
        # Create the log file
        try:
            with open(LOG_FILE_PATH, 'w') as log_file:
                log_file.write("IP update log initiated.\n")
            print(f"Log file is: {LOG_FILE_PATH}")
            # Secure file
            os.chmod(LOG_FILE_PATH, 0o600)
        except PermissionError:
            print(f"Permission denied. Cannot create {LOG_FILE_PATH}. Please run with appropriate privileges.")
            sys.exit()
    else:
        print(f"Log file is: {LOG_FILE_PATH}.")


def find_ip_updater():
    # Find the full path of 'ip-updater' command
    ip_updater_path = shutil.which('ip-updater')

    if not ip_updater_path:
        print("ip-updater command not found. Try a fresh installation.")
        sys.exit(1)
    return ip_updater_path


def update_json_with_force_ip(fi):
    # Check if the file exists
    if os.path.exists(CONFIG_FILE_PATH):
        # Load existing JSON data
        with open(CONFIG_FILE_PATH, 'r') as json_file:
            config_data = json.load(json_file)

        # Update the dictionary with new key-value pairs
        config_data["CURRENT_IP"] = "none"  # To force change when --cron
        config_data["COUNTER"] = fi
        config_data["FORCE_IP"] = fi

        # Write the updated dictionary back to the JSON file
        with open(CONFIG_FILE_PATH, 'w') as json_file:
            json.dump(config_data, json_file)
        print("Updated JSON file with Force IP address interval.")
    else:
        print("JSON file not found. Please run setup again.")


def manage_cron_job():
    # Check if the config file exists, otherwise you haven't run --setup yet
    if not os.path.exists(CONFIG_FILE_PATH):
        print(f"Please run 'cloudflare-ddns-updater --setup'")
        sys.exit()
    # Ask for and validate cron interval
    valid = False
    while not valid:
        cron_interval = input("\nHow often in minutes do you want to check your IP address? (Default is 2, max 59): ")
        if cron_interval == "":
            cron_interval = "2"
        if cron_interval.isnumeric() and int(cron_interval) in range(1, 60):
            print(f"script will run every {cron_interval} minutes")
            valid = True
        else:
            print("\nNo, seriously...")

    # Ask for and validate Force update interval
    valid = False
    while not valid:
        force_interval = input("After how many days would you like to force an IP update? (default is 1) ")
        if force_interval == "":
            force_interval = "1"
        if force_interval.isnumeric() and int(force_interval) in range(1, 366):
            print(f"IP address will be forced every {force_interval} days.")
            # Calculate force interval in runs
            force_after_runs = int(int(force_interval) * 1440 / int(cron_interval))  # / creates a float. we want an int
            update_json_with_force_ip(force_after_runs)
            valid = True
        else:
            print("\nNo, seriously...")

    # Get the full path of ip-updater
    ip_updater_path = find_ip_updater()
    # Delete old cron job
    delete_cron_job()
    # Create new cron job
    cron = CronTab(user=True)
    job = cron.new(command=f"{ip_updater_path} >> {LOG_FILE_PATH} 2>&1", comment=cron_comment)
    job.minute.every(cron_interval)
    cron.write()
    print(f"Cron job added/updated successfully. New interval: {cron_interval} minutes.")


def run_setup():
    check_for_crontab()
    print("\nThis script fetches the Zone ID and dns record ID from yor Cloudflare account.\n"
          "\nBefore running this script you must obtain a Cloudflare Token \n"
          "with the following Permissions:\n"
          "Zone - Zone - Read\nZone - DNS - Edit\n"
          "and the following Zone Resources:\nInclude - Specific zone - yourdomain.xx")
    print("You must also create an A record (xxx.yourdomain.xxx)")
    print("\nThis script only needs to be run once.\n"
          "The ip_updater script will then be run as a cron job.")
    if input("Do you have your token? y or n: ").lower() != "y":
        print("Once you have the token run this script again. see you later!")
        sys.exit()
    api_token = verify_token()

    # Get zone id
    url = "https://api.cloudflare.com/client/v4/zones"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    try:
        response = requests.request("GET", url, headers=headers)
        r = response.json()
        zone_id = r['result'][0]['id']
        print(f"zone id is: {zone_id}")
    except Exception as e:
        print(f"Error occurred during retrieval of zone id.\n"
              f"Make sure that your token has 'Zone-Zone-Read' permissions.\n{e}")
        sys.exit()

    # Get dns record id
    try:
        dns_records = f"{url}/{zone_id}/dns_records"
        response = requests.request("GET", dns_records, headers=headers)
        d = response.json()["result"]
        dns_record_id = "none"
        try_again = True
        while try_again:
            dns_record = input("For what record do you want to manage dns? (for example vpn.yourdomain.com)\n")
            for i in range(len(d)):
                if d[i]["name"] == dns_record:
                    dns_record_id = d[i]["id"]
                    print(f'dns record id is: {dns_record_id}')
                    try_again = False
            if dns_record_id == "none":
                print(f"I could not find {dns_record} in your Zone")
                print("The A records in your Zone are:")
                for i in range(len(d)):
                    if d[i]["type"] == "A":
                        print(f'  {d[i]["name"]}')
                cont = input("Would you like to use one of these? (y or n): ").lower()
                if cont != "y":
                    print("Run setup again when you are ready.")
                    sys.exit()
    except Exception as e:
        print(f"Something went wrong: {e}")
        sys.exit()

    # Create dictionary with data
    data = {
        "ZONE_ID": zone_id,
        "DNS_RECORD_ID": dns_record_id,
        "API_TOKEN": api_token,
    }

    # Write the data to a JSON file
    with open(CONFIG_FILE_PATH, 'w') as cf:
        json.dump(data, cf)
    print(f"\nConfig file is: {CONFIG_FILE_PATH}")
    # Secure file permissions
    os.chmod(CONFIG_FILE_PATH, 0o600)

    create_log_file()
    manage_cron_job()


def main():
    parser = argparse.ArgumentParser(description="Cloudflare DDNS Updater")
    parser.add_argument('--setup', action='store_true', help="Run the setup process.")
    parser.add_argument('--cron', action='store_true', help="Update the cron job.")
    parser.add_argument('--cleanup', action='store_true', help="Cleanup files before uninstalling")
    parser.add_argument('--stop', action='store_true', help="Stop cron job")
    parser.add_argument('--start', action='store_true', help="Start existing cron job")

    args = parser.parse_args()

    if args.setup:
        run_setup()
    elif args.cron:
        manage_cron_job()
    elif args.cleanup:
        cleanup()
    elif args.stop:
        toggle_cron_job(False)
    elif args.start:
        toggle_cron_job(True)
    else:
        print("Please provide an argument. For help, -h")


# The following ensures that when the user runs `cloudflare-ddns-updater`, the main function will be called.
if __name__ == "__main__":
    main()
