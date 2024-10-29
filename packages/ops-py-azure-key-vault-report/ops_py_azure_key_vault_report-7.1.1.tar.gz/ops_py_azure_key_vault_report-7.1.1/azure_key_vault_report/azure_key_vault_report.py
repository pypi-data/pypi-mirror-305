#!/usr/bin/env python

import logging
import datetime
from .html_table import HTMLTable
from .ms_teams_json import MSTeamsPayload
from .set_timestamp import set_timestamp, now
from .markdown import Markdown
from .config import *
from .slack_payloads import SlackPayloads


########################################################################################################################

# NOTE: This package will be refactored to use ops-py-reports to generate the various report formats


class AzureKeyVaultReport(object):
    """Generates reports i various formats from the results of 'az keyvault' commands.

    The values of 'updated', 'created' and 'expires' are converted to date object
    and the age (in days) is calculated.

    Attributes
    ----------

    results : list
        The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
    items : list
        The list of items.
        Items are enriched with more data, e.g. age of each date element, vault_name, record_type, record_name
    vaults : list
         The unique list of vaults processed
    vaults_failed : list
        The unique list of vaults failed to process
    total_scanned_records_count : int
        A counter of all scanned records. Not including failed records.
    html_table : html table obj
        The html table object which are used to provide an HTML table for the MS Teams payload.
    report : list
        The list of filtered row items as dict
    report_md : str
        The text Markdown version of the report
    report_csv : list
        The list of csv rows
    summary : dict
        The summary of the report as dict
    summary_md : str
        The text Markdown version of the summary
    report_summary_md : str
        The text Markdown version of the summary and report combined
    slack_alert_rows : list
        The list of Slack messages formatted as Slack Markdown
    teams_alert_rows : list
        A list of Teams payloads (dicts) to be posted to MS Teams.
    summary_values : dict
        The config for the summary report. Read from config.py
    report_values : dict
        The config for the report. Read from config.py
    report_full : dict
        The full report, including the summary, as dict


    Methods
    -------
    parse_results()
        Parse through the provided 'results' from the azure cli keyvault cmd outputs.
        For each result in the results new item is created and added to the items list.
        Each item contains the following data:
        - Date objects, created from the 'updated', 'created' and 'expires' values and stored as values
          in new X_ts keys.
        - The age (in days) is calculated from each of the date objects and stored as values in new X_age keys.
        - 'vault_name' and 'record_type

    add_report(expire_threshold=None, alert_threshold=None,
               ignore_no_expiration=True, include_all=False, teams_json=False):
        Creates detailed 'column and rows' reports with comment according to the parameters passed.

        The column names are defined in the 'config.py' file.

        The values for the "Comment" column is generated according to the age of 'updated', 'created' and 'expires'.
        If missing 'expires' then a comment concerning that is added.

        When a row is completed it is added to the report(s), according to input arguments.
        A json object of a completed row is ALWAYS created.

    add_summary()
        Creates a summary as a dict ('summary') and as a plain text Markdown table ('summary_md').

        The heading / keys are defined in the config.py file.

        The 'summary' dict is also added to the 'report_full' dict.

    sort_items():
        Returns a sorted list of all the records

    get_teams_payloads()
        Create and returns an MS Teams payload. The HTML table is added as a part of the payload, if no other
        text is provided as argument.

    get_html_table()
        Returns the HTML table which is used in the MS Teams payload.

    slack_alert_payload(rows)
        Creates a Slack Markdown of the provided list of rows.

    create_kv_rows()
        Creates key/value pairs of the items in the report rows

    get_report_full()
        Returns the dict version of the full report were all the rows are included and a dict of the summary.

    get_report()
        Returns a list of dict versions of the filtered rows.

    get_csv_report()
        Creates a csv report and returns it.

    get_summary()
        Returns the dict version of the summary.

    get_summary_markdown()
        Returns a string with the plain text Markdown version of the summary.

    get_report_markdown()
        Returns a string with the plain text Markdown version of the report.

    get_report_summary_markdown()
        Returns a string with the plain text Markdown version of the summary and report combined.

    get_slack_payloads(title, max_chars=3500, app=True, md=True)
        Returns a list of Slack messages to be used in Slack posts.

    error_record_handle(message)
        Checks if the error az cli cmd error output contains a known error.
        Known errors are defined in the config file.

    teams_alert_payload(row)
        Creates an MS Teams alert payload of an alert row.
    """

    def __init__(self, results):
        """
        Parameters
        ----------
        results : list
            The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
        """

        self.results = results
        self.items = []
        self.vaults = []
        self.vaults_failed = []
        self.total_scanned_records_count = 0
        self.html_table = None
        self.report_md = ""
        self.report = []
        self.report_csv = []
        self.summary = {}
        self.summary_md = ""
        self.report_summary_md = ""
        self.slack_alert_rows = []
        self.teams_alert_rows = []
        self.summary_values = config.get("summary")
        self.report_values = config.get("report")
        self.report_full = {
            "created_at": datetime.datetime.utcnow().isoformat(),
            "summary": {},
            "report": {}
        }

    def sort_items(self, expired_days=7, will_expire_days=14):
        """Sort the list of dict items by days to expiration

        If no parameters provided, this method will return a sorted list of all the records.
        The list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns the sorted list.

        If any of the parameters provided, it will first create and sort
        an 'error' list
        and then an 'expired' list
        and then a 'will_expire' list
        and the finally a list with the other records.

        Each list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns a combined list.

        Parameters
        ----------
        expired_days : int
            If provided, the record will be added to a separate list (expired),
            if the expires_age (days since expiration) of the record
            is between 0 the days provided in the expired_days argument.

        will_expire_days : int
            If provided, the record will be added to a separate list (will_expire),
            if the expires_age (days to expiration) of the record
            is between 0 the days provided in the will_expire_days argument,
            and the record is not already added to the expired list.
        """

        if not isinstance(expired_days, int):
            return sorted(self.items, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        errors = []
        expired = []
        will_expire = []
        others = []
        for item in self.items:
            if item.get("error"):
                errors.append(item)
                continue

            expires_age = item.get("expires_age")
            if isinstance(expires_age, int) and expires_age <= 0 and abs(expires_age) <= expired_days:
                expired.append(item)
                continue

            if isinstance(expires_age, int) and 0 <= expires_age <= will_expire_days:
                will_expire.append(item)
                continue

            others.append(item)

        sorted_list = errors
        sorted_list += sorted(expired, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(will_expire, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(others, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        return sorted_list

    def error_record_handle(self, message):
        """Checks if the error az cli cmd error output contains a known error - as defined in the config file"""

        # Get the known error from config file
        known_errors = config.get("known_errors")

        # Returns if no error message provided or known errors not found in the config file
        if not message or not known_errors:
            return

        vault_name = "-"
        record_type = "-"
        error_msg = "-"

        # Parse through the know error keys in config to check if the same error is present in the message
        # The Vault Name and Record Type is fetched from the executed 'az keyvault' cmd
        # which may be present in the provided message
        for key, value in known_errors.items():
            if key.lower() in str(message).lower():
                for line in message.splitlines():

                    # List permission error
                    if line.startswith("ERROR:"):
                        if "list permission" in line.lower():
                            for item in line.split(";"):
                                if key.lower() in item:
                                    vault_name = item.split("'")[-1]
                                    record_type = item.split(key.lower())[0].split()[-1]
                                    error_msg = value
                                    if error_msg and vault_name and record_type:
                                        break

                        # Firewall not authorized error and establish error
                        else:
                            error_msg = value

                    # Firewall not authorized error
                    if error_msg and line.startswith("Vault: "):
                        vault_name = line.split(";")[0].split()[-1]
                        record_type = "-"

                    # Get vault_name and record_type from executed 'az keyvault' command (if command logged)
                    if line.startswith("az keyvault"):
                        cmd_elements = line.split()
                        vault_name = cmd_elements[-1]
                        record_type = cmd_elements[-4]
                        error_msg = value

        self.items.append(
            {
                "error": error_msg,
                "vault_name": vault_name,
                "record_type": record_type
            }
        )
        if vault_name not in self.vaults_failed:
            self.vaults_failed.append(vault_name)

    def parse_results(self):
        """Parse through the result from the azure cli keyvault cmd output and build new enriched items."""

        if not isinstance(self.results, list):
            logging.error(f"The provided results must be a list.")
            return

        for result in self.results:
            vault_name = ""
            record_type = ""

            if not isinstance(result, list):
                logging.error(f"The az output result is not a list. Will check if known error..")
                self.error_record_handle(result)
                continue

            for r in result:
                if not isinstance(r, dict):
                    logging.error(f"The az output is not in expected format.")
                    continue

                if not vault_name and not record_type:
                    kv_id = r.get("id", "")
                    if not kv_id:
                        kv_id = r.get("kid", "")

                    items = kv_id.split("/")
                    if len(items) == 5:
                        vault_name = items[2].split(".")[0]
                        record_type = items[3].rstrip("s")

                if not vault_name and not record_type:
                    continue

                if vault_name not in self.vaults:
                    self.vaults.append(vault_name)

                item = {
                        "vault_name": vault_name,
                        "record_type": record_type,
                        "record_name": r.get("name"),
                        "enabled": False,
                }

                a = r.get("attributes")
                if isinstance(a, dict):
                    for k, v in a.items():
                        if "enabled" in k:
                            item["enabled"] = v

                    if not item.get("enabled"):
                        self.summary_values["records_disabled"]["value"] += 1

                    else:
                        self.summary_values["records_active"]["value"] += 1

                    for k, v in a.items():
                        if ("updated" in k or "created" in k or "expires" in k) and v:
                            value = v.split("T")[0]
                            item[k] = value
                            ts = set_timestamp(value)
                            item[f"{k}_ts"] = ts
                            age = (now() - ts).days
                            item[f"{k}_age"] = age

                            # Update the update age counters:
                            # If already expired
                            if "expires" in k and item.get("enabled") and age > 0:
                                self.summary_values["expired"]["value"] += 1

                            # One year and older, but less than two years
                            if "updated" in k and item.get("enabled") and age < 365:
                                self.summary_values["this_year"]["value"] += 1

                            # One year and older, but less than two years
                            if "updated" in k and item.get("enabled") and (365 <= age < 365 * 2):
                                self.summary_values["one_year"]["value"] += 1

                            # Two year and older, but less than three years
                            elif "updated" in k and item.get("enabled") and (365 * 2 <= age < 365 * 3):
                                self.summary_values["two_years"]["value"] += 1

                            # Three years and older
                            elif "updated" in k and item.get("enabled") and age >= 365 * 3:
                                self.summary_values["three_years"]["value"] += 1

                        if "expires" in k and item.get("enabled") and not v:
                            self.summary_values["missing"]["value"] += 1

                self.items.append(item)
                self.total_scanned_records_count += 1

    def add_summary(self):
        """Creates a plain text Markdown version of the summary, and also add it to the 'report_full' dict."""

        self.summary = {}
        self.summary_values["vaults"]["value"] = len(self.vaults)
        self.summary_values["vaults_error"]["value"] = len(self.vaults_failed)
        self.summary_values["records"]["value"] = self.total_scanned_records_count

        rows = []
        for k, v in self.summary_values.items():
            if "heading" in k:
                rows.append(v)
            elif isinstance(v, dict):
                value = v.get("value")
                if value:
                    text = v.get("text")
                    rows.append([text, value])
                    self.summary[text] = value

        md = Markdown(rows)
        md.set_widths()
        self.summary_md = md.get_output(1)
        self.report_full["summary"]["rows"] = [self.summary]

    def add_report(self, expire_threshold=None, alert_threshold=None, ignore_no_expiration=True,
                   include_all=False, teams_json=False):
        """Creates a detailed 'column and rows' reports with comment.

        The column names are defined in the 'config.py' file.

        The values for the "Comment" column is generated according to the age of 'updated', 'created' and 'expires'.
        If missing 'expires' then a comment concerning that is added.

        When a row is completed it is added to the report(s), according to input arguments.
        A json object of a completed row is ALWAYS created.

        Parameters
        ----------
        expire_threshold : int
            Ignore to report the record if days till the secret will expire are more than this 'expire_threshold' value
            NOTE: Secrets expiring today or already expired will always be reported.
        alert_threshold : int
            If specified, a Slack Markdown post of the row will be created, IF the row contains a record which days to
            expiring/expired (+/-) are within the value of 'alert_threshold' value.
            The markdown post will then be added to a 'slack_alert_rows' list.
        ignore_no_expiration : bool
            Reports all records if set to False. If set to True only secrets with Expiration Date set will be reported.
        include_all : bool
            If set to True all records are included in the output.
        teams_json : bool
            If set to True then a report in json format containing a html table will also be generated.
        """
        if not isinstance(self.results, list):
            return

        heading = self.report_values.get("heading")

        # Add header to CSV report
        self.report_csv.append(heading)

        # If argument 'teams_json' is True, then a html table is initialized. To be used with the MS Teams payload
        if teams_json:
            self.html_table = HTMLTable(heading)
            self.html_table.init_html_table()

        # Ensure only heading and no data rows
        rows = [heading]
        rows_all = [heading]

        # Sort the items from top and down
        # First sort by the oldest 'Expiration' date
        # Then sort by the oldest 'Last Updated' date
        items = self.sort_items()

        for item in items:

            # If no Vault Name, we skip to next item in the list
            vault_name = item.get("vault_name", "")
            if not vault_name:
                continue

            error = item.get("error")
            if error:
                record_type = item.get("record_type", "-")
                vault_name = item.get("vault_name", "-")
                error = item.get("error", "")
                record_name = "ERROR"
                updated = ""
                expires = ""
                comment = "Unknown error"
                if error:
                    comment = f"Error: {error.replace('a new ', '')}"

                row = [record_name, record_type, vault_name, updated, expires, comment]
                rows_all.append(row)
                rows.append(row)

                # If the teams_json argument was set to True, a html_table was created.
                # If so, then the row is also added to the html table, which are used in the MS Teams payload.
                if self.html_table:
                    self.html_table.add_html_row(*row)
                continue

            # Get the record name
            record_name = item.get("record_name", "ERROR")

            # Get the record type
            record_type = item.get("record_type", "")

            # Get the expires, update and enabled values
            expires = item.get("expires", "")
            expires_age = item.get("expires_age")
            updated = item.get("updated")
            updated_age = item.get("updated_age")
            enabled = item.get("enabled")

            # Add to row: the values of: 'record_name', 'record_type', 'vault_name' and 'updated'
            row = [record_name, record_type, vault_name, updated]

            # Add to row: the value of: 'expires' (if any)
            if expires:
                row.append(expires)
            else:
                row.append(" ")

            # Create 'comment' variable
            # The value of 'Comment' is dependent of the info from the 'expires' and 'update' values
            comment = ""
            if not enabled:
                comment += "Disabled. "

            if isinstance(expires_age, int):
                if expires_age <= 0:
                    comment += f"Will expire in {abs(expires_age)} days. "
                if expires_age > 0:
                    comment += f"Expired {expires_age} days ago. "

            if not expires:
                comment += f"Has no expiration date. "

            if isinstance(updated_age, int):
                comment += f"Updated {updated_age} days ago. "

            # A little cosmetic touch to avoid plural where it should not be used
            comment = comment.replace(" 1 days", " 1 day")

            # Add the comment to the row
            row.append(comment)

            # The row is now complete
            # Add the row to the rows_all (The ones that will be stored in db, but not necessarily will be alerted on)
            rows_all.append(row)

            # Add the row to CSV report
            self.report_csv.append(row)

            # Only include disabled entries if set to include_all
            if not include_all and not enabled:
                continue

            # Skip records with no Expiration Date set, only if 'ignore_no_expiration' and not 'include_all'
            if not expires:
                if ignore_no_expiration and not include_all:
                    continue

            # If the record has Expiration Date set, check if it should be alerted and/or reported on
            if isinstance(expires_age, int):
                # Check if soon expiring OR expired recently (the alert_threshold range)
                # If so, a Slack Markdown Payload of current row will be created
                # and added to the list of Slack Markdown payloads,
                if isinstance(alert_threshold, int):
                    alert = False

                    # The record has not expired, but is within the alert_threshold range
                    if 0 >= expires_age >= -alert_threshold:
                        logging.info(f"{record_name} - expiring in {abs(expires_age)} days.")
                        alert = True

                    # The record has expired and is within the alert_threshold range
                    if 0 < expires_age <= alert_threshold:
                        logging.info(f"{record_name} - expired {expires_age} days ago.")
                        alert = True

                    if alert:
                        logging.info(f"{record_name} - alert_threshold is set to '{alert_threshold}'.")
                        logging.info(f"{record_name} - will be alerted to Slack.")
                        slack_payload = self.slack_alert_payload(row)
                        if slack_payload:
                            logging.info(f"{record_name} - Slack alert payload created.")
                            self.slack_alert_rows.append(slack_payload)

                        teams_payload = self.teams_alert_payload(row)
                        if teams_payload:
                            logging.info(f"{record_name} - MS Teams alert payload created.")
                            self.teams_alert_rows.append(teams_payload)

                if expires_age < 0:
                    # The record has not expired yet
                    logging.info(f"{record_name} - has not expired yet. "
                                 f"It will expire in {abs(expires_age)} days ({expires}).")

                    # Handle those within the valid 'expire_threshold' range
                    # Those record will not be included in the standard report.
                    # They will only be included in the full report or if 'include_all' is set to True
                    if isinstance(expire_threshold, int) and expire_threshold < abs(expires_age):
                        logging.info(
                            f"{record_name} - Expiration Date is within the valid specified threshold of "
                            f"{expire_threshold} days. This record will start to be "
                            f"reported in {abs(expires_age) - expire_threshold} days.")

                        # This record is within the valid 'expire_threshold' range so the loop will
                        # not proceed with adding the row the list of rows
                        # unless if 'include_all' is set to True, then the row will be added.
                        if not include_all:
                            continue

                else:
                    # The record has expired or is expiring today
                    logging.info(f"{record_name} - expired {expires_age} days ago.")

            # Then finally add the row to the rows which will be reported on
            rows.append(row)
            # If the teams_json argument was set to True, a html_table was created.
            # If so, then the row is also added to the html table, which are used in the MS Teams payload.
            if self.html_table:
                self.html_table.add_html_row(*row)

        ################################################################################################################
        # All the rows are now processed. Only the wanted rows are kept and will be used to create the reports

        # A json object of all rows are always created.
        self.report_full["report"]["rows"] = self.create_kv_rows(rows_all)

        # If 'include_all' argument is set to True, then 'all_rows' are used instead of the ones not filtered out.
        if include_all:
            rows = rows_all

        if not rows:
            logging.error("No report generated.")
            return

        # Create the reports
        if len(rows) > 1:
            # Create a plain text Markdown of the report
            md = Markdown(rows)
            md.set_widths()
            self.report_md = md.get_output()

            # Create json of the report
            self.report = self.create_kv_rows(rows)

            logging.info("report generated.")

    def create_kv_rows(self, rows):
        """Creates key/value pairs of the items in the rows

        Returns
        -------
        A list of row items as dicts.
        """

        kv_rows = []
        for i, r in enumerate(rows):
            if i > 0:
                j = {}
                for n, v in enumerate(self.report_values.get("heading")):
                    j[v] = r[n]
                kv_rows.append(j)
        return kv_rows

    def slack_alert_payload(self, row):
        """Creates a Slack alert payload of the row.

        Returns
        -------
        A dict of the Slack item.
        """

        if not row:
            return

        item = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"{row[0]}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{row[-1]}*"
                    }
                },
                {
                    "type": "section",
                    "fields": []
                }
            ]
        }

        blocks = item.get("blocks")
        for i in range(1, len(row)-1):
            x = {"type": "mrkdwn",
                 "text": f"*{self.report_values['heading'][i]}:*\n{row[i]}"
                 }
            blocks[-1]["fields"].append(x)
        blocks.append({"type": "divider"})
        return item

    def teams_alert_payload(self, row):
        """Creates an MS Teams alert payload of the row.

        Returns
        -------
        MS Teams payload.
        """
        if not row:
            return

        item = {"type": "message",
                "attachments": [{"contentType": "application/vnd.microsoft.card.adaptive",
                                 "content": {
                                     "type": "AdaptiveCard",
                                     "body": [
                                         {
                                             "type": "TextBlock",
                                             "size": "large",
                                             "weight": "Bolder",
                                             "text": row[0]
                                         },
                                         {
                                             "type": "TextBlock",
                                             "size": "medium",
                                             "weight": "Bolder",
                                             "text": row[-1]
                                         },
                                         {
                                             "type": "TextBlock",
                                             "text": ""
                                         }
                                     ]
                                 }
                                 }
                                ]
                }

        for i in range(1, len(row) - 1):
            item['attachments'][0]['content']['body'][-1]["text"] += f"**{self.report_values['heading'][i]}:** {row[i]}\n\n"

        return item

    def get_report_full(self):
        """Returns the dict version of the full report were all the rows are included and a dict of the summary."""

        return self.report_full

    def get_report(self):
        """Returns a list of dict versions of the filtered rows."""

        return self.report

    def get_csv_report(self):
        """Create and returns a csv report"""

        out = ""
        for row in self.report_csv:
            current_row = ""
            for col in row:
                current_row += f"{col},"
            current_row = current_row.rstrip(",")
            out += f"{current_row}\n"

        return out.rstrip("\n")

    def get_summary(self):
        """Returns the dict version of the summary."""

        return self.summary

    def get_summary_markdown(self):
        """Returns a string with the plain text Markdown version of the summary."""

        return self.summary_md

    def get_report_markdown(self):
        """Returns a string with the plain text Markdown version of the report."""

        return self.report_md

    def get_report_summary_markdown(self):
        """Returns a string with the plain text Markdown version of the summary and report combined."""

        if self.report_md:
            self.report_summary_md = f"{self.summary_md}\n\n{self.report_md}"
        else:
            self.report_summary_md = self.summary_md

        return self.report_summary_md

    def get_teams_payloads(self, title, text="", alert=False):
        """Initiate the MSTeamsPayload class to build and return an MS Teams payload.

        Parameters
        ----------
        title : string
            The 'activityTitle' of the MS Teams payload
        text : string
            The 'text' part of the payload. If not provided, the generated 'html_table' will be used instead.
        alert : boolean
            If set to True, the 'teams_alert_rows' will be returned, which is a list of Teams payloads (dicts) to be
            posted to MS Teams.
            This list has only been populated if the 'add_report' method has not been executed with a value for the
            'alert_threshold' and the record in the row has met the 'alert_threshold' filter.

        Returns
        -------
        A json dump (string) of the complete payload.
        """

        if alert:
            return self.teams_alert_rows

        if not isinstance(self.results, list):
            return

        if len(self.items) == 0:
            return

        if not text:
            text = self.get_html_table()

        ms_teams_payload = MSTeamsPayload(title, text, self.summary_values)
        ms_teams_payload.set_json_facts()
        return ms_teams_payload.get_json_output()

    def get_html_table(self):
        """Returns the 'html_table as string'

        None is returned if the 'add_report' method has not been executed with 'teams_json' argument set to True"""

        if self.html_table:
            return self.html_table.get_table()

    def get_slack_payloads(self, title, max_chars=3500, alert=False, app=True):
        """Returns a list of Slack messages to be used in Slack posts.

        Parameters
        ----------
        title : string
            Title/heading of the message.
        max_chars : int
            Message above this limit will be split into multiple parts
            (default: 3500)
        alert : boolean
            If set to True, the 'slack_alert_rows' will be returned, which is a list of Slack items (dicts) to be posted to Slack.
            This list has only been populated if the 'add_report' method has not been executed with a value for the
            'alert_threshold' and the record in the row has met the 'alert_threshold' filter.
        app : boolean
            If True, a list of Slack items (dicts) to be used as payload for a Slack App is returned
            If False, a list of Slack items in tuple pairs is returned. To be used to post to a Slack Workflow.

            Note: Not relevant if 'md' is set to True

        """

        if alert:
            return self.slack_alert_rows

        self.get_summary_markdown()
        self.get_report_summary_markdown()
        self.get_report_markdown()

        p = SlackPayloads(title, self.summary_md, self.report_md, self.report_summary_md, max_chars=max_chars)
        if app:
            return p.get_app_payloads()

        return p.get_workflow_posts()
