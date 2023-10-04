section .data
    a: dq 0             ; Integer input
    sfmt1: db "%ld", 0  ; Format string for scanf
    pfmt1: db "Enter an integer: ", 0   ; Prompt for input
    pfmt2: db "%ld squared is %ld", 0x0a, 0   ; Output format string

section .text
    global _start
    global square
    extern printf
    extern scanf

; main function
_start:
    push rbp            ; Save old base pointer
    mov rbp, rsp        ; Set new base pointer

    ; Print prompt and read input
    mov rdi, pfmt1      ; Load format string
    call printf         ; Print prompt
    mov rdi, a          ; Load address of a
    mov rsi, sfmt1      ; Load format string
    call scanf          ; Read input

    ; Call square function
    mov rdi, [a]        ; Load a into rdi
    call square         ; Calculate a^2

    ; Print result
    mov rdi, pfmt2      ; Load format string
    xor rsi, rsi        ; Clear rsi
    mov rdx, [a]        ; Load a into rdx
    call printf         ; Print result

    ; Exit program
    mov rax, 60
    xor rdi, rdi
    syscall

; square function
square:
    push rbp            ; Save old base pointer
    mov rbp, rsp        ; Set new base pointer

    ; Calculate a^2 and store result in a
    mov rax, [rbp+16]   ; Load a into rax
    mul rax             ; Multiply a by a
    mov [a], rax        ; Store result in a

    pop rbp             ; Restore old base pointer
    ret                 ; Return to caller





