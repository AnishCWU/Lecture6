    segment .data
p   db      3   ; assign value 3 to db as p variable
q   dw      11  ; assign value 11 to dw as q variable
r   dd      1213 ; assign value 1213 to dd as r variable
s   dq      12346578 ; assign value 3 to dq as s variable

sumPQRS dq 0    ; new variable with 0 value to dq 

    segment .text
    global main ;
    
main:
    movsx   rax,byte [p] ; p in rax
    movzx   rbx,word [q] ; q in rbx 
    movsx   rcx,dword [r] ; r in rcx
    mov     rdx,[s] ; s in rdx
    
    movzx r13, byte[p] ; p into r13 
    add   r13, rax     ; r13 to rax
    add   r13, rcx      ; r13 to rcx
    add   r13, rdx      ; r13 to rdx
    
    mov   [sumPQRS],r13
    
    xor rax, rax
    leave 
    ret
    
