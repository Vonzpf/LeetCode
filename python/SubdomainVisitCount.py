# -*- coding:utf-8 -*-

# @Author zpf
"""
A website domain like "discuss.leetcode.com" consists of various subdomains.
At the top level, we have "com", at the next level, we have "leetcode.com",
and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains.
We would like a list of count-paired domains, (in the same format as the input, and in any order),
that explicitly counts the number of visits to each subdomain.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

Notes:

The length of cpdomains will not exceed 100.
The length of each domain name will not exceed 100.
Each address will have either 1 or 2 "." characters.
The input count in any count-paired domain will not exceed 10000.
The answer output can be returned in any order.
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for domain in cpdomains:
            temp = domain.split()
            value = int(temp[0])
            name = temp[1].split('.')
            if len(name) == 3:
                sub_domain_1 = '.'.join(name)
                sub_domain_2 = '.'.join(name[1:])
                sub_domain_3 = name[-1]
                if sub_domain_1 not in domain_dict.keys():
                    domain_dict[sub_domain_1] = value
                else:
                    domain_dict[sub_domain_1] += value
                if sub_domain_2 not in domain_dict.keys():
                    domain_dict[sub_domain_2] = value
                else:
                    domain_dict[sub_domain_2] += value
                if sub_domain_3 not in domain_dict.keys():
                    domain_dict[sub_domain_3] = value
                else:
                    domain_dict[sub_domain_3] += value
            else:
                sub_domain_1 = '.'.join(name)
                sub_domain_2 = name[-1]
                if sub_domain_1 not in domain_dict.keys():
                    domain_dict[sub_domain_1] = value
                else:
                    domain_dict[sub_domain_1] += value
                if sub_domain_2 not in domain_dict.keys():
                    domain_dict[sub_domain_2] = value
                else:
                    domain_dict[sub_domain_2] += value
        domain_list = []
        for key in domain_dict.keys():
            temp = str(domain_dict[key]) + ' ' + key
            domain_list.append(temp)
        return domain_list

if __name__ == "__main__":
    sample = Solution()
    print(sample.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
