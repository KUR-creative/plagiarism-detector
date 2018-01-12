	.file	"1-4.cpp"
	.section	.text.unlikely._ZNSt6vectorIiSaIiEED2Ev,"axG",@progbits,_ZNSt6vectorIiSaIiEED5Ev,comdat
	.align 2
.LCOLDB0:
	.section	.text._ZNSt6vectorIiSaIiEED2Ev,"axG",@progbits,_ZNSt6vectorIiSaIiEED5Ev,comdat
.LHOTB0:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEED2Ev
	.type	_ZNSt6vectorIiSaIiEED2Ev, @function
_ZNSt6vectorIiSaIiEED2Ev:
.LFB8452:
	.cfi_startproc
	movq	(%rdi), %rdi
	testq	%rdi, %rdi
	je	.L1
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L1:
	rep ret
	.cfi_endproc
.LFE8452:
	.size	_ZNSt6vectorIiSaIiEED2Ev, .-_ZNSt6vectorIiSaIiEED2Ev
	.section	.text.unlikely._ZNSt6vectorIiSaIiEED2Ev,"axG",@progbits,_ZNSt6vectorIiSaIiEED5Ev,comdat
.LCOLDE0:
	.section	.text._ZNSt6vectorIiSaIiEED2Ev,"axG",@progbits,_ZNSt6vectorIiSaIiEED5Ev,comdat
.LHOTE0:
	.weak	_ZNSt6vectorIiSaIiEED1Ev
	.set	_ZNSt6vectorIiSaIiEED1Ev,_ZNSt6vectorIiSaIiEED2Ev
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
	.align 2
.LCOLDB1:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
.LHOTB1:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev
	.type	_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev, @function
_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev:
.LFB8994:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	8(%rdi), %rbp
	movq	(%rdi), %rbx
	cmpq	%rbx, %rbp
	je	.L5
	movq	%rdi, %r12
	.p2align 4,,10
	.p2align 3
.L7:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L6
	call	_ZdlPv
.L6:
	addq	$24, %rbx
	cmpq	%rbx, %rbp
	jne	.L7
	movq	(%r12), %rbp
.L5:
	testq	%rbp, %rbp
	je	.L4
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	movq	%rbp, %rdi
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L4:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8994:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
.LCOLDE1:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
.LHOTE1:
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev
	.set	_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev,_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.globl	_ZN4EdgeC2Eii
	.type	_ZN4EdgeC2Eii, @function
_ZN4EdgeC2Eii:
.LFB8315:
	.cfi_startproc
	movl	%esi, (%rdi)
	movl	%edx, 4(%rdi)
	ret
	.cfi_endproc
.LFE8315:
	.size	_ZN4EdgeC2Eii, .-_ZN4EdgeC2Eii
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.globl	_ZN4EdgeC1Eii
	.set	_ZN4EdgeC1Eii,_ZN4EdgeC2Eii
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.globl	_ZN5GraphC2Ei
	.type	_ZN5GraphC2Ei, @function
_ZN5GraphC2Ei:
.LFB8321:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movabsq	$382805968326492160, %rax
	movslq	%esi, %rbx
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	cmpq	%rax, %rbx
	movl	%esi, (%rdi)
	movl	$0, 4(%rdi)
	movq	$-1, %rdi
	ja	.L16
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L16:
	call	_Znam
	xorl	%ecx, %ecx
	movq	%rbx, (%rax)
	addq	$8, %rax
	testq	%rbx, %rbx
	movq	%rax, %rdx
	je	.L18
	.p2align 4,,10
	.p2align 3
.L21:
	addq	$1, %rcx
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rbx, %rcx
	jne	.L21
.L18:
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8321:
	.size	_ZN5GraphC2Ei, .-_ZN5GraphC2Ei
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.globl	_ZN5GraphC1Ei
	.set	_ZN5GraphC1Ei,_ZN5GraphC2Ei
	.section	.text.unlikely
	.align 2
.LCOLDB4:
	.text
.LHOTB4:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7addEdgeEii
	.type	_ZN5Graph7addEdgeEii, @function
_ZN5Graph7addEdgeEii:
.LFB8323:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movslq	%esi, %rsi
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	8(%rdi), %rax
	movl	%edx, %r12d
	leaq	(%rsi,%rsi,2), %rdx
	movq	%rdi, %rbx
	movl	$24, %edi
	leaq	(%rax,%rdx,8), %rbp
	call	_Znwm
	movq	%rbp, %rsi
	movl	%r12d, 16(%rax)
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbp)
	addl	$1, 4(%rbx)
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8323:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.text.unlikely
.LCOLDB5:
	.text
.LHOTB5:
	.p2align 4,,15
	.globl	_Z9vec_printRSt6vectorIiSaIiEERSo
	.type	_Z9vec_printRSt6vectorIiSaIiEERSo, @function
_Z9vec_printRSt6vectorIiSaIiEERSo:
.LFB8329:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	(%rdi), %rdx
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	movq	8(%rdi), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	testq	%rax, %rax
	je	.L27
	movq	%rdi, %rbp
	movq	%rsi, %r12
	xorl	%ebx, %ebx
	.p2align 4,,10
	.p2align 3
.L32:
	movl	(%rdx,%rbx,4), %esi
	movq	%r12, %rdi
	addq	$1, %rbx
	call	_ZNSolsEi
	leaq	7(%rsp), %rsi
	movl	$1, %edx
	movq	%rax, %rdi
	movb	$32, 7(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	0(%rbp), %rdx
	movq	8(%rbp), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	cmpq	%rbx, %rax
	ja	.L32
.L27:
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L35
	addq	$16, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L35:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE8329:
	.size	_Z9vec_printRSt6vectorIiSaIiEERSo, .-_Z9vec_printRSt6vectorIiSaIiEERSo
	.section	.text.unlikely
.LCOLDE5:
	.text
.LHOTE5:
	.section	.text.unlikely
.LCOLDB6:
	.text
.LHOTB6:
	.p2align 4,,15
	.globl	_Z11vec_compareRSt6vectorIiSaIiEES2_
	.type	_Z11vec_compareRSt6vectorIiSaIiEES2_, @function
_Z11vec_compareRSt6vectorIiSaIiEES2_:
.LFB8330:
	.cfi_startproc
	movq	(%rdi), %r8
	movq	8(%rdi), %rdi
	subq	%r8, %rdi
	sarq	$2, %rdi
	testq	%rdi, %rdi
	je	.L44
	movq	(%rsi), %rsi
	movl	(%rsi), %eax
	cmpl	%eax, (%r8)
	jg	.L43
	jl	.L44
	movl	$1, %eax
	jmp	.L38
	.p2align 4,,10
	.p2align 3
.L39:
	movl	(%r8,%rax,4), %ecx
	movl	(%rsi,%rax,4), %edx
	cmpl	%edx, %ecx
	jg	.L43
	addq	$1, %rax
	cmpl	%edx, %ecx
	jl	.L44
.L38:
	cmpq	%rdi, %rax
	jne	.L39
.L44:
	xorl	%eax, %eax
	ret
	.p2align 4,,10
	.p2align 3
.L43:
	movl	$1, %eax
	ret
	.cfi_endproc
.LFE8330:
	.size	_Z11vec_compareRSt6vectorIiSaIiEES2_, .-_Z11vec_compareRSt6vectorIiSaIiEES2_
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
	.align 2
.LCOLDB7:
	.section	.text._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LHOTB7:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEEaSERKS1_
	.type	_ZNSt6vectorIiSaIiEEaSERKS1_, @function
_ZNSt6vectorIiSaIiEEaSERKS1_:
.LFB8485:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	cmpq	%rdi, %rsi
	je	.L46
	movq	8(%rsi), %rdx
	movq	(%rsi), %r15
	movq	%rsi, %r12
	movq	(%rdi), %r13
	movq	16(%rdi), %rcx
	movq	%rdx, %rbp
	subq	%r15, %rbp
	subq	%r13, %rcx
	movq	%rbp, %r14
	sarq	$2, %rcx
	sarq	$2, %r14
	cmpq	%rcx, %r14
	ja	.L69
	movq	8(%rdi), %rdi
	movq	%rdi, %rax
	subq	%r13, %rax
	movq	%rax, %rcx
	sarq	$2, %rcx
	cmpq	%rcx, %r14
	jbe	.L70
	testq	%rcx, %rcx
	jne	.L71
.L56:
	leaq	(%r15,%rax), %rsi
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	testq	%rax, %rax
	jne	.L57
.L68:
	addq	%r13, %rbp
.L53:
	movq	%rbp, 8(%rbx)
.L46:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%rbx, %rax
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L70:
	.cfi_restore_state
	testq	%r14, %r14
	je	.L68
	movq	%rbp, %rdx
	movq	%r15, %rsi
	movq	%r13, %rdi
	call	memmove
	addq	(%rbx), %rbp
	jmp	.L53
	.p2align 4,,10
	.p2align 3
.L69:
	xorl	%r12d, %r12d
	testq	%r14, %r14
	je	.L51
	movabsq	$4611686018427387903, %rax
	cmpq	%rax, %r14
	ja	.L72
	movq	%rbp, %rdi
	call	_Znwm
	testq	%r14, %r14
	movq	%rax, %r12
	movq	(%rbx), %r13
	jne	.L73
.L51:
	testq	%r13, %r13
	je	.L52
.L74:
	movq	%r13, %rdi
	call	_ZdlPv
.L52:
	addq	%r12, %rbp
	movq	%r12, (%rbx)
	movq	%rbp, 16(%rbx)
	jmp	.L53
	.p2align 4,,10
	.p2align 3
.L73:
	movq	%rbp, %rdx
	movq	%r15, %rsi
	movq	%rax, %rdi
	call	memmove
	testq	%r13, %r13
	jne	.L74
	jmp	.L52
	.p2align 4,,10
	.p2align 3
.L57:
	call	memmove
	addq	(%rbx), %rbp
	jmp	.L53
	.p2align 4,,10
	.p2align 3
.L71:
	movq	%r13, %rdi
	movq	%rax, %rdx
	movq	%r15, %rsi
	call	memmove
	movq	8(%rbx), %rdi
	movq	(%rbx), %r13
	movq	(%r12), %r15
	movq	8(%r12), %rdx
	movq	%rdi, %rax
	subq	%r13, %rax
	jmp	.L56
.L72:
	call	_ZSt17__throw_bad_allocv
	.cfi_endproc
.LFE8485:
	.size	_ZNSt6vectorIiSaIiEEaSERKS1_, .-_ZNSt6vectorIiSaIiEEaSERKS1_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LCOLDE7:
	.section	.text._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LHOTE7:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
	.align 2
.LCOLDB8:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTB8:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_:
.LFB8575:
	.cfi_startproc
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	movq	%rsi, %r12
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movq	8(%rdi), %rax
	movq	%rdi, %rbx
	subq	(%rdi), %rax
	sarq	$2, %rax
	testq	%rax, %rax
	je	.L83
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L95
.L84:
	movq	$-4, %r13
	jmp	.L76
	.p2align 4,,10
	.p2align 3
.L83:
	movl	$4, %r13d
.L76:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L82:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movl	(%r12), %ecx
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	addq	%rdx, %r12
	je	.L78
	movl	%ecx, (%r12)
.L78:
	testq	%rax, %rax
	jne	.L96
	addq	$4, %r12
	testq	%r14, %r14
	je	.L81
.L80:
	movq	%r14, %rdi
	call	_ZdlPv
.L81:
	movq	%rbp, (%rbx)
	addq	%r13, %rbp
	movq	%r12, 8(%rbx)
	movq	%rbp, 16(%rbx)
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L96:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$4, %r12
	call	memmove
	jmp	.L80
.L95:
	movabsq	$4611686018427387903, %rcx
	cmpq	%rcx, %rdx
	ja	.L84
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L82
	leaq	0(,%rax,8), %r13
	jmp	.L76
	.cfi_endproc
.LFE8575:
	.size	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LCOLDE8:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTE8:
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely
.LCOLDB9:
	.text
.LHOTB9:
	.p2align 4,,15
	.globl	_Z11vector_pushRSt6vectorIiSaIiEEi
	.type	_Z11vector_pushRSt6vectorIiSaIiEEi, @function
_Z11vector_pushRSt6vectorIiSaIiEEi:
.LFB8313:
	.cfi_startproc
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	movq	8(%rdi), %r8
	movq	(%rdi), %rcx
	movl	%esi, 12(%rsp)
	movq	%r8, %rdx
	subq	%rcx, %rdx
	sarq	$2, %rdx
	testq	%rdx, %rdx
	je	.L98
	cmpl	%esi, (%rcx)
	je	.L97
	movl	$1, %eax
	jmp	.L100
	.p2align 4,,10
	.p2align 3
.L101:
	addq	$1, %rax
	cmpl	%esi, -4(%rcx,%rax,4)
	je	.L97
.L100:
	cmpq	%rdx, %rax
	jne	.L101
.L98:
	cmpq	%r8, 16(%rdi)
	je	.L102
	testq	%r8, %r8
	movl	12(%rsp), %eax
	je	.L103
	movl	%eax, (%r8)
.L103:
	addq	$4, %r8
	movq	%r8, 8(%rdi)
.L97:
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L102:
	.cfi_restore_state
	leaq	12(%rsp), %rsi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	jmp	.L97
	.cfi_endproc
.LFE8313:
	.size	_Z11vector_pushRSt6vectorIiSaIiEEi, .-_Z11vector_pushRSt6vectorIiSaIiEEi
	.section	.text.unlikely
.LCOLDE9:
	.text
.LHOTE9:
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB10:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,comdat
.LHOTB10:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_
	.type	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_, @function
_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_:
.LFB8730:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movabsq	$-6148914691236517205, %rcx
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rsi, %rbx
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	8(%rdi), %r14
	movq	(%rdi), %rax
	movq	%r14, %rdx
	subq	%rax, %rdx
	movq	%rdx, %rsi
	sarq	$3, %rsi
	imulq	%rsi, %rcx
	testq	%rcx, %rcx
	je	.L122
	leaq	(%rcx,%rcx), %rsi
	cmpq	%rsi, %rcx
	jbe	.L139
.L123:
	movq	$-16, %r13
.L112:
	movq	%r13, %rdi
	call	_Znwm
	movq	8(%rbp), %r14
	movq	%rax, %r12
	addq	%rax, %r13
	movq	0(%rbp), %rax
	leaq	24(%r12), %r15
	movq	%r14, %rdx
	subq	%rax, %rdx
.L121:
	addq	%r12, %rdx
	je	.L124
	movq	(%rbx), %rax
	movq	$0, (%rbx)
	movq	%rax, (%rdx)
	movq	8(%rbx), %rax
	movq	$0, 8(%rbx)
	movq	%rax, 8(%rdx)
	movq	16(%rbx), %rax
	movq	$0, 16(%rbx)
	movq	8(%rbp), %r14
	movq	0(%rbp), %rdi
	movq	%rax, 16(%rdx)
.L114:
	cmpq	%r14, %rdi
	je	.L115
	movq	%r12, %rax
	movq	%rdi, %rdx
	.p2align 4,,10
	.p2align 3
.L117:
	testq	%rax, %rax
	je	.L116
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
	movq	$0, (%rax)
	movq	(%rdx), %rcx
	movq	%rcx, (%rax)
	movq	$0, (%rdx)
	movq	8(%rdx), %rsi
	movq	8(%rax), %rcx
	movq	%rsi, 8(%rax)
	movq	%rcx, 8(%rdx)
	movq	16(%rdx), %rsi
	movq	16(%rax), %rcx
	movq	%rsi, 16(%rax)
	movq	%rcx, 16(%rdx)
.L116:
	addq	$24, %rdx
	addq	$24, %rax
	cmpq	%r14, %rdx
	jne	.L117
	leaq	24(%rdi), %rax
	movq	0(%rbp), %rbx
	subq	%rax, %r14
	shrq	$3, %r14
	leaq	48(%r12,%r14,8), %r15
	movq	8(%rbp), %r14
	cmpq	%rbx, %r14
	je	.L115
	.p2align 4,,10
	.p2align 3
.L119:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L118
	call	_ZdlPv
.L118:
	addq	$24, %rbx
	cmpq	%r14, %rbx
	jne	.L119
	movq	0(%rbp), %r14
.L115:
	testq	%r14, %r14
	je	.L120
	movq	%r14, %rdi
	call	_ZdlPv
.L120:
	movq	%r12, 0(%rbp)
	movq	%r15, 8(%rbp)
	movq	%r13, 16(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L122:
	.cfi_restore_state
	movl	$24, %r13d
	jmp	.L112
	.p2align 4,,10
	.p2align 3
.L124:
	movq	%rax, %rdi
	jmp	.L114
.L139:
	movabsq	$768614336404564650, %rdi
	cmpq	%rdi, %rsi
	ja	.L123
	testq	%rsi, %rsi
	jne	.L140
	movl	$24, %r15d
	xorl	%r13d, %r13d
	xorl	%r12d, %r12d
	jmp	.L121
.L140:
	leaq	(%rsi,%rcx,4), %r13
	salq	$3, %r13
	jmp	.L112
	.cfi_endproc
.LFE8730:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,comdat
.LCOLDE10:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_,comdat
.LHOTE10:
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIIS1_EEEvDpOT_
	.set	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIIS1_EEEvDpOT_,_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB11:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LHOTB11:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.type	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_, @function
_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_:
.LFB8598:
	.cfi_startproc
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L142
	testq	%rax, %rax
	je	.L143
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
	movq	$0, (%rax)
	movq	(%rsi), %rdx
	movq	%rdx, (%rax)
	movq	$0, (%rsi)
	movq	8(%rsi), %rcx
	movq	8(%rax), %rdx
	movq	%rcx, 8(%rax)
	movq	%rdx, 8(%rsi)
	movq	16(%rsi), %rcx
	movq	16(%rax), %rdx
	movq	%rcx, 16(%rax)
	movq	%rdx, 16(%rsi)
	movq	8(%rdi), %rax
.L143:
	addq	$24, %rax
	movq	%rax, 8(%rdi)
	ret
	.p2align 4,,10
	.p2align 3
.L142:
	jmp	_ZNSt6vectorIS_IiSaIiEESaIS1_EE19_M_emplace_back_auxIJS1_EEEvDpOT_
	.cfi_endproc
.LFE8598:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LCOLDE11:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LHOTE11:
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIIS1_EEEvDpOT_
	.set	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIIS1_EEEvDpOT_,_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.section	.text.unlikely
	.align 2
.LCOLDB12:
	.text
.LHOTB12:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.type	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, @function
_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_:
.LFB8324:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8324
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdx, %rax
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movl	%esi, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rcx, %r13
	subq	$120, %rsp
	.cfi_def_cfa_offset 176
	movq	%rdx, 8(%rsp)
	movslq	%esi, %rdx
	movq	%rcx, 64(%rsp)
	leaq	0(,%rdx,4), %rsi
	movq	%rdi, 40(%rsp)
	movq	%r9, 24(%rsp)
	movq	%fs:40, %rcx
	movq	%rcx, 104(%rsp)
	xorl	%ecx, %ecx
	addq	%rsi, %rax
	addq	%rsi, %r13
	movq	%rsi, 32(%rsp)
	movq	%rax, %rcx
	movq	%rax, 56(%rsp)
	movl	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip), %eax
	movl	$0, 72(%rsp)
	addl	$1, %eax
	movl	%eax, 0(%r13)
	movl	%eax, _ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip)
	movl	%eax, (%rcx)
	leaq	(%rdx,%rdx,2), %rax
	movq	8(%rdi), %rcx
	leal	1(%r12), %edx
	salq	$3, %rax
	movq	%rax, 16(%rsp)
	addq	%rcx, %rax
	movl	%edx, 76(%rsp)
	movq	(%rax), %rbp
	cmpq	%rax, %rbp
	je	.L149
	movq	%r8, %rbx
	jmp	.L171
	.p2align 4,,10
	.p2align 3
.L151:
	movq	24(%rsp), %rax
	movq	32(%rsp), %rdi
	cmpl	(%rax,%rdi), %r15d
	je	.L154
	cmpl	0(%r13), %edx
	jge	.L154
	movl	%edx, 0(%r13)
	movl	$24, %edi
.LEHB0:
	call	_Znwm
	movq	%rbx, %rsi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r12d, 16(%rax)
	movl	%r15d, 20(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
.L182:
	movq	40(%rsp), %rax
	movq	8(%rax), %rcx
.L154:
	movq	16(%rsp), %rax
	movq	0(%rbp), %rbp
	addq	%rcx, %rax
	cmpq	%rax, %rbp
	je	.L149
.L171:
	movslq	16(%rbp), %rax
	movq	8(%rsp), %rdx
	movl	(%rdx,%rax,4), %edx
	movq	%rax, %r15
	leaq	0(,%rax,4), %r11
	cmpl	$-1, %edx
	jne	.L151
	movq	24(%rsp), %r14
	movl	$24, %edi
	movq	%r11, 48(%rsp)
	addl	$1, 72(%rsp)
	movl	%r12d, (%r14,%rax,4)
	call	_Znwm
	movq	%rbx, %rsi
	movq	%rax, %rdi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r12d, 16(%rax)
	movl	%r15d, 20(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	movq	%r14, %r9
	movq	64(%rsp), %r14
	movq	8(%rsp), %rdx
	movq	40(%rsp), %rdi
	movq	%rbx, %r8
	movl	%r15d, %esi
	movq	%r14, %rcx
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	movq	48(%rsp), %r11
	movl	0(%r13), %eax
	addq	%r14, %r11
	cmpl	%eax, (%r11)
	cmovle	(%r11), %eax
	movl	%eax, 0(%r13)
	movq	56(%rsp), %rax
	movl	(%rax), %eax
	cmpl	$1, %eax
	je	.L185
	jle	.L182
	cmpl	(%r11), %eax
	jg	.L182
	jmp	.L173
	.p2align 4,,10
	.p2align 3
.L155:
	movslq	cCnt(%rip), %rax
	addl	$1, %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
	movq	8(%rbx), %rax
	movl	20(%rax), %esi
	movslq	cCnt(%rip), %rax
	addl	$1, %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
	movq	8(%rbx), %r14
	subq	$1, 16(%rbx)
	movq	%r14, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r14, %rdi
	call	_ZdlPv
.L173:
	movq	8(%rbx), %rax
	movl	16(%rax), %esi
	cmpl	%esi, %r12d
	jne	.L155
	cmpl	20(%rax), %r15d
	jne	.L155
	movslq	cCnt(%rip), %rax
	movl	76(%rsp), %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
	movq	8(%rbx), %rax
	movl	20(%rax), %esi
	movslq	cCnt(%rip), %rax
	addl	$1, %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
.LEHE0:
	movq	8(%rbx), %rax
	subq	$1, 16(%rbx)
	movq	%rax, %rdi
	movq	%rax, 48(%rsp)
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	48(%rsp), %rax
	movq	%rax, %rdi
	call	_ZdlPv
	leaq	80(%rsp), %rsi
	movl	$cmp_set, %edi
	addl	$1, cCnt(%rip)
	movq	$0, 80(%rsp)
	movq	$0, 88(%rsp)
	movq	$0, 96(%rsp)
.LEHB1:
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
.LEHE1:
	movq	80(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L182
	call	_ZdlPv
	movq	40(%rsp), %rax
	movq	8(%rax), %rcx
	jmp	.L154
	.p2align 4,,10
	.p2align 3
.L149:
	movq	104(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L186
	addq	$120, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L185:
	.cfi_restore_state
	cmpl	$1, 72(%rsp)
	jne	.L173
	jmp	.L182
.L164:
	movq	80(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L161
	call	_ZdlPv
.L161:
	movq	%rbx, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
.L186:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8324:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA8324:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8324-.LLSDACSB8324
.LLSDACSB8324:
	.uleb128 .LEHB0-.LFB8324
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB8324
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L164-.LFB8324
	.uleb128 0
	.uleb128 .LEHB2-.LFB8324
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE8324:
	.text
	.size	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, .-_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.section	.text.unlikely
.LCOLDE12:
	.text
.LHOTE12:
	.section	.text.unlikely
	.align 2
.LCOLDB13:
	.text
.LHOTB13:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph3BCCEv
	.type	_ZN5Graph3BCCEv, @function
_ZN5Graph3BCCEv:
.LFB8325:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8325
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movabsq	$2287828610704211968, %rbx
	subq	$56, %rsp
	.cfi_def_cfa_offset 112
	movq	%fs:40, %rax
	movq	%rax, 40(%rsp)
	xorl	%eax, %eax
	movslq	(%rdi), %rax
	cmpq	%rbx, %rax
	ja	.L188
	movq	%rdi, %r13
	leaq	0(,%rax,4), %rdi
.LEHB3:
	call	_Znam
	movq	%rax, %r12
	movslq	0(%r13), %rax
	cmpq	%rbx, %rax
	ja	.L188
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movq	%rax, (%rsp)
	movslq	0(%r13), %rax
	cmpq	%rbx, %rax
	ja	.L188
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movslq	4(%r13), %rbp
	movq	%rax, %r15
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %rbp
	ja	.L190
	leaq	0(%rbp,%rbp,2), %rax
	leaq	8(,%rax,8), %rdi
.L190:
	call	_Znam
	movq	%rbp, (%rax)
	movq	%rax, %rbx
	leaq	8(%rax), %rax
	xorl	%edx, %edx
	testq	%rbp, %rbp
	movq	%rax, 8(%rsp)
	je	.L193
	.p2align 4,,10
	.p2align 3
.L217:
	addq	$1, %rdx
	movq	$0, 16(%rax)
	movq	%rax, (%rax)
	movq	%rax, 8(%rax)
	addq	$24, %rax
	cmpq	%rdx, %rbp
	jne	.L217
.L193:
	movl	0(%r13), %edx
	xorl	%eax, %eax
	testl	%edx, %edx
	jle	.L187
	.p2align 4,,10
	.p2align 3
.L214:
	movq	(%rsp), %rcx
	movl	$-1, (%r12,%rax,4)
	movl	$-1, (%r15,%rax,4)
	movl	$-1, (%rcx,%rax,4)
	addq	$1, %rax
	cmpl	%eax, %edx
	jg	.L214
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L201:
	cmpl	$-1, (%r12,%rbp,4)
	je	.L225
.L195:
	cmpq	$0, 24(%rbx)
	je	.L196
	.p2align 4,,10
	.p2align 3
.L213:
	movq	16(%rbx), %rax
	movl	16(%rax), %esi
	movslq	cCnt(%rip), %rax
	addl	$1, %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
	movq	16(%rbx), %rax
	movl	20(%rax), %esi
	movslq	cCnt(%rip), %rax
	addl	$1, %esi
	leaq	(%rax,%rax,2), %rdx
	movq	cmp_set(%rip), %rax
	leaq	(%rax,%rdx,8), %rdi
	call	_Z11vector_pushRSt6vectorIiSaIiEEi
.LEHE3:
	movq	16(%rbx), %r14
	subq	$1, 24(%rbx)
	movq	%r14, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r14, %rdi
	call	_ZdlPv
	cmpq	$0, 24(%rbx)
	jne	.L213
	leaq	16(%rsp), %rsi
	movl	$cmp_set, %edi
	addl	$1, cCnt(%rip)
	movq	$0, 16(%rsp)
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
.LEHB4:
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
.LEHE4:
	movq	16(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L196
	call	_ZdlPv
.L196:
	leal	1(%rbp), %eax
	addq	$1, %rbp
	cmpl	%eax, 0(%r13)
	jg	.L201
.L187:
	movq	40(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L226
	addq	$56, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L225:
	.cfi_restore_state
	movq	8(%rsp), %r8
	movq	(%rsp), %rcx
	movq	%r15, %r9
	movq	%r12, %rdx
	movl	%ebp, %esi
	movq	%r13, %rdi
.LEHB5:
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	jmp	.L195
.L188:
	call	__cxa_throw_bad_array_new_length
.L226:
	call	__stack_chk_fail
.L208:
	movq	16(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L203
	call	_ZdlPv
.L203:
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE5:
	.cfi_endproc
.LFE8325:
	.section	.gcc_except_table
.LLSDA8325:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8325-.LLSDACSB8325
.LLSDACSB8325:
	.uleb128 .LEHB3-.LFB8325
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB4-.LFB8325
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L208-.LFB8325
	.uleb128 0
	.uleb128 .LEHB5-.LFB8325
	.uleb128 .LEHE5-.LEHB5
	.uleb128 0
	.uleb128 0
.LLSDACSE8325:
	.text
	.size	_ZN5Graph3BCCEv, .-_ZN5Graph3BCCEv
	.section	.text.unlikely
.LCOLDE13:
	.text
.LHOTE13:
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDB14:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTB14:
	.p2align 4,,15
	.weak	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.type	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, @function
_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_:
.LFB8834:
	.cfi_startproc
	cmpq	%rdi, %rsi
	je	.L244
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	leaq	4(%rdi), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	cmpq	%rsi, %rbp
	je	.L227
	movq	%rsi, %r14
	movq	%rdi, %r13
	movl	$4, %r12d
	.p2align 4,,10
	.p2align 3
.L235:
	movl	0(%rbp), %ebx
	cmpl	0(%r13), %ebx
	jl	.L246
	movl	-4(%rbp), %edx
	leaq	-4(%rbp), %rax
	cmpl	%edx, %ebx
	jl	.L234
	jmp	.L247
	.p2align 4,,10
	.p2align 3
.L237:
	movq	%rcx, %rax
.L234:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %ebx
	jl	.L237
.L233:
	movl	%ebx, (%rax)
.L232:
	addq	$4, %rbp
	cmpq	%rbp, %r14
	jne	.L235
.L227:
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_restore 13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_restore 14
	.cfi_def_cfa_offset 8
.L244:
	rep ret
	.p2align 4,,10
	.p2align 3
.L246:
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	.cfi_offset 6, -40
	.cfi_offset 12, -32
	.cfi_offset 13, -24
	.cfi_offset 14, -16
	movq	%rbp, %rdx
	subq	%r13, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	testq	%rax, %rax
	je	.L231
	movq	%r12, %rdi
	movq	%r13, %rsi
	subq	%rdx, %rdi
	addq	%rbp, %rdi
	call	memmove
.L231:
	movl	%ebx, 0(%r13)
	jmp	.L232
.L247:
	movq	%rbp, %rax
	jmp	.L233
	.cfi_endproc
.LFE8834:
	.size	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, .-_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDE14:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTE14:
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDB15:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTB15:
	.p2align 4,,15
	.weak	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.type	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, @function
_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_:
.LFB8964:
	.cfi_startproc
	leaq	-1(%rdx), %rax
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rax, %r12
	shrq	$63, %r12
	addq	%rax, %r12
	sarq	%r12
	cmpq	%r12, %rsi
	jge	.L249
	movq	%rsi, %r10
	jmp	.L251
	.p2align 4,,10
	.p2align 3
.L259:
	movq	%rax, %r10
.L251:
	leaq	1(%r10), %r8
	leaq	(%r8,%r8), %rax
	leaq	(%rdi,%r8,8), %r8
	leaq	-1(%rax), %r11
	movl	(%r8), %r9d
	leaq	(%rdi,%r11,4), %rbp
	movl	0(%rbp), %ebx
	cmpl	%r9d, %ebx
	jle	.L250
	movq	%rbp, %r8
	movl	%ebx, %r9d
	movq	%r11, %rax
.L250:
	cmpq	%r12, %rax
	movl	%r9d, (%rdi,%r10,4)
	jl	.L259
	testb	$1, %dl
	jne	.L252
.L258:
	subq	$2, %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%r9, %rdx
	sarq	%rdx
	cmpq	%rax, %rdx
	je	.L263
.L252:
	cmpq	%rsi, %rax
	jle	.L253
	leaq	-1(%rax), %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%rdx, %r9
	sarq	%r9
	movl	(%rdi,%r9,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L253
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	movl	%r10d, (%rdi,%rax,4)
	jge	.L253
.L256:
	leaq	-1(%r9), %rax
	movq	%rax, %rdx
	shrq	$63, %rdx
	addq	%rax, %rdx
	movq	%r9, %rax
	sarq	%rdx
	movl	(%rdi,%rdx,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L253
	movq	%rdx, %r9
	movl	%r10d, (%rdi,%rax,4)
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	jl	.L256
.L253:
	movl	%ecx, (%r8)
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L263:
	.cfi_restore_state
	leaq	1(%rax,%rax), %rax
	leaq	(%rdi,%rax,4), %rdx
	movl	(%rdx), %r9d
	movl	%r9d, (%r8)
	movq	%rdx, %r8
	jmp	.L252
.L249:
	testb	$1, %dl
	leaq	(%rdi,%rsi,4), %r8
	movq	%rsi, %rax
	je	.L258
	jmp	.L253
	.cfi_endproc
.LFE8964:
	.size	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, .-_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDE15:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTE15:
	.section	.text.unlikely
.LCOLDB16:
	.text
.LHOTB16:
	.p2align 4,,15
	.type	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73, @function
_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73:
.LFB9070:
	.cfi_startproc
	movq	%rsi, %rax
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	movq	%rsi, %r14
	subq	%rdi, %rax
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	cmpq	$67, %rax
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	jle	.L264
	testq	%rdx, %rdx
	movq	%rdi, %r12
	movq	%rdx, %r13
	je	.L266
	leaq	8(%rdi), %rbx
	movq	%rsi, %rbp
.L267:
	subq	%r12, %rbp
	movl	4(%r12), %edi
	subq	$1, %r13
	sarq	$2, %rbp
	movl	-4(%rsi), %ecx
	movq	%rbp, %rax
	shrq	$63, %rax
	addq	%rax, %rbp
	sarq	%rbp
	leaq	(%r12,%rbp,4), %rdx
	movl	(%rdx), %eax
	cmpl	%eax, %edi
	jge	.L272
	cmpl	%ecx, %eax
	jl	.L278
	cmpl	%ecx, %edi
	jge	.L290
.L291:
	movl	(%r12), %edx
	movl	%ecx, (%r12)
	movl	%edx, -4(%rsi)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
.L274:
	movq	%rbx, %r8
	movq	%rsi, %rcx
	.p2align 4,,10
	.p2align 3
.L276:
	leaq	-4(%r8), %rbp
	cmpl	%edi, %r9d
	movq	%rbp, %r14
	jl	.L279
	cmpl	%edi, %edx
	leaq	-4(%rcx), %rax
	jle	.L286
	leaq	-8(%rcx), %rax
	.p2align 4,,10
	.p2align 3
.L281:
	movq	%rax, %rcx
	subq	$4, %rax
	movl	4(%rax), %edx
	cmpl	%edi, %edx
	jg	.L281
	cmpq	%rcx, %rbp
	jnb	.L292
.L282:
	movl	%edx, -4(%r8)
	movl	%r9d, (%rcx)
	movl	-4(%rcx), %edx
	movl	(%r12), %edi
.L279:
	movl	(%r8), %r9d
	addq	$4, %r8
	jmp	.L276
.L286:
	movq	%rax, %rcx
	cmpq	%rcx, %rbp
	jb	.L282
.L292:
	movq	%r13, %rdx
	movq	%rbp, %rdi
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73
	movq	%rbp, %rax
	subq	%r12, %rax
	cmpq	$67, %rax
	jle	.L264
	testq	%r13, %r13
	je	.L266
	movq	%rbp, %rsi
	jmp	.L267
.L272:
	cmpl	%ecx, %edi
	jl	.L290
	cmpl	%ecx, %eax
	jl	.L291
.L278:
	movl	(%r12), %ecx
	movl	%eax, (%r12)
	movl	%ecx, (%rdx)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
	movl	-4(%rsi), %edx
	jmp	.L274
.L290:
	movl	(%r12), %r9d
	movl	%edi, (%r12)
	movl	%r9d, 4(%r12)
	movl	-4(%rsi), %edx
	jmp	.L274
.L266:
	sarq	$2, %rax
	leaq	-2(%rax), %rbp
	movq	%rax, %rbx
	sarq	%rbp
	jmp	.L269
.L293:
	subq	$1, %rbp
.L269:
	subq	$8, %rsp
	.cfi_def_cfa_offset 56
	movl	(%r12,%rbp,4), %ecx
	movq	%rbp, %rsi
	pushq	$0
	.cfi_def_cfa_offset 64
	movq	%rbx, %rdx
	movq	%r12, %rdi
	call	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	testq	%rbp, %rbp
	popq	%rcx
	.cfi_def_cfa_offset 56
	popq	%rsi
	.cfi_def_cfa_offset 48
	jne	.L293
	subq	$4, %r14
.L270:
	movl	(%r12), %eax
	movq	%r14, %rbx
	movl	(%r14), %ecx
	subq	$8, %rsp
	.cfi_def_cfa_offset 56
	subq	%r12, %rbx
	xorl	%esi, %esi
	movq	%rbx, %rdx
	movq	%r12, %rdi
	subq	$4, %r14
	movl	%eax, 4(%r14)
	pushq	$0
	.cfi_def_cfa_offset 64
	sarq	$2, %rdx
	call	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	cmpq	$7, %rbx
	popq	%rax
	.cfi_def_cfa_offset 56
	popq	%rdx
	.cfi_def_cfa_offset 48
	jg	.L270
.L264:
	popq	%rbx
	.cfi_def_cfa_offset 40
	popq	%rbp
	.cfi_def_cfa_offset 32
	popq	%r12
	.cfi_def_cfa_offset 24
	popq	%r13
	.cfi_def_cfa_offset 16
	popq	%r14
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9070:
	.size	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73, .-_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73
	.section	.text.unlikely
.LCOLDE16:
	.text
.LHOTE16:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC17:
	.string	"food.inp"
.LC18:
	.string	"food.out"
	.section	.text.unlikely
.LCOLDB19:
	.section	.text.startup,"ax",@progbits
.LHOTB19:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB8331:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8331
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movl	$8, %edx
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movl	$.LC17, %esi
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$1096, %rsp
	.cfi_def_cfa_offset 1152
	leaq	560(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1080(%rsp)
	xorl	%eax, %eax
.LEHB6:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE6:
	leaq	48(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC18, %esi
.LEHB7:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE7:
	leaq	560(%rsp), %rdi
	movl	$N, %esi
.LEHB8:
	call	_ZNSirsERi
.LEHE8:
	leaq	16(%rsp), %rsi
	movl	$cmp_set, %edi
	movq	$0, 16(%rsp)
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
.LEHB9:
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE12emplace_backIJS1_EEEvDpOT_
.LEHE9:
	movq	16(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L295
	call	_ZdlPv
.L295:
	movl	N(%rip), %esi
	leaq	16(%rsp), %rdi
.LEHB10:
	call	_ZN5GraphC1Ei
	movl	N(%rip), %r9d
	testl	%r9d, %r9d
	jle	.L296
	xorl	%ebp, %ebp
	jmp	.L325
	.p2align 4,,10
	.p2align 3
.L297:
	addl	$1, %ebp
	cmpl	%ebp, N(%rip)
	jle	.L296
.L325:
	leaq	8(%rsp), %rsi
	leaq	560(%rsp), %rdi
	call	_ZNSirsERi
	.p2align 4,,10
	.p2align 3
.L299:
	leaq	12(%rsp), %rsi
	leaq	560(%rsp), %rdi
	call	_ZNSirsERi
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L297
	movl	12(%rsp), %eax
	testl	%eax, %eax
	je	.L297
	leal	-1(%rax), %r12d
	movl	8(%rsp), %eax
	movl	$24, %edi
	subl	$1, %eax
	cltq
	leaq	(%rax,%rax,2), %rdx
	movq	24(%rsp), %rax
	leaq	(%rax,%rdx,8), %rbx
	call	_Znwm
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%rbx, %rsi
	movl	%r12d, 16(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	addl	$1, 20(%rsp)
	jmp	.L299
	.p2align 4,,10
	.p2align 3
.L296:
	leaq	16(%rsp), %rdi
	call	_ZN5Graph3BCCEv
	movl	cCnt(%rip), %r8d
	xorl	%r14d, %r14d
	xorl	%ebx, %ebx
	movq	cmp_set(%rip), %rsi
	movl	$63, %ebp
	testl	%r8d, %r8d
	jle	.L301
	.p2align 4,,10
	.p2align 3
.L348:
	leaq	(%rsi,%r14), %rax
	movq	8(%rax), %r15
	movq	(%rax), %r13
	cmpq	%r15, %r13
	movq	%r13, %rax
	je	.L303
	movq	%r15, %r12
	movq	%rbp, %rdx
	movq	%r15, %rsi
	subq	%r13, %r12
	movq	%r13, %rdi
	movq	%r12, %rax
	sarq	$2, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.73
	cmpq	$67, %r12
	jle	.L304
	subq	$8, %rsp
	.cfi_def_cfa_offset 1160
	leaq	64(%r13), %r12
	movq	%r13, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1168
	movq	%r12, %rsi
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	cmpq	%r12, %r15
	popq	%rsi
	.cfi_def_cfa_offset 1160
	popq	%rdi
	.cfi_def_cfa_offset 1152
	movq	%r12, %rdi
	je	.L351
	.p2align 4,,10
	.p2align 3
.L342:
	movl	(%rdi), %esi
	movl	-4(%rdi), %edx
	leaq	-4(%rdi), %rax
	cmpl	%edx, %esi
	jl	.L307
	jmp	.L355
	.p2align 4,,10
	.p2align 3
.L332:
	movq	%rcx, %rax
.L307:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %esi
	jl	.L332
	addq	$4, %rdi
	movl	%esi, (%rax)
	cmpq	%rdi, %r15
	jne	.L342
.L351:
	movq	cmp_set(%rip), %rsi
	leaq	(%rsi,%r14), %rdx
	movq	(%rdx), %rax
	movq	8(%rdx), %r13
.L303:
	subq	%rax, %r13
	movslq	cmp_max_sz(%rip), %rax
	sarq	$2, %r13
	cmpq	%r13, %rax
	jnb	.L309
	movl	%r13d, cmp_max_sz(%rip)
.L309:
	movslq	cCnt(%rip), %rax
	addl	$1, %ebx
	addq	$24, %r14
	cmpl	%ebx, %eax
	jg	.L348
	testl	%eax, %eax
	jle	.L301
	movq	8(%rsi), %rdx
	subq	(%rsi), %rdx
	movslq	cmp_max_sz(%rip), %r9
	sarq	$2, %rdx
	cmpq	%rdx, %r9
	je	.L301
	leaq	24(%rsi), %rdi
	xorl	%edx, %edx
.L313:
	addl	$1, %edx
	cmpl	%edx, %eax
	jne	.L327
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %rsi
.L301:
	movl	$trg_cmp, %edi
	call	_ZNSt6vectorIiSaIiEEaSERKS1_
	movl	cCnt(%rip), %eax
	testl	%eax, %eax
	jle	.L315
	xorl	%ebp, %ebp
	xorl	%ebx, %ebx
	jmp	.L316
	.p2align 4,,10
	.p2align 3
.L317:
	addl	$1, %ebx
	addq	$24, %rbp
	cmpl	%ebx, cCnt(%rip)
	jle	.L315
.L316:
	movq	%rbp, %rsi
	addq	cmp_set(%rip), %rsi
	movslq	cmp_max_sz(%rip), %rdx
	movq	(%rsi), %rdi
	movq	8(%rsi), %rax
	subq	%rdi, %rax
	sarq	$2, %rax
	cmpq	%rax, %rdx
	jne	.L317
	movq	trg_cmp(%rip), %r9
	movq	trg_cmp+8(%rip), %r8
	subq	%r9, %r8
	sarq	$2, %r8
	testq	%r8, %r8
	je	.L317
	movl	(%rdi), %eax
	cmpl	%eax, (%r9)
	jg	.L318
	jl	.L317
	movl	$1, %eax
	jmp	.L319
	.p2align 4,,10
	.p2align 3
.L356:
	addq	$1, %rax
	cmpl	%edx, %ecx
	jl	.L317
.L319:
	cmpq	%rax, %r8
	je	.L317
	movl	(%r9,%rax,4), %ecx
	movl	(%rdi,%rax,4), %edx
	cmpl	%edx, %ecx
	jle	.L356
.L318:
	movl	$trg_cmp, %edi
	call	_ZNSt6vectorIiSaIiEEaSERKS1_
	addl	$1, %ebx
	addq	$24, %rbp
	cmpl	%ebx, cCnt(%rip)
	jg	.L316
.L315:
	leaq	48(%rsp), %rsi
	movl	$trg_cmp, %edi
	call	_Z9vec_printRSt6vectorIiSaIiEERSo
	leaq	48(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE5closeEv
.LEHE10:
	leaq	48(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	560(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1080(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L357
	addq	$1096, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L304:
	.cfi_restore_state
	subq	$8, %rsp
	.cfi_def_cfa_offset 1160
	movq	%r15, %rsi
	movq	%r13, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1168
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	movq	cmp_set(%rip), %rsi
	leaq	(%rsi,%r14), %rdx
	movq	(%rdx), %rax
	movq	8(%rdx), %r13
	popq	%rdx
	.cfi_def_cfa_offset 1160
	popq	%rcx
	.cfi_def_cfa_offset 1152
	jmp	.L303
.L355:
	movq	%rdi, %rax
	addq	$4, %rdi
	cmpq	%rdi, %r15
	movl	%esi, (%rax)
	jne	.L342
	jmp	.L351
.L327:
	movq	%rdi, %r8
	addq	$24, %rdi
	movq	8(%r8), %rcx
	subq	(%r8), %rcx
	sarq	$2, %rcx
	cmpq	%r9, %rcx
	jne	.L313
	movq	%r8, %rsi
	jmp	.L301
.L335:
	movq	16(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L323
	call	_ZdlPv
.L323:
	leaq	48(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L324:
	leaq	560(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB11:
	call	_Unwind_Resume
.LEHE11:
.L357:
	call	__stack_chk_fail
.L333:
	movq	%rax, %rbx
	jmp	.L324
.L334:
	movq	%rax, %rbx
	jmp	.L323
	.cfi_endproc
.LFE8331:
	.section	.gcc_except_table
.LLSDA8331:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8331-.LLSDACSB8331
.LLSDACSB8331:
	.uleb128 .LEHB6-.LFB8331
	.uleb128 .LEHE6-.LEHB6
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB7-.LFB8331
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L333-.LFB8331
	.uleb128 0
	.uleb128 .LEHB8-.LFB8331
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L334-.LFB8331
	.uleb128 0
	.uleb128 .LEHB9-.LFB8331
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L335-.LFB8331
	.uleb128 0
	.uleb128 .LEHB10-.LFB8331
	.uleb128 .LEHE10-.LEHB10
	.uleb128 .L334-.LFB8331
	.uleb128 0
	.uleb128 .LEHB11-.LFB8331
	.uleb128 .LEHE11-.LEHB11
	.uleb128 0
	.uleb128 0
.LLSDACSE8331:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE19:
	.section	.text.startup
.LHOTE19:
	.section	.text.unlikely
.LCOLDB20:
	.section	.text.startup
.LHOTB20:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_cCnt, @function
_GLOBAL__sub_I_cCnt:
.LFB8996:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$cmp_set, %esi
	movl	$_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev, %edi
	movq	$0, cmp_set(%rip)
	movq	$0, cmp_set+8(%rip)
	movq	$0, cmp_set+16(%rip)
	call	__cxa_atexit
	movq	$0, trg_cmp(%rip)
	movq	$0, trg_cmp+8(%rip)
	movl	$__dso_handle, %edx
	movq	$0, trg_cmp+16(%rip)
	movl	$trg_cmp, %esi
	movl	$_ZNSt6vectorIiSaIiEED1Ev, %edi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE8996:
	.size	_GLOBAL__sub_I_cCnt, .-_GLOBAL__sub_I_cCnt
	.section	.text.unlikely
.LCOLDE20:
	.section	.text.startup
.LHOTE20:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_cCnt
	.local	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time
	.comm	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time,4,4
	.globl	trg_cmp
	.bss
	.align 16
	.type	trg_cmp, @object
	.size	trg_cmp, 24
trg_cmp:
	.zero	24
	.globl	cmp_set
	.align 16
	.type	cmp_set, @object
	.size	cmp_set, 24
cmp_set:
	.zero	24
	.globl	cmp_max_sz
	.align 4
	.type	cmp_max_sz, @object
	.size	cmp_max_sz, 4
cmp_max_sz:
	.zero	4
	.globl	N
	.align 4
	.type	N, @object
	.size	N, 4
N:
	.zero	4
	.globl	cCnt
	.align 4
	.type	cCnt, @object
	.size	cCnt, 4
cCnt:
	.zero	4
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
