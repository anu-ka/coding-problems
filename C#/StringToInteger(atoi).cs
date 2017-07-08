public class Solution {
    
    public int MyAtoi(string str) {
        int index = 0;
        long number = 0;
        int neg = 1;

        if (str.Length == 0) return 0;

        // skip any initial white space
        while (char.IsWhiteSpace(str[index])) { ++index; }

        // check if this is a sign
        if (str[index] == '-') {
            neg = -1;
            ++index;
        } else if (str[index] == '+') {
            neg = 1;
            ++index;
        }

        while (index < str.Length) {
            if (char.IsDigit(str[index])) {
                number = number * 10 + (str[index] - '0');
                ++index;
            } else {
                break;
            }

            if (number > int.MaxValue) {
                break;
            }
        }

        if (number > int.MaxValue && neg < 0) {
            return int.MinValue;
        }

        if (number > int.MaxValue && neg > 0) {
            return int.MaxValue;
        }

        return neg * (int)number;
    }
}