# Submission: https://leetcode.com/problems/unique-email-addresses/submissions/915928393/
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        distinct = set()

        for email in emails:
            distinct.add(self.fix_email(email))

        return len(distinct)

    def fix_email(self, email: str) -> str:
        local, domain = email.split("@")
        local = local.split("+")[0]
        local = "".join(filter(lambda c: c != '.', local))
        return f"{local}@{domain}"

