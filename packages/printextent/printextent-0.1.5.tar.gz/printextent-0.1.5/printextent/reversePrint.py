def reversePrint(text: str) -> str:
    string_ = text
    final_string = ""

    def reverse(string_1: str):
        if not string_1:
            return ""
        else:
            front_part = reverse(string_1[1:])
            back_part = string_1[0]
            front_part + back_part + string_[:-len(string_1)]

        return front_part + back_part[0]

    reverse_text = reverse(string_)
    reverse_text = reverse_text.split()

    for index in reverse_text:
        final_string += f"{index} "
    print(final_string)

reversePrint("This is a text sentence reversed!")