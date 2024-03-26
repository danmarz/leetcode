class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()  # Set to store unique email addresses

        for email in emails:
            local_name, domain_name = email.split(
                "@"
            )  # Split email into local name and domain name
            local_name = local_name.split("+")[0]  # Ignore characters after '+' sign
            local_name = local_name.replace(".", "")  # Remove all '.' characters

            # Add the modified email address to the set
            unique_emails.add(local_name + "@" + domain_name)

        # Return the count of unique email addresses
        return len(unique_emails)
