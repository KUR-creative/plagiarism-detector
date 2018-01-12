	.file	"3.c"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB4:
	.text
.LHOTB4:
	.p2align 4,,15
	.globl	_Z11sqrtIntegerd
	.type	_Z11sqrtIntegerd, @function
_Z11sqrtIntegerd:
.LFB45:
	.cfi_startproc
	movapd	%xmm0, %xmm2
	movsd	.LC1(%rip), %xmm3
	movsd	.LC0(%rip), %xmm0
	movsd	.LC2(%rip), %xmm5
	movsd	.LC3(%rip), %xmm4
	jmp	.L5
	.p2align 4,,10
	.p2align 3
.L2:
	movapd	%xmm2, %xmm1
	divsd	%xmm0, %xmm1
	addsd	%xmm1, %xmm0
	mulsd	%xmm4, %xmm0
.L5:
	movapd	%xmm0, %xmm1
	mulsd	%xmm0, %xmm1
	subsd	%xmm2, %xmm1
	ucomisd	%xmm1, %xmm3
	ja	.L2
	ucomisd	%xmm5, %xmm1
	ja	.L2
	rep ret
	.cfi_endproc
.LFE45:
	.size	_Z11sqrtIntegerd, .-_Z11sqrtIntegerd
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC6:
	.string	"r"
.LC7:
	.string	"connect.inp"
.LC8:
	.string	"%lf"
.LC10:
	.string	"w"
.LC11:
	.string	"connect.out"
.LC12:
	.string	"%d"
	.section	.text.unlikely
.LCOLDB13:
	.section	.text.startup,"ax",@progbits
.LHOTB13:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB46:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	$.LC7, %edi
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	$.LC6, %esi
	addq	$-128, %rsp
	.cfi_def_cfa_offset 160
	movq	%fs:40, %rax
	movq	%rax, 120(%rsp)
	xorl	%eax, %eax
	call	fopen
	leaq	48(%rsp), %rdi
	movq	%rax, %rbp
	movl	$9, %ecx
	xorl	%eax, %eax
	leaq	48(%rsp), %rbx
	movq	$0, 16(%rsp)
	rep stosq
	leaq	72(%rbx), %r12
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
	.p2align 4,,10
	.p2align 3
.L9:
	movq	%rbx, %rdx
	xorl	%eax, %eax
	movl	$.LC8, %esi
	movq	%rbp, %rdi
	addq	$8, %rbx
	call	fscanf
	cmpq	%rbx, %r12
	jne	.L9
	movq	%rbp, %rdi
	call	fclose
	pxor	%xmm1, %xmm1
	leaq	72(%rsp), %rdx
	xorl	%eax, %eax
.L10:
	movsd	48(%rsp,%rax), %xmm0
	mulsd	%xmm1, %xmm0
	addsd	(%rdx,%rax), %xmm0
	movsd	%xmm0, 16(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L10
	movsd	96(%rsp), %xmm10
	movsd	16(%rsp), %xmm1
	movsd	104(%rsp), %xmm11
	movsd	24(%rsp), %xmm2
	subsd	%xmm10, %xmm1
	movsd	112(%rsp), %xmm12
	subsd	%xmm11, %xmm2
	movsd	32(%rsp), %xmm0
	movsd	.LC0(%rip), %xmm8
	subsd	%xmm12, %xmm0
	mulsd	%xmm1, %xmm1
	movapd	%xmm8, %xmm5
	movsd	.LC1(%rip), %xmm3
	mulsd	%xmm2, %xmm2
	movsd	.LC2(%rip), %xmm6
	mulsd	%xmm0, %xmm0
	addsd	%xmm2, %xmm1
	movsd	.LC3(%rip), %xmm2
	addsd	%xmm0, %xmm1
	jmp	.L14
	.p2align 4,,10
	.p2align 3
.L11:
	movapd	%xmm1, %xmm0
	divsd	%xmm5, %xmm0
	addsd	%xmm0, %xmm5
	mulsd	%xmm2, %xmm5
.L14:
	movapd	%xmm5, %xmm0
	mulsd	%xmm5, %xmm0
	subsd	%xmm1, %xmm0
	ucomisd	%xmm0, %xmm3
	ja	.L11
	ucomisd	%xmm6, %xmm0
	ja	.L11
	movsd	.LC5(%rip), %xmm9
	leaq	72(%rsp), %rdx
	movapd	%xmm8, %xmm13
	movl	$999, %ecx
	movapd	%xmm9, %xmm7
	movsd	.LC3(%rip), %xmm4
	.p2align 4,,10
	.p2align 3
.L21:
	movapd	%xmm8, %xmm2
	xorl	%eax, %eax
	subsd	%xmm7, %xmm2
.L15:
	movsd	(%rdx,%rax), %xmm1
	movsd	48(%rsp,%rax), %xmm0
	mulsd	%xmm2, %xmm1
	mulsd	%xmm7, %xmm0
	addsd	%xmm1, %xmm0
	movsd	%xmm0, 16(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L15
	movsd	16(%rsp), %xmm2
	movsd	24(%rsp), %xmm0
	subsd	%xmm10, %xmm2
	movsd	32(%rsp), %xmm1
	subsd	%xmm11, %xmm0
	subsd	%xmm12, %xmm1
	mulsd	%xmm2, %xmm2
	mulsd	%xmm0, %xmm0
	mulsd	%xmm1, %xmm1
	addsd	%xmm2, %xmm0
	movapd	%xmm0, %xmm2
	movapd	%xmm13, %xmm0
	addsd	%xmm1, %xmm2
	jmp	.L19
	.p2align 4,,10
	.p2align 3
.L16:
	movapd	%xmm2, %xmm1
	divsd	%xmm0, %xmm1
	addsd	%xmm1, %xmm0
	mulsd	%xmm4, %xmm0
.L19:
	movapd	%xmm0, %xmm1
	mulsd	%xmm0, %xmm1
	subsd	%xmm2, %xmm1
	ucomisd	%xmm1, %xmm3
	ja	.L16
	ucomisd	%xmm6, %xmm1
	ja	.L16
	minsd	%xmm5, %xmm0
	subl	$1, %ecx
	addsd	%xmm9, %xmm7
	movapd	%xmm0, %xmm5
	jne	.L21
	movl	$.LC10, %esi
	movl	$.LC11, %edi
	movsd	%xmm0, 8(%rsp)
	call	fopen
	movsd	8(%rsp), %xmm5
	movl	$1, %esi
	movq	%rax, %rdi
	movq	%rax, %rbx
	movl	$.LC12, %edx
	cvttsd2si	%xmm5, %ecx
	xorl	%eax, %eax
	addl	$1, %ecx
	call	__fprintf_chk
	movq	%rbx, %rdi
	call	fclose
	xorl	%eax, %eax
	movq	120(%rsp), %rsi
	xorq	%fs:40, %rsi
	jne	.L31
	subq	$-128, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L31:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE46:
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE13:
	.section	.text.startup
.LHOTE13:
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC0:
	.long	0
	.long	1072693248
	.align 8
.LC1:
	.long	1202590843
	.long	-1081836831
	.align 8
.LC2:
	.long	1202590843
	.long	1065646817
	.align 8
.LC3:
	.long	0
	.long	1071644672
	.align 8
.LC5:
	.long	3539053052
	.long	1062232653
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
