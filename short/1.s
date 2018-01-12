	.file	"1.cpp"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB0:
	.text
.LHOTB0:
	.p2align 4,,15
	.globl	_Z6set_ptRSiRA3_d
	.type	_Z6set_ptRSiRA3_d, @function
_Z6set_ptRSiRA3_d:
.LFB7972:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rsi, %rbx
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	8(%rbx), %rsi
	movq	%rbp, %rdi
	call	_ZNSi10_M_extractIdEERSiRT_
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	leaq	16(%rbx), %rsi
	movq	%rbp, %rdi
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	_ZNSi10_M_extractIdEERSiRT_
	.cfi_endproc
.LFE7972:
	.size	_Z6set_ptRSiRA3_d, .-_Z6set_ptRSiRA3_d
	.section	.text.unlikely
.LCOLDE0:
	.text
.LHOTE0:
	.section	.text.unlikely
.LCOLDB2:
	.text
.LHOTB2:
	.p2align 4,,15
	.globl	_Z4distRA3_dS0_
	.type	_Z4distRA3_dS0_, @function
_Z4distRA3_dS0_:
.LFB7973:
	.cfi_startproc
	pxor	%xmm2, %xmm2
	xorl	%eax, %eax
.L4:
	movsd	(%rdi,%rax), %xmm1
	subsd	(%rsi,%rax), %xmm1
	addq	$8, %rax
	cmpq	$24, %rax
	mulsd	%xmm1, %xmm1
	addsd	%xmm1, %xmm2
	jne	.L4
	sqrtsd	%xmm2, %xmm0
	ucomisd	%xmm0, %xmm0
	jp	.L12
	ret
	.p2align 4,,10
	.p2align 3
.L12:
	movapd	%xmm2, %xmm0
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	call	sqrt
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE7973:
	.size	_Z4distRA3_dS0_, .-_Z4distRA3_dS0_
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.text.unlikely
.LCOLDB4:
	.text
.LHOTB4:
	.p2align 4,,15
	.globl	_Z9center_ptRA3_dS0_S0_
	.type	_Z9center_ptRA3_dS0_S0_, @function
_Z9center_ptRA3_dS0_S0_:
.LFB7975:
	.cfi_startproc
	movsd	.LC3(%rip), %xmm1
	xorl	%eax, %eax
.L14:
	movsd	(%rdi,%rax), %xmm0
	addsd	(%rsi,%rax), %xmm0
	mulsd	%xmm1, %xmm0
	movsd	%xmm0, (%rdx,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L14
	rep ret
	.cfi_endproc
.LFE7975:
	.size	_Z9center_ptRA3_dS0_S0_, .-_Z9center_ptRA3_dS0_S0_
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.text.unlikely
.LCOLDB5:
	.text
.LHOTB5:
	.p2align 4,,15
	.globl	_Z8reset_d2RA3_dS0_S0_S0_
	.type	_Z8reset_d2RA3_dS0_S0_S0_, @function
_Z8reset_d2RA3_dS0_S0_S0_:
.LFB7976:
	.cfi_startproc
	movsd	.LC3(%rip), %xmm1
	xorl	%eax, %eax
.L17:
	movsd	(%rdi,%rax), %xmm0
	addsd	(%rsi,%rax), %xmm0
	mulsd	%xmm1, %xmm0
	movsd	%xmm0, (%rdx,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L17
	movq	%rcx, %rsi
	movq	%rdx, %rdi
	jmp	_Z4distRA3_dS0_
	.cfi_endproc
.LFE7976:
	.size	_Z8reset_d2RA3_dS0_S0_S0_, .-_Z8reset_d2RA3_dS0_S0_S0_
	.section	.text.unlikely
.LCOLDE5:
	.text
.LHOTE5:
	.section	.text.unlikely._ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,comdat
	.align 2
.LCOLDB6:
	.section	.text._ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,comdat
.LHOTB6:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_
	.type	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_, @function
_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_:
.LFB8261:
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
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L27
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L39
.L28:
	movq	$-8, %r13
	jmp	.L20
	.p2align 4,,10
	.p2align 3
.L27:
	movl	$8, %r13d
.L20:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L26:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movsd	(%r12), %xmm0
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	addq	%rdx, %r12
	je	.L22
	movsd	%xmm0, (%r12)
.L22:
	testq	%rax, %rax
	jne	.L40
	addq	$8, %r12
	testq	%r14, %r14
	je	.L25
.L24:
	movq	%r14, %rdi
	call	_ZdlPv
.L25:
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
.L40:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$8, %r12
	call	memmove
	jmp	.L24
.L39:
	movabsq	$2305843009213693951, %rcx
	cmpq	%rcx, %rdx
	ja	.L28
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L26
	salq	$4, %rax
	movq	%rax, %r13
	jmp	.L20
	.cfi_endproc
.LFE8261:
	.size	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_, .-_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,comdat
.LCOLDE6:
	.section	.text._ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_,comdat
.LHOTE6:
	.weak	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIIdEEEvDpOT_
	.set	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIIdEEEvDpOT_,_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,comdat
	.align 2
.LCOLDB7:
	.section	.text._ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,comdat
.LHOTB7:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	.type	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_, @function
_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_:
.LFB8193:
	.cfi_startproc
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L42
	testq	%rax, %rax
	movsd	(%rsi), %xmm0
	je	.L43
	movsd	%xmm0, (%rax)
.L43:
	addq	$8, %rax
	movq	%rax, 8(%rdi)
	ret
	.p2align 4,,10
	.p2align 3
.L42:
	jmp	_ZNSt6vectorIdSaIdEE19_M_emplace_back_auxIJdEEEvDpOT_
	.cfi_endproc
.LFE8193:
	.size	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_, .-_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,comdat
.LCOLDE7:
	.section	.text._ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_,comdat
.LHOTE7:
	.weak	_ZNSt6vectorIdSaIdEE12emplace_backIIdEEEvDpOT_
	.set	_ZNSt6vectorIdSaIdEE12emplace_backIIdEEEvDpOT_,_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDB8:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTB8:
	.p2align 4,,15
	.weak	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.type	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, @function
_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_:
.LFB8310:
	.cfi_startproc
	cmpq	%rdi, %rsi
	je	.L73
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	leaq	8(%rdi), %rbx
	subq	$24, %rsp
	.cfi_def_cfa_offset 64
	cmpq	%rsi, %rbx
	je	.L49
	movq	%rsi, %r12
	movq	%rdi, %rbp
	movl	$8, %r13d
	.p2align 4,,10
	.p2align 3
.L59:
	movsd	(%rbx), %xmm1
	movsd	0(%rbp), %xmm0
	ucomisd	%xmm1, %xmm0
	ja	.L75
	movsd	-8(%rbx), %xmm0
	leaq	-8(%rbx), %rax
	ucomisd	%xmm1, %xmm0
	ja	.L67
	jmp	.L76
	.p2align 4,,10
	.p2align 3
.L61:
	movq	%rdx, %rax
.L67:
	movsd	%xmm0, 8(%rax)
	leaq	-8(%rax), %rdx
	movsd	-8(%rax), %xmm0
	ucomisd	%xmm1, %xmm0
	ja	.L61
.L56:
	movsd	%xmm1, (%rax)
.L55:
	addq	$8, %rbx
	cmpq	%rbx, %r12
	jne	.L59
.L49:
	addq	$24, %rsp
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_restore 13
	.cfi_def_cfa_offset 8
.L73:
	rep ret
	.p2align 4,,10
	.p2align 3
.L75:
	.cfi_def_cfa_offset 64
	.cfi_offset 3, -40
	.cfi_offset 6, -32
	.cfi_offset 12, -24
	.cfi_offset 13, -16
	movq	%rbx, %rdx
	subq	%rbp, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L54
	movq	%r13, %rdi
	movq	%rbp, %rsi
	movsd	%xmm1, 8(%rsp)
	subq	%rdx, %rdi
	addq	%rbx, %rdi
	call	memmove
	movsd	8(%rsp), %xmm1
.L54:
	movsd	%xmm1, 0(%rbp)
	jmp	.L55
.L76:
	movq	%rbx, %rax
	jmp	.L56
	.cfi_endproc
.LFE8310:
	.size	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, .-_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDE8:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTE8:
	.section	.text.unlikely
.LCOLDB9:
	.text
.LHOTB9:
	.p2align 4,,15
	.type	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27, @function
_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27:
.LFB8425:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsi, %rax
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	%rdi, %rax
	movq	%rsi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	cmpq	$135, %rax
	jle	.L78
	subq	$8, %rsp
	.cfi_def_cfa_offset 40
	leaq	128(%rdi), %rbx
	pushq	$0
	.cfi_def_cfa_offset 48
	movq	%rbx, %rsi
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	cmpq	%rbx, %rbp
	popq	%rcx
	.cfi_def_cfa_offset 40
	popq	%rsi
	.cfi_def_cfa_offset 32
	movq	%rbx, %rsi
	je	.L77
	.p2align 4,,10
	.p2align 3
.L89:
	movsd	(%rsi), %xmm1
	leaq	-8(%rsi), %rax
	movsd	-8(%rsi), %xmm0
	ucomisd	%xmm1, %xmm0
	ja	.L91
	jmp	.L95
	.p2align 4,,10
	.p2align 3
.L87:
	movq	%rdx, %rax
.L91:
	movsd	%xmm0, 8(%rax)
	leaq	-8(%rax), %rdx
	movsd	-8(%rax), %xmm0
	ucomisd	%xmm1, %xmm0
	ja	.L87
	addq	$8, %rsi
	movsd	%xmm1, (%rax)
	cmpq	%rsi, %rbp
	jne	.L89
.L77:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L78:
	.cfi_restore_state
	subq	$8, %rsp
	.cfi_def_cfa_offset 40
	pushq	$0
	.cfi_def_cfa_offset 48
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	popq	%rax
	.cfi_def_cfa_offset 40
	popq	%rdx
	.cfi_def_cfa_offset 32
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L95:
	.cfi_restore_state
	movq	%rsi, %rax
	addq	$8, %rsi
	cmpq	%rsi, %rbp
	movsd	%xmm1, (%rax)
	jne	.L89
	jmp	.L77
	.cfi_endproc
.LFE8425:
	.size	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27, .-_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27
	.section	.text.unlikely
.LCOLDE9:
	.text
.LHOTE9:
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDB10:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTB10:
	.p2align 4,,15
	.weak	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.type	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, @function
_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_:
.LFB8378:
	.cfi_startproc
	leaq	-1(%rdx), %rax
	movq	%rax, %r11
	shrq	$63, %r11
	addq	%rax, %r11
	sarq	%r11
	cmpq	%r11, %rsi
	jge	.L97
	movq	%rsi, %r9
	jmp	.L99
	.p2align 4,,10
	.p2align 3
.L107:
	movq	%rcx, %r9
.L99:
	leaq	1(%r9), %rax
	leaq	(%rax,%rax), %r10
	salq	$4, %rax
	addq	%rdi, %rax
	leaq	-1(%r10), %rcx
	movsd	(%rax), %xmm2
	leaq	(%rdi,%rcx,8), %r8
	movsd	(%r8), %xmm1
	ucomisd	%xmm2, %xmm1
	ja	.L98
	movapd	%xmm2, %xmm1
	movq	%rax, %r8
	movq	%r10, %rcx
.L98:
	cmpq	%r11, %rcx
	movsd	%xmm1, (%rdi,%r9,8)
	jl	.L107
	testb	$1, %dl
	jne	.L100
.L106:
	subq	$2, %rdx
	movq	%rdx, %rax
	shrq	$63, %rax
	addq	%rax, %rdx
	sarq	%rdx
	cmpq	%rcx, %rdx
	je	.L110
.L100:
	cmpq	%rsi, %rcx
	jle	.L101
	leaq	-1(%rcx), %rax
	movq	%rax, %rdx
	shrq	$63, %rdx
	addq	%rax, %rdx
	sarq	%rdx
	movsd	(%rdi,%rdx,8), %xmm1
	ucomisd	%xmm1, %xmm0
	jbe	.L101
	cmpq	%rdx, %rsi
	leaq	(%rdi,%rdx,8), %r8
	movsd	%xmm1, (%rdi,%rcx,8)
	jge	.L101
.L104:
	leaq	-1(%rdx), %rax
	movq	%rax, %rcx
	shrq	$63, %rcx
	addq	%rcx, %rax
	movq	%rdx, %rcx
	sarq	%rax
	movsd	(%rdi,%rax,8), %xmm1
	ucomisd	%xmm1, %xmm0
	jbe	.L101
	movq	%rax, %rdx
	movsd	%xmm1, (%rdi,%rcx,8)
	cmpq	%rdx, %rsi
	leaq	(%rdi,%rdx,8), %r8
	jl	.L104
.L101:
	movsd	%xmm0, (%r8)
	ret
	.p2align 4,,10
	.p2align 3
.L110:
	leaq	1(%rcx,%rcx), %rcx
	leaq	(%rdi,%rcx,8), %rax
	movsd	(%rax), %xmm1
	movsd	%xmm1, (%r8)
	movq	%rax, %r8
	jmp	.L100
.L97:
	testb	$1, %dl
	leaq	(%rdi,%rsi,8), %r8
	movq	%rsi, %rcx
	je	.L106
	jmp	.L101
	.cfi_endproc
.LFE8378:
	.size	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, .-_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDE10:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTE10:
	.section	.text.unlikely
.LCOLDB11:
	.text
.LHOTB11:
	.p2align 4,,15
	.type	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35, @function
_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35:
.LFB8433:
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
	cmpq	$135, %rax
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	jle	.L111
	testq	%rdx, %rdx
	movq	%rdi, %r12
	movq	%rdx, %r13
	je	.L113
	leaq	16(%rdi), %rbp
	movq	%rsi, %rbx
.L114:
	subq	%r12, %rbx
	movsd	8(%r12), %xmm1
	sarq	$3, %rbx
	subq	$1, %r13
	movq	%rbx, %rax
	movsd	-8(%rsi), %xmm2
	shrq	$63, %rax
	addq	%rax, %rbx
	sarq	%rbx
	leaq	(%r12,%rbx,8), %rax
	movsd	(%rax), %xmm0
	ucomisd	%xmm1, %xmm0
	jbe	.L149
	ucomisd	%xmm0, %xmm2
	ja	.L153
	ucomisd	%xmm1, %xmm2
	jbe	.L156
.L157:
	movsd	(%r12), %xmm0
	movsd	%xmm2, (%r12)
	movsd	%xmm0, -8(%rsi)
	movsd	8(%r12), %xmm2
	movsd	(%r12), %xmm1
.L123:
	movq	%rbp, %rcx
	movq	%rsi, %rdx
	.p2align 4,,10
	.p2align 3
.L126:
	ucomisd	%xmm2, %xmm1
	leaq	-8(%rcx), %rbx
	movq	%rbx, %r14
	ja	.L131
	ucomisd	%xmm1, %xmm0
	leaq	-8(%rdx), %rdi
	leaq	-16(%rdx), %rax
	jbe	.L154
	.p2align 4,,10
	.p2align 3
.L146:
	movq	%rax, %rdx
	subq	$8, %rax
	movsd	8(%rax), %xmm0
	ucomisd	%xmm1, %xmm0
	ja	.L146
	cmpq	%rdx, %rbx
	jnb	.L158
.L135:
	movsd	%xmm0, -8(%rcx)
	movsd	%xmm2, (%rdx)
	movsd	-8(%rdx), %xmm0
	movsd	(%r12), %xmm1
.L131:
	movsd	(%rcx), %xmm2
	addq	$8, %rcx
	jmp	.L126
.L154:
	movq	%rdi, %rdx
	cmpq	%rdx, %rbx
	jb	.L135
.L158:
	movq	%r13, %rdx
	movq	%rbx, %rdi
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35
	movq	%rbx, %rax
	subq	%r12, %rax
	cmpq	$135, %rax
	jle	.L111
	testq	%r13, %r13
	je	.L113
	movq	%rbx, %rsi
	jmp	.L114
.L149:
	ucomisd	%xmm1, %xmm2
	ja	.L156
	ucomisd	%xmm0, %xmm2
	ja	.L157
.L153:
	movsd	(%r12), %xmm1
	movsd	%xmm0, (%r12)
	movsd	%xmm1, (%rax)
	movsd	8(%r12), %xmm2
	movsd	(%r12), %xmm1
	movsd	-8(%rsi), %xmm0
	jmp	.L123
.L156:
	movsd	(%r12), %xmm2
	movsd	%xmm1, (%r12)
	movsd	%xmm2, 8(%r12)
	movsd	-8(%rsi), %xmm0
	jmp	.L123
.L113:
	sarq	$3, %rax
	leaq	-2(%rax), %rbp
	movq	%rax, %rbx
	sarq	%rbp
	jmp	.L116
.L159:
	subq	$1, %rbp
.L116:
	subq	$8, %rsp
	.cfi_def_cfa_offset 56
	movsd	(%r12,%rbp,8), %xmm0
	pushq	$0
	.cfi_def_cfa_offset 64
	movq	%rbp, %rsi
	movq	%rbx, %rdx
	movq	%r12, %rdi
	call	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	testq	%rbp, %rbp
	popq	%rcx
	.cfi_def_cfa_offset 56
	popq	%rsi
	.cfi_def_cfa_offset 48
	jne	.L159
	subq	$8, %r14
.L117:
	movsd	(%r12), %xmm1
	movq	%r14, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 56
	subq	%r12, %rbx
	movsd	(%r14), %xmm0
	movq	%rbx, %rdx
	movsd	%xmm1, (%r14)
	pushq	$0
	.cfi_def_cfa_offset 64
	sarq	$3, %rdx
	xorl	%esi, %esi
	movq	%r12, %rdi
	call	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEEldNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	subq	$8, %r14
	cmpq	$15, %rbx
	popq	%rax
	.cfi_def_cfa_offset 56
	popq	%rdx
	.cfi_def_cfa_offset 48
	jg	.L117
.L111:
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
.LFE8433:
	.size	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35, .-_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35
	.section	.text.unlikely
.LCOLDE11:
	.text
.LHOTE11:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC12:
	.string	"connect.inp"
.LC13:
	.string	"connect.out"
	.section	.text.unlikely
.LCOLDB14:
	.section	.text.startup,"ax",@progbits
.LHOTB14:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB7977:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA7977
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	$.LC12, %esi
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	$8, %edx
	subq	$1216, %rsp
	.cfi_def_cfa_offset 1248
	leaq	688(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1208(%rsp)
	xorl	%eax, %eax
.LEHB0:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE0:
	leaq	48(%rsp), %rsi
	leaq	688(%rsp), %rdi
.LEHB1:
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	48(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	8(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	48(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	16(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	80(%rsp), %rsi
	leaq	688(%rsp), %rdi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	80(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	8(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	80(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	16(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	144(%rsp), %rsi
	leaq	688(%rsp), %rdi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	144(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	8(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	144(%rsp), %rax
	leaq	688(%rsp), %rdi
	leaq	16(%rax), %rsi
	call	_ZNSi10_M_extractIdEERSiRT_
	leaq	688(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE5closeEv
.LEHE1:
	xorl	%eax, %eax
.L161:
	movsd	80(%rsp,%rax), %xmm0
	addsd	48(%rsp,%rax), %xmm0
	mulsd	.LC3(%rip), %xmm0
	movsd	%xmm0, 112(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L161
	leaq	144(%rsp), %rsi
	leaq	48(%rsp), %rdi
	movq	$0, 16(%rsp)
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
	call	_Z4distRA3_dS0_
	leaq	8(%rsp), %rsi
	leaq	16(%rsp), %rdi
	movsd	%xmm0, 8(%rsp)
.LEHB2:
	call	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	leaq	144(%rsp), %rsi
	leaq	80(%rsp), %rdi
	call	_Z4distRA3_dS0_
	leaq	8(%rsp), %rsi
	leaq	16(%rsp), %rdi
	movsd	%xmm0, 8(%rsp)
	call	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	leaq	144(%rsp), %rsi
	leaq	112(%rsp), %rdi
	call	_Z4distRA3_dS0_
	leaq	8(%rsp), %rsi
	leaq	16(%rsp), %rdi
	movsd	%xmm0, 8(%rsp)
	call	_ZNSt6vectorIdSaIdEE12emplace_backIJdEEEvDpOT_
	movq	24(%rsp), %rbx
	movq	16(%rsp), %rbp
	cmpq	%rbp, %rbx
	je	.L162
	movq	%rbx, %rax
	movl	$63, %edx
	movq	%rbp, %rdi
	subq	%rbp, %rax
	movq	%rbx, %rsi
	sarq	$3, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35
	movq	%rbp, %rdi
	movq	%rbx, %rsi
	call	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27
	movq	16(%rsp), %rbp
.L162:
	movl	$63, %ebx
	.p2align 4,,10
	.p2align 3
.L174:
	movq	%rbp, %rdi
.L173:
	movsd	16(%rdi), %xmm0
	subsd	(%rdi), %xmm0
	ucomisd	.LC3(%rip), %xmm0
	jbe	.L199
	leaq	144(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_Z4distRA3_dS0_
	movq	16(%rsp), %rbp
	ucomisd	16(%rbp), %xmm0
	jp	.L165
	movl	$0, %eax
	jne	.L165
.L191:
	movsd	80(%rsp,%rax), %xmm0
	addsd	112(%rsp,%rax), %xmm0
	mulsd	.LC3(%rip), %xmm0
	movsd	%xmm0, 48(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L191
	leaq	144(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_Z4distRA3_dS0_
	movsd	%xmm0, 16(%rbp)
.L168:
	movq	24(%rsp), %rbp
	movq	16(%rsp), %r12
	cmpq	%r12, %rbp
	movq	%rbp, %rdi
	je	.L173
	movq	%rbp, %rax
	movq	%rbx, %rdx
	movq	%rbp, %rsi
	subq	%r12, %rax
	movq	%r12, %rdi
	sarq	$3, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.35
	movq	%rbp, %rsi
	movq	%r12, %rdi
	call	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPdSt6vectorIdSaIdEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.27
	movq	16(%rsp), %rbp
	jmp	.L174
	.p2align 4,,10
	.p2align 3
.L165:
	leaq	144(%rsp), %rsi
	leaq	80(%rsp), %rdi
	call	_Z4distRA3_dS0_
	movq	16(%rsp), %rbp
	xorl	%eax, %eax
	ucomisd	16(%rbp), %xmm0
	jp	.L172
	jne	.L172
.L171:
	movsd	48(%rsp,%rax), %xmm0
	addsd	112(%rsp,%rax), %xmm0
	mulsd	.LC3(%rip), %xmm0
	movsd	%xmm0, 80(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L171
	leaq	144(%rsp), %rsi
	leaq	80(%rsp), %rdi
	call	_Z4distRA3_dS0_
	movsd	%xmm0, 16(%rbp)
	jmp	.L168
	.p2align 4,,10
	.p2align 3
.L172:
	movsd	48(%rsp,%rax), %xmm0
	addsd	80(%rsp,%rax), %xmm0
	mulsd	.LC3(%rip), %xmm0
	movsd	%xmm0, 112(%rsp,%rax)
	addq	$8, %rax
	cmpq	$24, %rax
	jne	.L172
	leaq	144(%rsp), %rsi
	leaq	112(%rsp), %rdi
	call	_Z4distRA3_dS0_
	movsd	%xmm0, 16(%rbp)
	jmp	.L168
	.p2align 4,,10
	.p2align 3
.L199:
	leaq	176(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC13, %esi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE2:
	movq	16(%rsp), %rax
	movsd	(%rax), %xmm0
	call	ceil
	leaq	176(%rsp), %rdi
.LEHB3:
	call	_ZNSo9_M_insertIdEERSoT_
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	leaq	176(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE5closeEv
.LEHE3:
	leaq	176(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	movq	16(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L175
	call	_ZdlPv
.L175:
	leaq	688(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1208(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L203
	addq	$1216, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L181:
	.cfi_restore_state
	movq	%rax, %rbx
.L179:
	leaq	688(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB4:
	call	_Unwind_Resume
.LEHE4:
.L203:
	call	__stack_chk_fail
.L183:
	leaq	176(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L177:
	movq	16(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L179
	call	_ZdlPv
	jmp	.L179
.L182:
	movq	%rax, %rbx
	jmp	.L177
	.cfi_endproc
.LFE7977:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA7977:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE7977-.LLSDACSB7977
.LLSDACSB7977:
	.uleb128 .LEHB0-.LFB7977
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB7977
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L181-.LFB7977
	.uleb128 0
	.uleb128 .LEHB2-.LFB7977
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L182-.LFB7977
	.uleb128 0
	.uleb128 .LEHB3-.LFB7977
	.uleb128 .LEHE3-.LEHB3
	.uleb128 .L183-.LFB7977
	.uleb128 0
	.uleb128 .LEHB4-.LFB7977
	.uleb128 .LEHE4-.LEHB4
	.uleb128 0
	.uleb128 0
.LLSDACSE7977:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE14:
	.section	.text.startup
.LHOTE14:
	.section	.text.unlikely
.LCOLDB15:
	.section	.text.startup
.LHOTB15:
	.p2align 4,,15
	.type	_GLOBAL__sub_I__Z6set_ptRSiRA3_d, @function
_GLOBAL__sub_I__Z6set_ptRSiRA3_d:
.LFB8397:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE8397:
	.size	_GLOBAL__sub_I__Z6set_ptRSiRA3_d, .-_GLOBAL__sub_I__Z6set_ptRSiRA3_d
	.section	.text.unlikely
.LCOLDE15:
	.section	.text.startup
.LHOTE15:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z6set_ptRSiRA3_d
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1071644672
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
