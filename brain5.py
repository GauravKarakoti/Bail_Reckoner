import languagemodels as lm
def ReplyBrain(input):
    lm.config["max_ram"] = "4gb"
    output=lm.do(input)
    return output

