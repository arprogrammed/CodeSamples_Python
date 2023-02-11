def trans(phrase):
    inters = ('how', 'why', 'what', 'when', 'where', 'who','How', 'Why', 'What', 'When', 'Where', 'Who')
    capit = phrase.capitalize()
    if phrase.startswith(inters):
        return "{}?".format(capit)
    else:
        return "{}.".format(capit)

results = []
while True:
    ui = input("Say Something: ")
    if ui == "exit!":
        break
    else:
        results.append(trans(ui))

print(' '.join(results))