    segment .data
p   dw      135             ; assiging dw to variable p with value 135
q   dw      140             ; assiging dw to variable q with value 140
r   dw      112             ; assiging dw to variable r with value 112
    
pplusq      dw  0           ;  with 0 value, creating a variable pplusq on dw
pminusq     dw  0           ; with 0 value, creating a variable pminusq on dw
pplusr      dw  0           ; with 0 value, creating a variable pplusr on dw
pminusr     dw  0           ; with 0 value, creating a variable pminusr on dw


    segment .text
    global  main              ; linking the main
    
main:
    movzx     rax,word [p]    ; p into rax
    movzx     rbx,word [q]    ; q into rbx
    movzx     rcx,word [r]    ; r into rcx
    
    mov     r10, rax          ; rax into r10
    mov     r11, rax          ; rax into r11
    mov     r12, rax          ; rax into r12
    mov     r13, rax          ; rax into r13

    add     r10, rbx          ; add rbx to r10
    sub     r11, rbx          ; sub rbx from r11
    add     r12, rcx          ; add rcx to r12
    sub     r13, rcx          ; sub rcx from r13
            
    mov     [pplusq],  r10    ; r10 into pplusq
    mov     [pminusq], r11    ; r11 into pminusq
    mov     [pplusr],  r12    ; r12 into pplusr
    mov     [pminusr], r13    ; r13 into pminusr


    xor     rax, rax
    leave                     
    ret
