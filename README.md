# WelcomeToProgramming
Let's make this repo an experience sharing BLOG-like-thing where we will share our experiences of getting stucked or encountering errors as beginner (new programmer) (self solved or solved by frnd in inbox)


## sharafat
- At first I just used to read and read without practicing. Which is definitely a bad habit!
- How are you supposed to learn a software if you're afraid of an unknown button? This philosophy of mine both helped and got me into a tons of troubles.

## IbnulAbrarShahriarSeam
- Read the problem statement carefully.
- Try to find a mathematical solution rather than using a loop. Loops take a huge amount of time and memory to execute. A mathematical solution is almost always more efficient.
- If you are working with an integer-type variable, try not to use something that returns double or floating-point values (e.g., pow()). As it may result in unexpected behavior.

## KaziRifatMorshed
- - STOP USING white-spaces (or simply, space) while naming a folder or file. It just looks nice and human readable but the terminal feels uncomfortable if it encounters a path containing white-spaces. IT IS A BAD PRACTICE, STOP DOING IT FROM RIGHT NOW.
- - `%0.0f` is a good idea to remove after-point part of the floating number(from showing/printing (by the console)). Actually it is a way of defining how many blocks/spaces/digits you want to show. 0.0 means there will be no after point part. 0.2 means there will be 2 digits after point-sign. `%3.4f` means there will be 3 digits before the point and 4 digits after the point.
- - `char c = 'A'` use single quote to put a Character, not Double Quote. Double quote is for multiple characters AKA string.
- - `if (chr == 'a' || chr == 'e' || chr == 'i' || chr == 'o' || chr == 'u') `
- -  In C, one cannot skip the return statement when the return type of the function is non-void type.
- - ` scanf(" %[^\n]", name);`
- - I have 5 lines inside a loop and there is a continue statement in line no 3; then line no 4 & 5 will not work
- -  `if(blank)` doesn't work, `if(1)`is true, `if(0)`is false
- - `iterate`, `recursion` = repeating
- - `n = scanf("%d%d%d", &n,&m,&p);` since `%d` came 3 times is this line/code, `scanf` function will take input n,m,p from user and (for being a function) it will return `3` (because, there is 3 `%d`, vise versa, `%d` was used 3 times)
- - you cannot use the `break` statement inside a ternary operator
- - The less the runtime is the better the code is. Runtime depends on number of Assignment operation and number of Comparison operation.
- - Put a newline `\n` at the start of `printf` if there is `printf` & `scanf` together where `printf` is telling the user to input.
- -  `if ((int) d == 0)` or `if (d == 0.0)` careful when `d` is float or long.
- - May face issues/problems while working with `float`s, need more knowledge on Computer Architecture for detailed understanding.
- - Switch statement ! integers and characters only ! Don't forget to BREAK ! Statements written above cases will never executed. Multiple case label can't have same value. 
- -  In `printf("%p\n",a);`code:
- 	 `,`: This is the comma that separates the format string from the arguments that are to be printed.
- 	 `a`: This is the argument being passed to `printf`. It's a variable or expression whose value you want to print.
- 	 The output will be  `0xHEXA` where the "HEXA" part represents the equivalent hexadecimal value of the given decimal integer.
- - `char abc = 'MAERTYU9'; printf("%c\n",abc);` here, only last character of the string which is `9` here will be printed. Similarly, ...
- - `if(0)` is false and the following block will not be executed, except zero, put any integer or float (including minus sign), the if-block will be executed. Even `if(0==0)` will be executed since the statement is logically TRUE. Similarly `if(0==1)` will not be executed since it is logically wrong and the compiler will consider it as false and ignore the if-block. BUT, if the condition-presenting number(either int or float) starts with zero, the compiler will give and error message`ig: if(0123).
-   SUMMARY: In C, non-zero values are treated as true.
- - `printf(R"qwer⏎rtyu⏎uiop");` there will be 3 lines as it will be considered as Raw String. (NOTE, here ⏎ is the emoji/symbol to represent ENTER key.)
- - `if(1 && 0)` means: 1 * 0 = 0 (false); `if(1 || 0)` means: 1 + 0 = 1 (true)
- - `gets()` - Read a line from a channel; white-spacer are allowed. `puts()` - Write to a channel. NOTE THAT: `gets()` is a vulnerable function so, try avoiding it and may use `fgets()` instead. `gets === get-string`, where one string consist many characters but `getchar` will get one char (not many char).
- - `atoi()` will convert the number stored string into digits.
- - `#include <filename.h>    // for files in system/default directory` or `#include "filename.h"    // for files in same directory as source file`
- - DO NOT FORGET `&` in `scanf` function !!!
- - You can use do-while loop to check input condition after taking input. If the inputs are invalid (Specially in Matrix Multiplication), write the condition as if it will start the loop to ask input again.
- - `strcpy(destination, source);` do not forget the format. Trick: DS.
- - `for(i=0; i>-1; i++) { if(condition){break;} }` can be a good idea to break infinity loop.
- - It is better to avoid float operands with the equal/not-equal checking operators.
- - Simplify the condition inside `if-else` with De-Morgan's Law if the conditional part looks very complicated.
- - Do not use equal operator to compare two floating-point value. They are seldom exactly equal.
- - There are ALWAYS REMEMBER section after every chapter, boxed TIPS, Chapter 16 in `Programming in ANSI C` by `E.Balagurusamy` Book. Collect the book to have a look through those pages.
- - Do not use a variable to represent a case label (in Switch statement).
- - `getchar` means get(=get input) a character from user, `putchar` means put A (=single) character in a variable.
- - In macro I've called `# define PI 3.14` (NOTE THAT here 3.14 is floating number). If I use `printf("%d",PI)` will give a garbage value . To solve the issue,  use the required data type here `printf("%f",PI)`. Similarly, if I've called `# define PI 314` which is non-floating number but later `printf("%d",PI)`,  the output will be `0.000000`.
- - To get a string as input where it contains white space, use `scanf("%[^\n]%*c",stringname)` or `scanf(“%[^\n]s”, str);` or `gets()` .  
- 	  First Explanation: Here, `[]` is the `scanset character`. `^\n` tells to take input until newline doesn’t get encountered. Then, with this `%*c`, it reads newline character and here used `*` indicates that this newline character is discarded.  
- 	  Second Explanation: Here, `[]` is the scanset character. ^\n tells to take input until newline doesn’t get encountered. Here we used ^ (XOR -Operator ) which gives true until both characters are different. Once the character is equal to New-line (‘\n’),  ^ (XOR Operator ) gives false to read the string. So we use “%[^\n]s” instead of “%s”. So to get a line of input with space we can go with `scanf(“%[^\n]s”,str);` source: geeksforgeeks.  
- - In C or C++, we cannot return multiple values from a function directly. But, We can return more than one values from a function by using the method called “call by address”, or “call by reference”. In the `invoker function`, we will use two variables to store the results, and the function will take pointer type data. So we have to pass the address of the data.
- - `strlen()` works perfectly in char type array AKA string. But, return zero if there is no element and return if there are ANY ELEMENT in the array.
- - The allocation and de-allocation for stack memory is automatically done. Since the stack memory of a function gets deallocated after the function returns, there is no guarantee that the value stored in those area will stay the same. A common mistake is to return a pointer to a stack variable in a helper function.
- - A char type variable can be used as a subscript in an array. In fact, any integral type (char, int, etc.) can be used as a subscript.
- - Use line braking character `\` to write multiple line string.
- - Confused ?  Look through manual pages (Linux is a blessing) type `man strcat` 
- - `src` = source, `dst` = destination, 
- - `strcmp()` and `strncmp()` are CASE SENSITIVE, it can't recognize same capital and small letter. Use `strcasecmp()` and `strncasecmp()` instead.
- - In the following code `for (int i=0; i < 10; i++) {printf("%i",i);}` we are declaring `i` inside to loop to run the loop (or, simply, take count of the loop). This new variable `i` will not work outside this specific for loop.
- - Do not use spaces while naming a c file or any folders. Additionally, avoid using `+` sign in file's name. Compiler Fails !
- - `%d` and `%i` behavior is different with `scanf()`. %d assume base 10 while %i auto detects the base.
- - **`if (scanf("%d %d", &p, &q) == 2 && p > 0 && q > 0) { ... }`** would be a good idea to scan inputs avoiding invalid inputs at same time.
- - If I have total 13 elements in an array (indexed from 0 to 12), `for (int i; 12 - i; p++, i++)` is a bad idea coz when i=12, the loop gets end and it wont print(or work) last number from the array.
- - Find the array's length **`int size = sizeof(data) / sizeof(data[0]);`** Let the array `data` has 5 elements. The `sizeof(data)` returns **the total size of the array**, which is `5 * sizeof(int)` bytes. **The `sizeof(data[0])` returns the size of a single element** in the array, which is `sizeof(int)` bytes. Dividing the total size of the array by the size of a single element gives us the number of elements in the array, which is 5.
- - `gotoxy()` alternative is  `void gotoxy(int x,int y) { printf("%c[%d;%df",0x1B,y,x); }`.
- - A nice way of copying strings `void copy(char *s1, char *s2) { while ((*s2++ = *s1++) != '\0') {}; }` 
- - A nice way `while (cin >> c && c != '\0') { if (c == '1') {one++;} }` to input, check it, and store it somewhere !
- - The line of code `int charSet[256] = {0};` in C declares and initializes an integer array called `charSet` with a size of 256 elements. **Each element in the array is initialized to 0.** Similarly, The line of code `char inputstring[100] = ' ';` in C declares and initializes a character array called `inputstring` with a size of 100 elements. **Each element in the array is initialized to a space character `' '`.**
- - **The `fgets` function reads a line from the input stream, including the newline character at the end.** This means that the `inputstring` array will contain the newline character as the last character. When the `for` loop iterates over the characters in the `inputstring` array, it encounters the newline character and treats it as a distinct character. This results in the count being one more than expected.
- - Can we avoid using pointers by initializing a variable outside main function ?!? Probably, affirmative.
- - Variable-Length Arrays (VLAs) are not allowed in C when you're declaring arrays with sizes determined at runtime. Instead, you should use dynamic memory allocation with `malloc` to allocate memory for your matrices. 
-   `int *matrix1 = (int *)malloc(row * col * sizeof(int));` would be a better way.
- - UNDER A LOOP, The `scanf` calls for input have an extra space character in the format string ("%d "). This will cause the input to not work correctly, as it expects a space after each number. Remove the space character to fix this issue.
- - No Input, Exit Prog. `elements if(element==NULL){printf("No memory is allocated.");exit(0);}`
- - `#include <stdbool.h>⏎    bool isEven(int number) {return (number % 2 == 0); // Returns true if the number is even, false otherwise}` or better, use `#define true 1` and `#define false 0`.
- - typecasting warning ! `(int)pow(x,n);` otherwise Float-loving `pow(_,_)` function may return something horrible !
- - Easy GCD: `int GCD(int a, int b) { return b ? GCD(a, a % b) : a; }`. Ternary Operator makes life easier while using Recursion.
- - `printf("%5.15s",str);` results to print first 15 characters of the string.
- - `(int)atoi(&str[i])` converts the whole string to int from i to last index.
- - One element in a 2D array `array[row][col] = *(array + row * numColumns + col)`
- - `(isalpha(c) || isdigit(c)` or `isalnum()`
- - https://stackoverflow.com/questions/25438718/why-to-put-space-between-d-and-c-while-inputting-there-values-using-scanf 
- - `while (getchar() != '\n'){ // test here }` AND, **`do { fflush(stdin); c = getchar(); str[i++] = c; } while (c != '\n');`**
- - `c = !!a;` This line first applies the logical NOT operator (`!`) to `a`, which results in `0` (since `a` is non-zero and the logical NOT of a non-zero value is `0`). Then, another logical NOT operator is applied to the result, which changes `0` to `1` (`!0` equals `1`). This result, `1`, is then assigned to variable `c`.
- - The getchar() accepts any character keyed in. This includes RETURN and TAB. This means when we enter single character input, the newline character is waiting in the input queue after getchar() returns. This could create problems when we use getchar() in a loop interactively. A dummy getchar() may be used to "eat" the unwanted newline character. We can also use the flush function to flush out the unwanted characters.
- - The first scanf requests input data for three integer values a, b, and c, and accordingly three values 1, 2, and 3 are keyed in. Because of the specification `%*d` the value 2 has been skipped and 3 is assigned to the variable b . Notice that since no data is available for c , it contains garbage.(Reference: ANSI C, page 107(book),WorkOutProb5.4)
- - It is possible to force the printing to be left-justified by placing a minus sign directly after the % character, as shown in the fourth example above. It is also possible to pad with zeros the leading blanks by placing a 0 (zero) before the field width specifier as shown in the last item above. The minus (–) and zero (0) are known as flags.
- - Generate random number `int r = rand() % 20;` and use MODULO(%) for overflow safety purpose.
- - if `f=10.5` then `printf(“%d\n”,(int)f);` will output `10` but `printf(“%d\n”, f);` will output ZERO.

# Contribution

Let the power of words weave its magic, igniting sparks of inspiration and fostering a vibrant community united by the beauty of language. Join us on this remarkable journey of sharing, connecting, and celebrating the extraordinary impact of words in our lives.

## How to Contribute
Upcoming...
