from crackerV1 import BasicCracker
from crackerV2 import GeometricSeqCracker


def main():
    cracker1 = BasicCracker()
    cracker2 = GeometricSeqCracker()
    #operateCracker(cracker2)
    operateCracker(cracker1)

def operateCracker(cracker):
    password_len = cracker.find_pass_len()
    password_without_last_char = cracker.find_password(password_len)
    password = cracker.find_pass_last_char(password_without_last_char)
    return password

if __name__ == "__main__":
    main()