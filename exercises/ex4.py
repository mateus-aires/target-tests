billing_string = "SP – R$67.836,43; RJ – R$36.678,66; MG – R$29.229,88; ES – R$27.165,48; Outros – R$19.849,53"
cells = billing_string.split(";")


def get_state_billing(string):
  l = string.split("–")
  l[0] = l[0].strip()
  l[1] = float(l[1].strip().replace("R$", "").replace(".", "").replace(",", "."))

  return l[0], l[1]

dic = {}
result = {}
total = 0

for i in range(len(cells)):
  state, billing = get_state_billing(cells[i])
  dic[state] = billing
  total += billing

for key, value in dic.items():
  result[key] = value/total


print(result)