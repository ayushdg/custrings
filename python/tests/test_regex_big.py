import nvstrings

strs =  nvstrings.to_device(["hello @abc @def world The quick brown @fox jumps over the lazy @dog hello http://www.world.com I'm here @home", "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890","abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"])
#strs =  nvstrings.to_device(["12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"])

print("contains:short: true,false", strs.contains("@\\S+"))
print("contains:short: false,false", strs.contains("#\\S+"))

print("contains: true,false", strs.contains("hello @abc @def world The quick brown @fox jumps over the lazy @dog hello http://www.world.com I'm here @home"))
print("contains: false,false", strs.contains("hello @abc @def world The quick brown @fox jumps over the lazy @dog hello http://www.world.com I'm here @home zzzz"))

print("contains: false,true", strs.contains("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"))

print("match: true,false", strs.match("hello @abc @def world The quick brown @fox jumps over the lazy @dog hello http://www.world.com I'm here"))
print("match: false,true", strs.match("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"))

print("find: ", strs.find("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")[1])
print("findall: ", strs.findall("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")[1])
print("findall_column: ", strs.findall_column("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")[0])

print("replace: _ ", strs.replace("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567","_"))

print("count: 1 ", strs.count("12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567"))

print("extract: ", strs.extract("(12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567)")[1])
print("extract_column: ", strs.extract_column("(12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567)")[0])