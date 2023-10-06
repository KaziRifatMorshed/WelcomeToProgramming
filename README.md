# WelcomeToProgramming
Let's make this repo an experience sharing BLOG-like-thing where we will share our experiences of getting stucked or encountering errors as beginner (new programmer) (self solved or solved by frnd in inbox)


## KaziRifatMorshed
- we may get an error to compile a `.c` file with GCC if it contains `#include "math.h"` in UNIX(simply, Linux) operating system. Add `-lm` at the last of the command (which will look like this: `gcc -o abcxyz abcxyz.c -lm`, otherwise, the GCC compiler may fail to link math.h header file
- avoid `conio.h` , the latest GCC gives errors, forget it (so avoid `getch()` )
- use `C/C++ Compile Run` Extension (extension id: danielpinto8zz6.c-cpp-compile-run ) for VS-Code or VScode like IDE (like: OSS Code or VS Codium) , use keyboard shortcut F6 ; if you are interested to compile in GNU/Linux terminal, you may follow [this link](https://cseweb.ucsd.edu/classes/fa09/cse141/tutorial_gcc_gdb.html) 
- It is a bad practice to use the goto statement of C, a teacher suggested, avoiding it
- Online Judges are Stupid/idiot/baka.... itai ....
-  STOP USING whitespaces (or simply, space) while naming a folder or file. It just looks nice and human-readable but the terminal feels uncomfortable if it encounters a path containing whitespaces. IT IS A BAD PRACTICE, STOP DOING IT FROM RIGHT NOW.
-  `%0.0f` is a good idea to remove the afterpoint part of the floating number(from showing/printing (by the console)). Actually, it is a way of defining how many blocks/spaces/digits you want to show. 0.0 means there will be no after-point part. 0.2 means there will be 2 digits after point. `%3.4f` means there will be 3 digits before the point and 4 digits after the point.
-  `char c = 'A'` use single quote to put a Character, not Double Quote
-  `if (chr == 'a' || chr == 'e' || chr == 'i' || chr == 'o' || chr == 'u') `
-   In C, one cannot skip the return statement when the return type of the function is nonvoid type.
-  ` scanf("%[^\n]", name);`
-  I have 5 lines inside a loop and there is a continue statement in line no 3; then line no 4 & 5 will not work
-   `if(blank)` doesn't work, `if(1)`is true, `if(0)`is false
-  `iterate`, `recursion` = repeating
-  `n = scanf("%d%d%d", &n,&m,&p);` since `%d` came 3 times is this line/code, `scanf` function will take input n,m,p from user and (for being a function) it will return `3` (because, there is 3 `%d`, vise versa, `%d` was used 3 times)
-  you cannot use the `break` statement inside a ternary operator
-  The less the runtime is the better the code is. Runtime depends on number of Assignment operation and number of Comparison operation.
-  Put a newline `\n` at the start of `printf` if there is `printf` & `scanf` together where `printf` is telling the user to input.
-   `if ((int) d == 0)` or `if (d == 0.0)` careful when `d` is float or long.
-  May face issues/problems while working with `float`s, need more knowledge on Computer Architecture for detailed understanding.
-  Switch statement ! integers and characters only ! Don't forget to BREAK ! Statements written above cases will never executed. Multiple case label can't have same value. 
-   In `printf("%p\n",a);`code:  `,`: This is the comma that separates the format string from the arguments that are to be printed.	 `a`: This is the argument being passed to `printf`. It's a variable or expression whose value you want to print.	 The output will be  `0xHEXA` where the "HEXA" part represents the equivalent hexadecimal value of the given decimal integer.
-  `char abc = 'MAERTYU9'; printf("%c\n",abc);` here, only last character of the string which is `9` here will be printed. Similarly, ...
-  `if(0)` is false and the following block will not be executed, except zero, put any integer or float (including minus sign), the ifblock will be executed. Even `if(0==0)` will be executed since the statement is logically TRUE. Similarly `if(0==1)` will not be executed since it is logically wrong and the compiler will consider it as false and ignore the ifblock. BUT, if the conditionpresenting number(either int or float) starts with zero, the compiler will give and error message`ig: if(0123).
-   SUMMARY: In C, non-zero values are treated as true.
-  `printf(R"qwer⏎rtyu⏎uiop");` there will be 3 lines as it will be considered as Raw String. (NOTE, here ⏎ is the emoji/symbol to represent ENTER key.)
-  `if(1 && 0)` means: 1 * 0 = 0 (false); `if(1 || 0)` means: 1 + 0 = 1 (true)
-  null character in a string will stop the string there. Explanation: input:`I am a boy/0`,output:`I am a boy`; input:`I am a b\0oy`,output:`I am a b`; input`\0I am a boy`,output will be empty.
-  `gets()`  Read a line from a channel; whitespacer are allowed. `puts()`  Write to a channel. NOTE THAT: `gets()` is a vulnerable function so, try avoiding it and may use `fgets()` instead. `gets === getstring`, where one string consist many characters but `getchar` will get one char (not many char).
-  `atoi()` will convert the number stored string into digits.
-  `#include <filename.h>    // for files in system/default directory` or `#include "filename.h"    // for files in same directory as source file`
-  DO NOT FORGET `&` in `scanf` function !!!
-  You can use dowhile loop to check input condition after taking input. If the inputs are invalid (Specially in Matrix Multiplication), write the condition as if it will start the loop to ask input again.
-  `strcpy(destination, source);` do not forget the format.
-  `for(i=0; i>1; i++) { if(condition){break;} }` can be a good idea to break the infinity loop.
-  It is better to avoid float operands with the equal/notequal checking operators.
-  Simplify the condition inside `if-else` with DeMorgan's Law if the conditional part looks very complicated.
-  Do not use an equal operator to compare two floatingpoint value. They are seldom exactly equal.
-  There are "ALWAYS REMEMBER" sections after every chapter, boxed TIPS, Chapter 16 in `Programming in ANSI C` by `E.Balagurusamy` Book. Collect the book to have a look through those pages.
-  Do not use a variable to represent a case label (in Switch statement).
-  `getchar` means get(=get input) a character from user, `putchar` means put A (=single) character in a variable.
-  In macro I've called `# define PI 3.14` (NOTE THAT here 3.14 is floating number). If I use `printf("%d",PI)` will give a garbage value . To solve the issue,  use the required data type here `printf("%f",PI)`. Similarly, if I've called `# define PI 314` which is nonfloating number but later `printf("%d",PI)`,  the output will be `0.000000`.
-  To get a string as input where it contains white space, use `scanf("%[\n]",stringname)` or `gets()` 
-  In C or C++, we cannot return multiple values from a function directly. But, We can return more than one values from a function by using the method called “call by address”, or “call by reference”. In the `invoker function`, we will use two variables to store the results, and the function will take pointer-type data. So we have to pass the address of the data.
-  `strlen()` works perfectly in char type array AKA string. But, return zero if there is no element and return if there are ANY ELEMENT in the array.
-  The allocation and deallocation for stack memory is automatically done. Since the stack memory of a function gets deallocated after the function returns, there is no guarantee that the value stored in those areas will stay the same. A common mistake is to return a pointer to a stack variable in a helper function.

## IbnulAbrarShahriarSeam
- Read the problem statement carefully.
- Try to find a mathematical solution rather than using a loop. Loops take a huge amount of time and memory to execute. A mathematical solution is almost always more efficient.
- If you are working with an integer-type variable, try not to use something that returns double or floating-point values (e.g., pow()). As it may result in unexpected behavior.

## sharafat
- At first I just used to read and read without practicing. Which is definitely a bad habit!
- How are you supposed to learn a software if you're afraid of an unknown button? This philosophy of mine both helped and got me into a tons of troubles.

# Contribution

Let the power of words weave its magic, igniting sparks of inspiration and fostering a vibrant community united by the beauty of language. Join us on this remarkable journey of sharing, connecting, and celebrating the extraordinary impact of words in our lives.

## How to Contribute
Upcoming...
