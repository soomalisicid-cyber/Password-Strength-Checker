
import getpass
import string

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Isticmaal ugu yaraan 12 xaraf haddii ay suurtagal tahay.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Ku dar xarfo yaryar, sida a-z.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Ku dar xarfo waaweyn, sida A-Z.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Ku dar tirooyin, sida 123.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Ku dar calaamado, sida ! ama #.")

    if score <= 2:
        strength = "Daciif"
    elif score <= 4:
        strength = "Dhexdhexaad"
    else:
        strength = "Xooggan"

    return strength, tips


def main():
    print("=" * 40)
    print("  PASSWORD STRENGTH CHECKER")
    print("  Local Python Security Lab")
    print("=" * 40)

    password = getpass.getpass("Geli password tijaabo ah: ")

    if not password:
        print("Wax password ah lama gelin.")
        return

    strength, tips = check_password(password)

    print("\nNatiijada:", strength)

    if tips:
        print("\nTalooyin:")
        for tip in tips:
            print("-", tip)
    else:
        print("Password-ku wuxuu buuxiyey shuruudaha la eegay.")

    print("\nBadbaado: password-ka lama daabacayo ama lama kaydinayo.")


if __name__ == "__main__":
    main()

