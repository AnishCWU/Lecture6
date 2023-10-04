section .data
    a  dq 57, 78, 63, 4, 60, 21, 32, 64, 1, 91   ; Array a
    b  dq 100, 75, 19, 77, 21, 17, 38, 16, 66, 41   ; Array b
    n  dq 10                                      ; Array length
    
section .bss
    c resq 10   
    
section .text
    global main

main:
    xor rax, rax             ; Set rax to 0

for:
    cmp rax, [n]             ; Check if rax is less than n
    jge exit                 ; If rax >= n, exit loop

    mov rbx, [a+rax]       ; Load a[i] into rbx
    mov rcx, [b+rax]       ; Load b[i] into rcx
    cmp rbx, rcx             ; Compare a[i] and b[i]
    jg store_in_c            ; If a[i] > b[i], store a[i] in c[i]
    mov [c+rax], rcx       ; Otherwise, store b[i] in c[i]
    jmp increment            ; Increment i and continue loop

    store_in_c:
    mov [c+rax], rbx       ; Store a[i] in c[i]

    increment:
    inc rax                  ; Increment i
    jmp for         ; Continue loop

exit:
    ; Exit program
    mov rax, 60
    xor rdi, rdi
    syscall
