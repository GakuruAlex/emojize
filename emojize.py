import emoji
class Emojize:
    
    def main(self)-> None:
        user_st = input("Input: ")
        print(f"Output: {emoji.emojize(user_st, language = 'alias')}")

if __name__ == "__main__":
    emojize_ = Emojize()
    emojize_.main()