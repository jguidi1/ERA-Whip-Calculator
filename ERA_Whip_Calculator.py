def ERA_Calculator(earned, innings):
    return (earned*9) / innings

def WHIP_Calculator(walks, hits, innings):
    return (walks + hits) / innings


earned = float(input("Enter the number of earned runs: "))
innings = float(input("Enter the number of innings pitched: "))
walks = float(input("Enter the number of walks: "))
hits = float(input("Enter the number of hits: "))
print("ERA: ", ERA_Calculator(earned, innings))
print("WHIP: ", WHIP_Calculator(walks, hits, innings))