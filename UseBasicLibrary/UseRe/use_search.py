# -*- coding: utf-8 -*-
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.search("Hello.*?(\d+).*?Demo", content)
print(result)

# lit = [(123, "dd"), (234, "ee"), (345, 'ww')]
# for i, j in lit:
#     print(i, j)

