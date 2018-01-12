	.file	"geeks.cpp"
	.section	.text.unlikely._ZNKSt5ctypeIcE8do_widenEc,"axG",@progbits,_ZNKSt5ctypeIcE8do_widenEc,comdat
	.align 2
.LCOLDB0:
	.section	.text._ZNKSt5ctypeIcE8do_widenEc,"axG",@progbits,_ZNKSt5ctypeIcE8do_widenEc,comdat
.LHOTB0:
	.align 2
	.p2align 4,,15
	.weak	_ZNKSt5ctypeIcE8do_widenEc
	.type	_ZNKSt5ctypeIcE8do_widenEc, @function
_ZNKSt5ctypeIcE8do_widenEc:
.LFB1210:
	.cfi_startproc
	movl	%esi, %eax
	ret
	.cfi_endproc
.LFE1210:
	.size	_ZNKSt5ctypeIcE8do_widenEc, .-_ZNKSt5ctypeIcE8do_widenEc
	.section	.text.unlikely._ZNKSt5ctypeIcE8do_widenEc,"axG",@progbits,_ZNKSt5ctypeIcE8do_widenEc,comdat
.LCOLDE0:
	.section	.text._ZNKSt5ctypeIcE8do_widenEc,"axG",@progbits,_ZNKSt5ctypeIcE8do_widenEc,comdat
.LHOTE0:
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB1:
	.text
.LHOTB1:
	.align 2
	.p2align 4,,15
	.globl	_ZN4EdgeC2Eii
	.type	_ZN4EdgeC2Eii, @function
_ZN4EdgeC2Eii:
.LFB1836:
	.cfi_startproc
	movl	%esi, (%rdi)
	movl	%edx, 4(%rdi)
	ret
	.cfi_endproc
.LFE1836:
	.size	_ZN4EdgeC2Eii, .-_ZN4EdgeC2Eii
	.section	.text.unlikely
.LCOLDE1:
	.text
.LHOTE1:
	.globl	_ZN4EdgeC1Eii
	.set	_ZN4EdgeC1Eii,_ZN4EdgeC2Eii
	.section	.text.unlikely
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.globl	_ZN5GraphC2Ei
	.type	_ZN5GraphC2Ei, @function
_ZN5GraphC2Ei:
.LFB1842:
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
	ja	.L4
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L4:
	call	_Znam
	xorl	%ecx, %ecx
	movq	%rbx, (%rax)
	addq	$8, %rax
	testq	%rbx, %rbx
	movq	%rax, %rdx
	je	.L6
	.p2align 4,,10
	.p2align 3
.L9:
	addq	$1, %rcx
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rbx, %rcx
	jne	.L9
.L6:
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1842:
	.size	_ZN5GraphC2Ei, .-_ZN5GraphC2Ei
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.globl	_ZN5GraphC1Ei
	.set	_ZN5GraphC1Ei,_ZN5GraphC2Ei
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7addEdgeEii
	.type	_ZN5Graph7addEdgeEii, @function
_ZN5Graph7addEdgeEii:
.LFB1844:
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
.LFE1844:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC4:
	.string	"--"
.LC5:
	.string	" "
	.section	.text.unlikely
	.align 2
.LCOLDB6:
	.text
.LHOTB6:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.type	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, @function
_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_:
.LFB1845:
	.cfi_startproc
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
	movq	%rcx, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$88, %rsp
	.cfi_def_cfa_offset 144
	movq	%rdx, 8(%rsp)
	movslq	%esi, %rdx
	movl	%esi, 48(%rsp)
	leaq	0(,%rdx,4), %rsi
	movq	%rcx, 64(%rsp)
	movq	%rdi, 40(%rsp)
	movq	%r9, 24(%rsp)
	movl	$0, 52(%rsp)
	addq	%rsi, %rax
	addq	%rsi, %r13
	movq	%rsi, 32(%rsp)
	movq	%rax, %rcx
	movq	%rax, 56(%rsp)
	movl	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip), %eax
	addl	$1, %eax
	movl	%eax, 0(%r13)
	movl	%eax, _ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip)
	movl	%eax, (%rcx)
	leaq	(%rdx,%rdx,2), %rax
	movq	8(%rdi), %rcx
	salq	$3, %rax
	movq	%rax, 16(%rsp)
	addq	%rcx, %rax
	movq	(%rax), %r15
	cmpq	%rax, %r15
	je	.L16
	movq	%r8, %rbx
	jmp	.L34
	.p2align 4,,10
	.p2align 3
.L18:
	movq	24(%rsp), %rax
	movq	32(%rsp), %rdi
	cmpl	(%rax,%rdi), %r14d
	je	.L21
	cmpl	0(%r13), %edx
	jge	.L21
	movl	%edx, 0(%r13)
	movl	$24, %edi
	call	_Znwm
	movl	48(%rsp), %ecx
	movq	$0, (%rax)
	movq	%rbx, %rsi
	movq	$0, 8(%rax)
	movl	%r14d, 20(%rax)
	movq	%rax, %rdi
	movl	%ecx, 16(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
.L45:
	movq	40(%rsp), %rax
	movq	8(%rax), %rcx
.L21:
	movq	16(%rsp), %rax
	movq	(%r15), %r15
	addq	%rcx, %rax
	cmpq	%rax, %r15
	je	.L16
.L34:
	movslq	16(%r15), %rax
	movq	8(%rsp), %rdx
	movl	(%rdx,%rax,4), %edx
	movq	%rax, %r14
	leaq	0(,%rax,4), %rbp
	cmpl	$-1, %edx
	jne	.L18
	movq	24(%rsp), %r12
	movl	48(%rsp), %esi
	movl	$24, %edi
	addl	$1, 52(%rsp)
	movl	%esi, (%r12,%rax,4)
	call	_Znwm
	movl	48(%rsp), %esi
	movq	%rax, %rdi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r14d, 20(%rax)
	movl	%esi, 16(%rax)
	movq	%rbx, %rsi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	movq	%r12, %r9
	movq	64(%rsp), %r12
	movq	8(%rsp), %rdx
	movq	40(%rsp), %rdi
	movq	%rbx, %r8
	movl	%r14d, %esi
	addq	%r12, %rbp
	movq	%r12, %rcx
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	movl	0(%r13), %eax
	cmpl	%eax, 0(%rbp)
	cmovle	0(%rbp), %eax
	movl	%eax, 0(%r13)
	movq	56(%rsp), %rax
	movl	(%rax), %eax
	cmpl	$1, %eax
	je	.L48
	jle	.L45
	cmpl	0(%rbp), %eax
	jg	.L45
.L42:
	movq	%r13, 72(%rsp)
	movl	48(%rsp), %ebp
	jmp	.L36
	.p2align 4,,10
	.p2align 3
.L23:
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$2, %edx
	movq	%rax, %r13
	movl	$.LC4, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%r12d, %esi
	movq	%r13, %rdi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC5, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	8(%rbx), %r12
	subq	$1, 16(%rbx)
	movq	%r12, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r12, %rdi
	call	_ZdlPv
.L36:
	movq	8(%rbx), %rax
	movl	16(%rax), %esi
	movl	20(%rax), %r12d
	cmpl	%esi, %ebp
	jne	.L23
	cmpl	%r12d, %r14d
	jne	.L23
	movl	48(%rsp), %esi
	movl	$_ZSt4cout, %edi
	movq	72(%rsp), %r13
	call	_ZNSolsEi
	movl	$2, %edx
	movq	%rax, %rbp
	movl	$.LC4, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%r14d, %esi
	movq	%rbp, %rdi
	call	_ZNSolsEi
	movq	8(%rbx), %rbp
	subq	$1, 16(%rbx)
	movq	%rbp, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbp, %rdi
	call	_ZdlPv
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbp
	testq	%rbp, %rbp
	je	.L49
	cmpb	$0, 56(%rbp)
	je	.L25
	movsbl	67(%rbp), %esi
.L26:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	movq	40(%rsp), %rax
	movq	(%r15), %r15
	addl	$1, count(%rip)
	movq	8(%rax), %rcx
	movq	16(%rsp), %rax
	addq	%rcx, %rax
	cmpq	%rax, %r15
	jne	.L34
.L16:
	addq	$88, %rsp
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
.L48:
	.cfi_restore_state
	cmpl	$1, 52(%rsp)
	jne	.L42
	jmp	.L45
	.p2align 4,,10
	.p2align 3
.L25:
	movq	%rbp, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L26
	movq	%rbp, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L26
.L49:
	call	_ZSt16__throw_bad_castv
	.cfi_endproc
.LFE1845:
	.size	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, .-_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely
	.align 2
.LCOLDB7:
	.text
.LHOTB7:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph3BCCEv
	.type	_ZN5Graph3BCCEv, @function
_ZN5Graph3BCCEv:
.LFB1846:
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
	movabsq	$2287828610704211968, %rbx
	subq	$40, %rsp
	.cfi_def_cfa_offset 96
	movslq	(%rdi), %rax
	cmpq	%rbx, %rax
	ja	.L51
	movq	%rdi, %r13
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movq	%rax, %r12
	movslq	0(%r13), %rax
	cmpq	%rbx, %rax
	ja	.L51
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movq	%rax, 8(%rsp)
	movslq	0(%r13), %rax
	cmpq	%rbx, %rax
	ja	.L51
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movslq	4(%r13), %rbx
	movq	%rax, 16(%rsp)
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %rbx
	ja	.L53
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L53:
	call	_Znam
	movq	%rbx, (%rax)
	movq	%rax, %r14
	leaq	8(%rax), %rax
	xorl	%edx, %edx
	testq	%rbx, %rbx
	movq	%rax, 24(%rsp)
	je	.L56
	.p2align 4,,10
	.p2align 3
.L75:
	addq	$1, %rdx
	movq	$0, 16(%rax)
	movq	%rax, (%rax)
	movq	%rax, 8(%rax)
	addq	$24, %rax
	cmpq	%rdx, %rbx
	jne	.L75
.L56:
	movl	0(%r13), %edx
	xorl	%eax, %eax
	testl	%edx, %edx
	jle	.L50
	.p2align 4,,10
	.p2align 3
.L72:
	movq	8(%rsp), %rcx
	movl	$-1, (%r12,%rax,4)
	movl	$-1, (%rcx,%rax,4)
	movq	16(%rsp), %rcx
	movl	$-1, (%rcx,%rax,4)
	addq	$1, %rax
	cmpl	%eax, %edx
	jg	.L72
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L65:
	cmpl	$-1, (%r12,%rbp,4)
	je	.L82
.L58:
	cmpq	$0, 24(%r14)
	je	.L59
	.p2align 4,,10
	.p2align 3
.L71:
	movq	16(%r14), %rax
	movl	$_ZSt4cout, %edi
	movl	16(%rax), %esi
	movl	20(%rax), %ebx
	call	_ZNSolsEi
	movl	$2, %edx
	movq	%rax, %r15
	movl	$.LC4, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%ebx, %esi
	movq	%r15, %rdi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC5, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	16(%r14), %rbx
	subq	$1, 24(%r14)
	movq	%rbx, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbx, %rdi
	call	_ZdlPv
	cmpq	$0, 24(%r14)
	jne	.L71
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbx
	testq	%rbx, %rbx
	je	.L83
	cmpb	$0, 56(%rbx)
	je	.L62
	movsbl	67(%rbx), %esi
.L63:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	addl	$1, count(%rip)
.L59:
	leal	1(%rbp), %eax
	addq	$1, %rbp
	cmpl	0(%r13), %eax
	jl	.L65
.L50:
	addq	$40, %rsp
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
.L82:
	.cfi_restore_state
	movq	16(%rsp), %r9
	movq	24(%rsp), %r8
	movq	%r12, %rdx
	movq	8(%rsp), %rcx
	movl	%ebp, %esi
	movq	%r13, %rdi
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	jmp	.L58
.L62:
	movq	%rbx, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%rbx), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L63
	movq	%rbx, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L63
.L51:
	call	__cxa_throw_bad_array_new_length
.L83:
	call	_ZSt16__throw_bad_castv
	.cfi_endproc
.LFE1846:
	.size	_ZN5Graph3BCCEv, .-_ZN5Graph3BCCEv
	.section	.text.unlikely
.LCOLDE7:
	.text
.LHOTE7:
	.section	.text.unlikely._ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,"axG",@progbits,_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,comdat
	.align 2
.LCOLDB8:
	.section	.text._ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,"axG",@progbits,_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,comdat
.LHOTB8:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	.type	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_, @function
_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_:
.LFB2004:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rdx, %r12
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdi, %rbx
	movl	$24, %edi
	movq	%rsi, %rbp
	call	_Znwm
	movl	(%r12), %edx
	movq	%rbp, %rsi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%rax, %rdi
	movl	%edx, 16(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE2004:
	.size	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_, .-_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	.section	.text.unlikely._ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,"axG",@progbits,_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,comdat
.LCOLDE8:
	.section	.text._ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,"axG",@progbits,_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_,comdat
.LHOTE8:
	.weak	_ZNSt7__cxx114listIiSaIiEE9_M_insertIIRKiEEEvSt14_List_iteratorIiEDpOT_
	.set	_ZNSt7__cxx114listIiSaIiEE9_M_insertIIRKiEEEvSt14_List_iteratorIiEDpOT_,_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	.section	.rodata.str1.1
.LC9:
	.string	"Above are "
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC10:
	.string	" biconnected components in graph"
	.section	.text.unlikely
.LCOLDB11:
	.section	.text.startup,"ax",@progbits
.LHOTB11:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1850:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$12, %esi
	subq	$144, %rsp
	.cfi_def_cfa_offset 160
	leaq	112(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	call	_ZN5GraphC1Ei
	movq	120(%rsp), %rdi
	movq	%rsp, %rdx
	movl	$1, (%rsp)
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	4(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$0, 4(%rsp)
	leaq	24(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	8(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$2, 8(%rsp)
	leaq	24(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	12(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$1, 12(%rsp)
	leaq	48(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	16(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$3, 16(%rsp)
	leaq	24(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	20(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$1, 20(%rsp)
	leaq	72(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	24(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$3, 24(%rsp)
	leaq	48(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	28(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$2, 28(%rsp)
	leaq	72(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	32(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$4, 32(%rsp)
	leaq	48(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	36(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$2, 36(%rsp)
	leaq	96(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	40(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$4, 40(%rsp)
	leaq	72(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	44(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$3, 44(%rsp)
	leaq	96(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	48(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$5, 48(%rsp)
	leaq	24(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	52(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$1, 52(%rsp)
	leaq	120(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rdi
	leaq	56(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$6, 56(%rsp)
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	60(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$0, 60(%rsp)
	leaq	144(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	64(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$6, 64(%rsp)
	leaq	120(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	68(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$5, 68(%rsp)
	leaq	144(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	72(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$7, 72(%rsp)
	leaq	120(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	76(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$5, 76(%rsp)
	leaq	168(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	80(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$8, 80(%rsp)
	leaq	120(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	84(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$5, 84(%rsp)
	leaq	192(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	88(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$8, 88(%rsp)
	leaq	168(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	92(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$7, 92(%rsp)
	leaq	192(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	96(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$9, 96(%rsp)
	leaq	192(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	100(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$8, 100(%rsp)
	leaq	216(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	104(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$11, 104(%rsp)
	leaq	240(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	movq	120(%rsp), %rax
	leaq	108(%rsp), %rdx
	addl	$1, 116(%rsp)
	movl	$10, 108(%rsp)
	leaq	264(%rax), %rdi
	movq	%rdi, %rsi
	call	_ZNSt7__cxx114listIiSaIiEE9_M_insertIJRKiEEEvSt14_List_iteratorIiEDpOT_
	leaq	112(%rsp), %rdi
	addl	$1, 116(%rsp)
	call	_ZN5Graph3BCCEv
	movl	count(%rip), %ebx
	movl	$10, %edx
	movl	$.LC9, %esi
	movl	$_ZSt4cout, %edi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%ebx, %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$.LC10, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	136(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L89
	addq	$144, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L89:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE1850:
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE11:
	.section	.text.startup
.LHOTE11:
	.section	.text.unlikely
.LCOLDB12:
	.section	.text.startup
.LHOTB12:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_count, @function
_GLOBAL__sub_I_count:
.LFB2160:
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
.LFE2160:
	.size	_GLOBAL__sub_I_count, .-_GLOBAL__sub_I_count
	.section	.text.unlikely
.LCOLDE12:
	.section	.text.startup
.LHOTE12:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_count
	.local	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time
	.comm	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time,4,4
	.globl	count
	.bss
	.align 4
	.type	count, @object
	.size	count, 4
count:
	.zero	4
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
