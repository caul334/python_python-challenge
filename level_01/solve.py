# Challenge 1

# solution code
message = ''

"""
gap_ch = ord("M") - ord("K")
enc_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for ch in enc_message:
	ascii_ch = ord(ch)
	if ascii_ch > 122 or ascii_ch < 97:
		message += chr(ascii_ch)
		continue
	ch_dec = ascii_ch + gap_ch
	if ch_dec > 122:
		ch_dec = ch_dec - 26
	message += chr(ch_dec)
print(message)
"""

# recommend code
enc_message = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
enc_url = "map"
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
result = str.maketrans(intab, outtab)
print(f"result : {enc_message.translate(result)}")
# [result] => ocr
#print(enc_url.translate(result))
