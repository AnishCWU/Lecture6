;Anish 
        segment .data
a       dq      0
sfmt1   db      "%ld", 0
pfmt1   db      "Enter an integer: ", 0
pfmt2   db      "%ld squared is %ld", 0x0a, 0

        segment .text
        global  main
        global  square
        extern  printf
        extern  scanf
        
square:
    push    rbp                 ; save the old base pointer
    mov     rbp, rsp            ; set the new base pointer
    mov     rax, rdi            ; copy the input value to rax
    mul     rdi                 ; square the input value
    pop     rbp                 ; restore the old base pointer
    ret                         ; return from the function

; The main function asks the user for an input, calls the square function,
; and prints the result to the terminal

main:
    push    rbp                 ; save the old base pointer
    mov     rbp, rsp            ; set the new base pointer
    mov     rdi, sfmt1          ; load the address of the format string
    lea     rsi, [rel pfmt1]    ; load the address of the prompt string
    mov     rax, 0              ; clear rax
    call    printf              ; print the prompt

    ; read an integer from the input string and store it in rdi
    mov     rax, 0              ; clear rax
    lea     rdi, [rel a]        ; load the address of the input variable
    mov     rsi, sfmt1          ; load the address of the format string
    call    scanf

    ; call the square function to square the input value
    mov     rdi, [rel a]        ; load the input value from memory
    call    square

    ; print the result to the terminal
    mov     rdi, pfmt2          ; load the address of the output string
    mov     rsi, [rel a]        ; load the input value
    mov     rdx, rax            ; load the result value
    mov     rax, 0              ; clear rax
    call    printf

    mov     rsp, rbp            ; restore the old stack pointer
    pop     rbp                 ; restore the old base pointer
                             ; return from the main function
    
    xor rax, rax
    leave
    ret 
    
