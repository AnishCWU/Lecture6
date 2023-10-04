    segment .data
p   dq      5; creating varibale and assging value to dq
q   dq      0x015ed ; creating variable and assiging hexadecimal value to dq'
r   dq      -3  ; creating variable and assiging value to dq
s   dq      -4  ; creating varibale and assigning value to dq

    segment .text
    global main; link to main
    
main:
    mov     rax, [p]; place p in rax
    mov     rbx, [q] ; place q in rbx
    mov     rcx, [r] ; place r in rcx
    mov     rdx, [s] ; place s in rdx
    
    mov     r13, [p] ; add p to r13 to sum
    add     r13, [q] ; add q to r13 to sum 
    add     r13, [r] ; add r to r13 to sum 
    add     r13, [s] ; add s to r13 to sum 
    
    xor rax,rax
    leave ; 
    ret
    
    
