	.file	"1-3.cpp"
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB0:
	.text
.LHOTB0:
	.align 2
	.p2align 4,,15
	.globl	_ZN4EdgeC2Eii
	.type	_ZN4EdgeC2Eii, @function
_ZN4EdgeC2Eii:
.LFB2253:
	.cfi_startproc
	movl	%esi, (%rdi)
	movl	%edx, 4(%rdi)
	ret
	.cfi_endproc
.LFE2253:
	.size	_ZN4EdgeC2Eii, .-_ZN4EdgeC2Eii
	.section	.text.unlikely
.LCOLDE0:
	.text
.LHOTE0:
	.globl	_ZN4EdgeC1Eii
	.set	_ZN4EdgeC1Eii,_ZN4EdgeC2Eii
	.section	.text.unlikely
	.align 2
.LCOLDB1:
	.text
.LHOTB1:
	.align 2
	.p2align 4,,15
	.globl	_ZN5GraphC2Ei
	.type	_ZN5GraphC2Ei, @function
_ZN5GraphC2Ei:
.LFB2259:
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
	ja	.L3
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L3:
	call	_Znam
	xorl	%ecx, %ecx
	movq	%rbx, (%rax)
	addq	$8, %rax
	testq	%rbx, %rbx
	movq	%rax, %rdx
	je	.L5
	.p2align 4,,10
	.p2align 3
.L8:
	addq	$1, %rcx
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rbx, %rcx
	jne	.L8
.L5:
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE2259:
	.size	_ZN5GraphC2Ei, .-_ZN5GraphC2Ei
	.section	.text.unlikely
.LCOLDE1:
	.text
.LHOTE1:
	.globl	_ZN5GraphC1Ei
	.set	_ZN5GraphC1Ei,_ZN5GraphC2Ei
	.section	.text.unlikely
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7addEdgeEii
	.type	_ZN5Graph7addEdgeEii, @function
_ZN5Graph7addEdgeEii:
.LFB2261:
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
.LFE2261:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
	.align 2
.LCOLDB3:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTB3:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE:
.LFB2515:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L25
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movq	%rdi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rsi, %rbx
	.p2align 4,,10
	.p2align 3
.L21:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	16(%rbx), %rbp
	movq	%rbx, %rdi
	call	_ZdlPv
	testq	%rbp, %rbp
	movq	%rbp, %rbx
	jne	.L21
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L25:
	rep ret
	.cfi_endproc
.LFE2515:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LCOLDE3:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTE3:
	.section	.text.unlikely._ZNSt3setIiSt4lessIiESaIiEED2Ev,"axG",@progbits,_ZNSt3setIiSt4lessIiESaIiEED5Ev,comdat
	.align 2
.LCOLDB4:
	.section	.text._ZNSt3setIiSt4lessIiESaIiEED2Ev,"axG",@progbits,_ZNSt3setIiSt4lessIiESaIiEED5Ev,comdat
.LHOTB4:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt3setIiSt4lessIiESaIiEED2Ev
	.type	_ZNSt3setIiSt4lessIiESaIiEED2Ev, @function
_ZNSt3setIiSt4lessIiESaIiEED2Ev:
.LFB2264:
	.cfi_startproc
	movq	16(%rdi), %rsi
	jmp	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.cfi_endproc
.LFE2264:
	.size	_ZNSt3setIiSt4lessIiESaIiEED2Ev, .-_ZNSt3setIiSt4lessIiESaIiEED2Ev
	.section	.text.unlikely._ZNSt3setIiSt4lessIiESaIiEED2Ev,"axG",@progbits,_ZNSt3setIiSt4lessIiESaIiEED5Ev,comdat
.LCOLDE4:
	.section	.text._ZNSt3setIiSt4lessIiESaIiEED2Ev,"axG",@progbits,_ZNSt3setIiSt4lessIiESaIiEED5Ev,comdat
.LHOTE4:
	.weak	_ZNSt3setIiSt4lessIiESaIiEED1Ev
	.set	_ZNSt3setIiSt4lessIiESaIiEED1Ev,_ZNSt3setIiSt4lessIiESaIiEED2Ev
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
	.align 2
.LCOLDB5:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTB5:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_:
.LFB2520:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rsi, %r14
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdi, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	leaq	8(%rdi), %r12
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	16(%rdi), %rbx
	testq	%rbx, %rbx
	je	.L38
	movl	(%rsi), %ecx
	jmp	.L29
	.p2align 4,,10
	.p2align 3
.L44:
	movq	16(%rbx), %rax
	testq	%rax, %rax
	je	.L30
.L45:
	movq	%rax, %rbx
.L29:
	movl	32(%rbx), %edx
	cmpl	%ecx, %edx
	jg	.L44
	movq	24(%rbx), %rax
	testq	%rax, %rax
	jne	.L45
.L30:
	cmpl	%ecx, %edx
	movq	%rbx, %rax
	jg	.L28
	cmpl	%ecx, %edx
	jl	.L34
.L42:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	xorl	%edx, %edx
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
.L38:
	.cfi_restore_state
	movq	%r12, %rbx
	.p2align 4,,10
	.p2align 3
.L28:
	cmpq	%rbx, 24(%r13)
	je	.L34
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movl	(%r14), %ecx
	movl	32(%rax), %edx
	cmpl	%ecx, %edx
	jge	.L42
.L34:
	cmpq	%rbx, %r12
	je	.L40
	xorl	%r15d, %r15d
	movl	32(%rbx), %eax
	cmpl	%eax, (%r14)
	setl	%r15b
.L35:
	movl	$40, %edi
	call	_Znwm
	movq	%rax, %rbp
	movl	(%r14), %eax
	movq	%rbx, %rdx
	movq	%r12, %rcx
	movq	%rbp, %rsi
	movl	%r15d, %edi
	movl	%eax, 32(%rbp)
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 40(%r13)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%rbp, %rax
	popq	%rbx
	.cfi_def_cfa_offset 48
	movl	$1, %edx
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
.L40:
	.cfi_restore_state
	movl	$1, %r15d
	jmp	.L35
	.cfi_endproc
.LFE2520:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LCOLDE5:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTE5:
	.section	.text.unlikely._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,comdat
	.align 2
.LCOLDB6:
	.section	.text._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,comdat
.LHOTB6:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E
	.type	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E, @function
_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E:
.LFB2628:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L56
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movq	%rdi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rsi, %rbx
	.p2align 4,,10
	.p2align 3
.L52:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E
	movq	48(%rbx), %rsi
	movq	16(%rbx), %rbp
	leaq	32(%rbx), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
	movq	%rbp, %rbx
	call	_ZdlPv
	testq	%rbp, %rbp
	jne	.L52
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L56:
	rep ret
	.cfi_endproc
.LFE2628:
	.size	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E, .-_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E
	.section	.text.unlikely._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,comdat
.LCOLDE6:
	.section	.text._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E,comdat
.LHOTE6:
	.section	.text.unlikely._ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev,"axG",@progbits,_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED5Ev,comdat
	.align 2
.LCOLDB7:
	.section	.text._ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev,"axG",@progbits,_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED5Ev,comdat
.LHOTB7:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev
	.type	_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev, @function
_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev:
.LFB2920:
	.cfi_startproc
	movq	16(%rdi), %rsi
	jmp	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE8_M_eraseEPSt13_Rb_tree_nodeIS4_E
	.cfi_endproc
.LFE2920:
	.size	_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev, .-_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev
	.section	.text.unlikely._ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev,"axG",@progbits,_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED5Ev,comdat
.LCOLDE7:
	.section	.text._ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev,"axG",@progbits,_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED5Ev,comdat
.LHOTE7:
	.weak	_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED1Ev
	.set	_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED1Ev,_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED2Ev
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 2
.LCOLDB8:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTB8:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_:
.LFB2694:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2694
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdi, %r14
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rcx, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rsi, %rbx
	subq	$24, %rsp
	.cfi_def_cfa_offset 80
	movq	8(%rcx), %r15
	testq	%r15, %r15
	je	.L59
	movq	8(%r15), %rax
	testq	%rax, %rax
	movq	%rax, 8(%rcx)
	je	.L60
	cmpq	24(%rax), %r15
	je	.L114
	movq	$0, 16(%rax)
.L65:
	movl	32(%rbx), %eax
	movl	%eax, 32(%r15)
.L80:
	movl	(%rbx), %eax
	movq	$0, 24(%r15)
	cmpq	$0, 24(%rbx)
	movq	$0, 16(%r15)
	movq	%rdx, 8(%r15)
	movl	%eax, (%r15)
	je	.L66
	movq	24(%rbx), %rsi
	movq	%r12, %rcx
	movq	%r15, %rdx
	movq	%r14, %rdi
.LEHB0:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%r15)
.L66:
	movq	16(%rbx), %rbp
	movq	%r15, %r13
	testq	%rbp, %rbp
	jne	.L102
	jmp	.L95
	.p2align 4,,10
	.p2align 3
.L70:
	movq	$0, 16(%rax)
.L110:
	movl	32(%rbp), %eax
	movl	%eax, 32(%rbx)
	movl	0(%rbp), %eax
	movq	$0, 24(%rbx)
	movq	24(%rbp), %rsi
	movq	$0, 16(%rbx)
	movl	%eax, (%rbx)
	movq	%rbx, 16(%r13)
	testq	%rsi, %rsi
	movq	%r13, 8(%rbx)
	je	.L75
	movq	%r12, %rcx
	movq	%rbx, %rdx
	movq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%rbx)
.L75:
	movq	16(%rbp), %rbp
	testq	%rbp, %rbp
	je	.L95
	movq	%rbx, %r13
.L102:
	movq	8(%r12), %rbx
	testq	%rbx, %rbx
	je	.L68
	movq	8(%rbx), %rax
	testq	%rax, %rax
	movq	%rax, 8(%r12)
	je	.L69
	cmpq	24(%rax), %rbx
	jne	.L70
	movq	$0, 24(%rax)
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L110
	movq	24(%rax), %rdx
	movq	%rax, 8(%r12)
	testq	%rdx, %rdx
	jne	.L73
	jmp	.L115
	.p2align 4,,10
	.p2align 3
.L86:
	movq	%rax, %rdx
.L73:
	movq	24(%rdx), %rax
	testq	%rax, %rax
	jne	.L86
	movq	%rdx, 8(%r12)
.L72:
	movq	16(%rdx), %rax
	testq	%rax, %rax
	je	.L110
	movq	%rax, 8(%r12)
	jmp	.L110
	.p2align 4,,10
	.p2align 3
.L69:
	movq	$0, (%r12)
	jmp	.L110
	.p2align 4,,10
	.p2align 3
.L68:
	movl	$40, %edi
	call	_Znwm
.LEHE0:
	movq	%rax, %rbx
	jmp	.L110
	.p2align 4,,10
	.p2align 3
.L95:
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%r15, %rax
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
.L115:
	.cfi_restore_state
	movq	%rax, %rdx
	jmp	.L72
.L114:
	movq	$0, 24(%rax)
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L65
	movq	%rax, 8(%rcx)
	movq	24(%rax), %rcx
	testq	%rcx, %rcx
	jne	.L64
	jmp	.L116
	.p2align 4,,10
	.p2align 3
.L84:
	movq	%rax, %rcx
.L64:
	movq	24(%rcx), %rax
	testq	%rax, %rax
	jne	.L84
	movq	%rcx, 8(%r12)
.L63:
	movq	16(%rcx), %rax
	testq	%rax, %rax
	je	.L65
	movq	%rax, 8(%r12)
	jmp	.L65
.L60:
	movq	$0, (%rcx)
	jmp	.L65
.L59:
	movl	$40, %edi
	movq	%rdx, 8(%rsp)
.LEHB1:
	call	_Znwm
.LEHE1:
	movq	%rax, %r15
	movl	32(%rbx), %eax
	movq	8(%rsp), %rdx
	movl	%eax, 32(%r15)
	jmp	.L80
.L116:
	movq	%rax, %rcx
	jmp	.L63
.L87:
.L78:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	%r15, %rsi
	movq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.LEHB2:
	call	__cxa_rethrow
.LEHE2:
.L88:
	movq	%rax, %rbx
.L79:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB3:
	call	_Unwind_Resume
.LEHE3:
	.cfi_endproc
.LFE2694:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"aG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 4
.LLSDA2694:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT2694-.LLSDATTD2694
.LLSDATTD2694:
	.byte	0x1
	.uleb128 .LLSDACSE2694-.LLSDACSB2694
.LLSDACSB2694:
	.uleb128 .LEHB0-.LFB2694
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L87-.LFB2694
	.uleb128 0x1
	.uleb128 .LEHB1-.LFB2694
	.uleb128 .LEHE1-.LEHB1
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB2-.LFB2694
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L88-.LFB2694
	.uleb128 0
	.uleb128 .LEHB3-.LFB2694
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
.LLSDACSE2694:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT2694:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LCOLDE8:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTE8:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
	.align 2
.LCOLDB9:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LHOTB9:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_:
.LFB2543:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2543
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdi, %rbx
	subq	$40, %rsp
	.cfi_def_cfa_offset 64
	movq	%fs:40, %rax
	movq	%rax, 24(%rsp)
	xorl	%eax, %eax
	cmpq	%rsi, %rdi
	je	.L118
	movq	16(%rdi), %rax
	movq	32(%rdi), %rdx
	movq	%rsi, %rbp
	movq	%rdi, 16(%rsp)
	testq	%rax, %rax
	movq	%rax, (%rsp)
	movq	%rdx, 8(%rsp)
	je	.L119
	movq	16(%rdx), %rdx
	movq	$0, 8(%rax)
	testq	%rdx, %rdx
	je	.L120
	movq	%rdx, 8(%rsp)
.L120:
	leaq	8(%rbx), %rdx
	movq	$0, 16(%rbx)
	movq	$0, 40(%rbx)
	movq	%rdx, 24(%rbx)
	movq	%rdx, 32(%rbx)
	movq	16(%rbp), %rsi
	testq	%rsi, %rsi
	je	.L126
	movq	%rsp, %rcx
	movq	%rbx, %rdi
.LEHB4:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE4:
	movq	%rax, 16(%rbx)
	movq	%rax, %rcx
	jmp	.L122
	.p2align 4,,10
	.p2align 3
.L127:
	movq	%rdx, %rcx
.L122:
	movq	16(%rcx), %rdx
	testq	%rdx, %rdx
	jne	.L127
	movq	%rcx, 24(%rbx)
	jmp	.L123
	.p2align 4,,10
	.p2align 3
.L128:
	movq	%rdx, %rax
.L123:
	movq	24(%rax), %rdx
	testq	%rdx, %rdx
	jne	.L128
	movq	%rax, 32(%rbx)
	movq	40(%rbp), %rax
	movq	16(%rsp), %rdi
	movq	%rax, 40(%rbx)
	movq	(%rsp), %rax
.L121:
	movq	%rax, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.L118:
	movq	24(%rsp), %rdi
	xorq	%fs:40, %rdi
	movq	%rbx, %rax
	jne	.L136
	addq	$40, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L119:
	.cfi_restore_state
	movq	$0, 8(%rsp)
	jmp	.L120
	.p2align 4,,10
	.p2align 3
.L126:
	movq	%rbx, %rdi
	jmp	.L121
.L129:
	movq	%rax, %rbx
	jmp	.L124
.L136:
	call	__stack_chk_fail
.L124:
	movq	16(%rsp), %rdi
	movq	(%rsp), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB5:
	call	_Unwind_Resume
.LEHE5:
	.cfi_endproc
.LFE2543:
	.section	.gcc_except_table._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"aG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LLSDA2543:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2543-.LLSDACSB2543
.LLSDACSB2543:
	.uleb128 .LEHB4-.LFB2543
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L129-.LFB2543
	.uleb128 0
	.uleb128 .LEHB5-.LFB2543
	.uleb128 .LEHE5-.LEHB5
	.uleb128 0
	.uleb128 0
.LLSDACSE2543:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LCOLDE9:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LHOTE9:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 2
.LCOLDB10:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTB10:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_:
.LFB2913:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2913
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rcx, %r14
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdi, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movl	$40, %edi
	movq	%rsi, %rbx
	movq	%rdx, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
.LEHB6:
	call	_Znwm
.LEHE6:
	movq	%rax, %r15
	movl	32(%rbx), %eax
	movq	24(%rbx), %rsi
	movq	$0, 16(%r15)
	movq	$0, 24(%r15)
	movq	%rbp, 8(%r15)
	movl	%eax, 32(%r15)
	movl	(%rbx), %eax
	testq	%rsi, %rsi
	movl	%eax, (%r15)
	je	.L138
	movq	%r14, %rcx
	movq	%r15, %rdx
	movq	%r13, %rdi
.LEHB7:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%r15)
.L138:
	movq	16(%rbx), %rbp
	movq	%r15, %r12
	testq	%rbp, %rbp
	je	.L150
	.p2align 4,,10
	.p2align 3
.L154:
	movl	$40, %edi
	call	_Znwm
	movq	%rax, %rbx
	movl	32(%rbp), %eax
	movl	%eax, 32(%rbx)
	movl	0(%rbp), %eax
	movq	$0, 24(%rbx)
	movq	24(%rbp), %rsi
	movq	$0, 16(%rbx)
	movl	%eax, (%rbx)
	movq	%rbx, 16(%r12)
	testq	%rsi, %rsi
	movq	%r12, 8(%rbx)
	je	.L140
	movq	%r14, %rcx
	movq	%rbx, %rdx
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE7:
	movq	%rax, 24(%rbx)
.L140:
	movq	16(%rbp), %rbp
	movq	%rbx, %r12
	testq	%rbp, %rbp
	jne	.L154
.L150:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	movq	%r15, %rax
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
.L145:
	.cfi_restore_state
.L143:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	%r15, %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.LEHB8:
	call	__cxa_rethrow
.LEHE8:
.L146:
	movq	%rax, %rbx
.L144:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB9:
	call	_Unwind_Resume
.LEHE9:
	.cfi_endproc
.LFE2913:
	.section	.gcc_except_table._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"aG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 4
.LLSDA2913:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT2913-.LLSDATTD2913
.LLSDATTD2913:
	.byte	0x1
	.uleb128 .LLSDACSE2913-.LLSDACSB2913
.LLSDACSB2913:
	.uleb128 .LEHB6-.LFB2913
	.uleb128 .LEHE6-.LEHB6
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB7-.LFB2913
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L145-.LFB2913
	.uleb128 0x1
	.uleb128 .LEHB8-.LFB2913
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L146-.LFB2913
	.uleb128 0
	.uleb128 .LEHB9-.LFB2913
	.uleb128 .LEHE9-.LEHB9
	.uleb128 0
	.uleb128 0
.LLSDACSE2913:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT2913:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LCOLDE10:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTE10:
	.section	.text.unlikely._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
	.align 2
.LCOLDB11:
	.section	.text._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
.LHOTB11:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_
	.type	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_, @function
_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_:
.LFB2674:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2674
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdx, %r14
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
	movq	%rdi, %rbp
	movl	$1, %r12d
	subq	$40, %rsp
	.cfi_def_cfa_offset 96
	movq	%fs:40, %rax
	movq	%rax, 24(%rsp)
	xorl	%eax, %eax
	testq	%rsi, %rsi
	je	.L201
.L160:
	movl	$80, %edi
.LEHB10:
	call	_Znwm
.LEHE10:
	movq	16(%r13), %rsi
	leaq	40(%rax), %rdx
	movq	%rax, %rbx
	movl	$0, 40(%rax)
	movq	$0, 48(%rax)
	leaq	32(%rax), %rdi
	movq	$0, 72(%rax)
	movq	%rdx, 56(%rax)
	testq	%rsi, %rsi
	movq	%rdx, 64(%rax)
	je	.L166
	leaq	16(%rsp), %rcx
	movq	%rdi, 16(%rsp)
.LEHB11:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE11:
	movq	%rax, 48(%rbx)
	movq	%rax, %rcx
	jmp	.L167
	.p2align 4,,10
	.p2align 3
.L178:
	movq	%rdx, %rcx
.L167:
	movq	16(%rcx), %rdx
	testq	%rdx, %rdx
	jne	.L178
	movq	%rcx, 56(%rbx)
	jmp	.L168
	.p2align 4,,10
	.p2align 3
.L179:
	movq	%rdx, %rax
.L168:
	movq	24(%rax), %rdx
	testq	%rdx, %rdx
	jne	.L179
	movq	%rax, 64(%rbx)
	movq	40(%r13), %rax
	movq	%rax, 72(%rbx)
.L166:
	leaq	8(%rbp), %rcx
	movq	%rbx, %rsi
	movzbl	%r12b, %edi
	movq	%r14, %rdx
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 40(%rbp)
	movq	%rbx, %rax
	movq	24(%rsp), %rsi
	xorq	%fs:40, %rsi
	jne	.L202
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
.L201:
	.cfi_restore_state
	leaq	8(%rdi), %rax
	cmpq	%rax, %rdx
	je	.L160
	movq	56(%rdx), %rbx
	leaq	40(%rdx), %rax
	leaq	8(%rcx), %rsi
	movq	24(%rcx), %r15
	movq	%rsi, %rdi
	movq	%rax, 8(%rsp)
	movq	%rsi, (%rsp)
	cmpq	%rax, %rbx
	setne	%al
	cmpq	%r15, %rdi
	movl	%eax, %esi
	je	.L161
	testb	%al, %al
	je	.L161
	movl	32(%rbx), %eax
	cmpl	%eax, 32(%r15)
	jl	.L160
	.p2align 4,,10
	.p2align 3
.L196:
	jg	.L177
	movq	%r15, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rbx, %rdi
	movq	%rax, %r15
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 8(%rsp)
	movq	%rax, %rbx
	setne	%al
	cmpq	%r15, (%rsp)
	movl	%eax, %esi
	je	.L161
	testb	%al, %al
	je	.L161
	movl	32(%rbx), %eax
	cmpl	%eax, 32(%r15)
	jge	.L196
	movl	$1, %r12d
	jmp	.L160
.L177:
	xorl	%r12d, %r12d
	jmp	.L160
	.p2align 4,,10
	.p2align 3
.L161:
	cmpq	%r15, (%rsp)
	sete	%r12b
	andl	%esi, %r12d
	jmp	.L160
.L202:
	call	__stack_chk_fail
.L182:
.L169:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	%rbx, %rdi
	call	_ZdlPv
.LEHB12:
	call	__cxa_rethrow
.LEHE12:
.L181:
	movq	%rax, %rbx
.L170:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB13:
	call	_Unwind_Resume
.LEHE13:
	.cfi_endproc
.LFE2674:
	.section	.gcc_except_table._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"aG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
	.align 4
.LLSDA2674:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT2674-.LLSDATTD2674
.LLSDATTD2674:
	.byte	0x1
	.uleb128 .LLSDACSE2674-.LLSDACSB2674
.LLSDACSB2674:
	.uleb128 .LEHB10-.LFB2674
	.uleb128 .LEHE10-.LEHB10
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB11-.LFB2674
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L182-.LFB2674
	.uleb128 0x1
	.uleb128 .LEHB12-.LFB2674
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L181-.LFB2674
	.uleb128 0
	.uleb128 .LEHB13-.LFB2674
	.uleb128 .LEHE13-.LEHB13
	.uleb128 0
	.uleb128 0
.LLSDACSE2674:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT2674:
	.section	.text._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
	.size	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_, .-_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_
	.section	.text.unlikely._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
.LCOLDE11:
	.section	.text._ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,"axG",@progbits,_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_,comdat
.LHOTE11:
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
.LFB2262:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2262
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
	movq	%rcx, %r10
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$200, %rsp
	.cfi_def_cfa_offset 256
	movq	%rdx, 16(%rsp)
	movslq	%esi, %rdx
	movq	%rcx, 96(%rsp)
	movq	%fs:40, %rcx
	movq	%rcx, 184(%rsp)
	xorl	%ecx, %ecx
	leaq	0(,%rdx,4), %rcx
	movl	%esi, 12(%rsp)
	movq	%rdi, 64(%rsp)
	movq	%r9, 32(%rsp)
	addq	%rcx, %rax
	movq	%rcx, %rsi
	movq	%rcx, 48(%rsp)
	movq	%rax, 88(%rsp)
	movq	%rax, %rcx
	movq	%r10, %rax
	addq	%rsi, %rax
	movq	%rax, %rsi
	movq	%rax, 56(%rsp)
	movl	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip), %eax
	addl	$1, %eax
	movl	%eax, (%rsi)
	movl	%eax, _ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip)
	movl	%eax, (%rcx)
	leaq	(%rdx,%rdx,2), %rax
	movq	8(%rdi), %rcx
	salq	$3, %rax
	movq	%rax, 24(%rsp)
	addq	%rcx, %rax
	movq	(%rax), %r14
	cmpq	%rax, %r14
	je	.L203
	movq	%r8, %rbx
	movl	$0, 76(%rsp)
	leaq	136(%rsp), %r12
	jmp	.L236
	.p2align 4,,10
	.p2align 3
.L205:
	movq	32(%rsp), %rax
	movq	48(%rsp), %rsi
	cmpl	(%rax,%rsi), %ebp
	je	.L208
	movq	56(%rsp), %rax
	cmpl	(%rax), %edx
	jge	.L208
	movl	%edx, (%rax)
	movl	$24, %edi
.LEHB14:
	call	_Znwm
	movl	12(%rsp), %ecx
	movq	$0, (%rax)
	movq	%rbx, %rsi
	movq	$0, 8(%rax)
	movl	%ebp, 20(%rax)
	movq	%rax, %rdi
	movl	%ecx, 16(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
.L288:
	movq	64(%rsp), %rax
	movq	8(%rax), %rcx
.L208:
	movq	24(%rsp), %rax
	movq	(%r14), %r14
	addq	%rcx, %rax
	cmpq	%rax, %r14
	je	.L203
.L236:
	movslq	16(%r14), %rax
	movq	16(%rsp), %rdx
	movl	(%rdx,%rax,4), %edx
	movq	%rax, %rbp
	leaq	0(,%rax,4), %r13
	cmpl	$-1, %edx
	jne	.L205
	movq	32(%rsp), %r15
	movl	12(%rsp), %edx
	movl	$24, %edi
	addl	$1, 76(%rsp)
	movl	%edx, (%r15,%rax,4)
	call	_Znwm
	movl	12(%rsp), %edx
	movq	%rax, %rdi
	movq	%rbx, %rsi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%ebp, 20(%rax)
	movl	%edx, 16(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	movq	%r15, %r9
	movq	96(%rsp), %r15
	movq	16(%rsp), %rdx
	movq	64(%rsp), %rdi
	movq	%rbx, %r8
	movl	%ebp, %esi
	movq	%r15, %rcx
	addq	%r15, %r13
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
.LEHE14:
	movq	56(%rsp), %rcx
	movl	(%rcx), %eax
	cmpl	%eax, 0(%r13)
	cmovle	0(%r13), %eax
	movl	%eax, (%rcx)
	movq	88(%rsp), %rax
	movl	(%rax), %eax
	cmpl	$1, %eax
	je	.L292
	jle	.L288
	cmpl	0(%r13), %eax
	jg	.L288
.L207:
	movl	$0, 136(%rsp)
	movq	$0, 144(%rsp)
	movq	$0, 168(%rsp)
	movq	%r12, 152(%rsp)
	movq	%r12, 160(%rsp)
	jmp	.L211
	.p2align 4,,10
	.p2align 3
.L209:
	leaq	128(%rsp), %rdi
	addq	$16, %rsi
.LEHB15:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	128(%rsp), %rdi
	leaq	20(%rax), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %r13
	subq	$1, 16(%rbx)
	movq	%r13, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r13, %rdi
	call	_ZdlPv
.L211:
	movq	8(%rbx), %rsi
	movl	12(%rsp), %eax
	cmpl	16(%rsi), %eax
	jne	.L209
	cmpl	20(%rsi), %ebp
	jne	.L209
	leaq	128(%rsp), %rdi
	addq	$16, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	128(%rsp), %rdi
	leaq	20(%rax), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	my_list+16(%rip), %rax
	testq	%rax, %rax
	je	.L212
	movq	152(%rsp), %rcx
	movq	%rbx, 104(%rsp)
	movq	%rax, %rbx
	movq	%r14, 80(%rsp)
	cmpq	%r12, %rcx
	movq	%rcx, 40(%rsp)
	setne	74(%rsp)
	.p2align 4,,10
	.p2align 3
.L213:
	movq	56(%rbx), %r13
	leaq	40(%rbx), %rbp
	movzbl	74(%rsp), %eax
	cmpq	%r13, %rbp
	setne	%sil
	andb	%sil, %al
	movb	%al, 75(%rsp)
	je	.L246
	movq	40(%rsp), %rax
	movl	32(%r13), %ecx
	cmpl	%ecx, 32(%rax)
	jl	.L216
	jg	.L217
	movq	%r13, %r14
	movq	%rax, %r15
	jmp	.L219
	.p2align 4,,10
	.p2align 3
.L293:
	testb	%al, %al
	je	.L215
	movl	32(%r14), %eax
	cmpl	%eax, 32(%r15)
	jl	.L216
	jg	.L217
.L219:
	movq	%r15, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r14, %rdi
	movq	%rax, %r15
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %rbp
	movq	%rax, %r14
	setne	%al
	cmpq	%r12, %r15
	movl	%eax, %esi
	jne	.L293
.L215:
	cmpq	%r12, %r15
	jne	.L217
	testb	%sil, %sil
	je	.L217
	.p2align 4,,10
	.p2align 3
.L216:
	movq	16(%rbx), %rax
	movl	$1, %edx
	testq	%rax, %rax
	je	.L214
.L294:
	movq	%rax, %rbx
	jmp	.L213
	.p2align 4,,10
	.p2align 3
.L217:
	movq	24(%rbx), %rax
	xorl	%edx, %edx
	testq	%rax, %rax
	jne	.L294
.L214:
	testb	%dl, %dl
	movq	80(%rsp), %r14
	movq	%rbx, %rax
	movq	%rbx, 80(%rsp)
	movq	104(%rsp), %rbx
	je	.L247
	cmpq	%rax, my_list+24(%rip)
	je	.L224
.L244:
	movq	80(%rsp), %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movq	40(%rsp), %rdx
	movq	56(%rax), %r13
	leaq	40(%rax), %rbp
	cmpq	%r12, %rdx
	setne	74(%rsp)
	movzbl	74(%rsp), %ecx
	cmpq	%rbp, %r13
	setne	%al
	andl	%ecx, %eax
	movb	%al, 75(%rsp)
.L223:
	cmpb	$0, 75(%rsp)
	je	.L225
	movq	40(%rsp), %rax
	movl	32(%rax), %eax
	cmpl	%eax, 32(%r13)
	jl	.L226
	movq	%rdx, %r15
	jle	.L229
	jmp	.L227
	.p2align 4,,10
	.p2align 3
.L295:
	testb	%al, %al
	je	.L284
	movl	32(%r15), %eax
	cmpl	%eax, 32(%r13)
	jl	.L226
	jg	.L227
.L229:
	movq	%r13, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r15, %rdi
	movq	%rax, %r13
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%r12, %rax
	movq	%rax, %r15
	setne	%al
	cmpq	%rbp, %r13
	movl	%eax, %edx
	jne	.L295
.L284:
	movb	%dl, 74(%rsp)
.L225:
	cmpq	%r13, %rbp
	jne	.L227
	cmpb	$0, 74(%rsp)
	je	.L227
.L226:
	cmpq	$0, 80(%rsp)
	je	.L227
.L224:
	movq	80(%rsp), %rdx
	leaq	112(%rsp), %r8
	leaq	128(%rsp), %rcx
	xorl	%esi, %esi
	movl	$my_list, %edi
	movq	$my_list, 112(%rsp)
	call	_ZNSt8_Rb_treeISt3setIiSt4lessIiESaIiEES4_St9_IdentityIS4_ES1_IS4_ESaIS4_EE10_M_insert_IRKS4_NS9_11_Alloc_nodeEEESt17_Rb_tree_iteratorIS4_EPSt18_Rb_tree_node_baseSH_OT_RT0_
.L227:
	movq	8(%rbx), %rbp
	subq	$1, 16(%rbx)
	movq	%rbp, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbp, %rdi
	call	_ZdlPv
	movslq	max_size(%rip), %rdx
	movq	168(%rsp), %rax
	addl	$1, count(%rip)
	cmpq	%rdx, %rax
	ja	.L296
	je	.L297
.L233:
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	64(%rsp), %rax
	movq	(%r14), %r14
	movq	8(%rax), %rcx
	movq	24(%rsp), %rax
	addq	%rcx, %rax
	cmpq	%rax, %r14
	jne	.L236
.L203:
	movq	184(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L298
	addq	$200, %rsp
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
.L246:
	.cfi_restore_state
	movq	40(%rsp), %r15
	jmp	.L215
.L292:
	cmpl	$1, 76(%rsp)
	jne	.L207
	jmp	.L288
.L247:
	movq	40(%rsp), %rdx
	jmp	.L223
.L296:
	movl	%eax, max_size(%rip)
.L287:
	leaq	128(%rsp), %rsi
	movl	$result, %edi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
.LEHE15:
	jmp	.L233
.L297:
	movq	152(%rsp), %r13
	movq	result+24(%rip), %rbp
	movl	32(%r13), %edx
	movl	32(%rbp), %eax
	cmpl	%edx, %eax
	jne	.L234
	.p2align 4,,10
	.p2align 3
.L235:
	movq	%r13, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rbp, %rdi
	movq	%rax, %r13
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movl	32(%r13), %edx
	movq	%rax, %rbp
	movl	32(%rax), %eax
	cmpl	%eax, %edx
	je	.L235
.L234:
	cmpl	%eax, %edx
	jge	.L233
	jmp	.L287
.L212:
	cmpq	$my_list+8, my_list+24(%rip)
	movq	$my_list+8, 80(%rsp)
	je	.L224
	movq	152(%rsp), %rax
	movq	%rax, 40(%rsp)
	jmp	.L244
.L298:
	call	__stack_chk_fail
.L249:
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB16:
	call	_Unwind_Resume
.LEHE16:
	.cfi_endproc
.LFE2262:
	.section	.gcc_except_table,"a",@progbits
.LLSDA2262:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2262-.LLSDACSB2262
.LLSDACSB2262:
	.uleb128 .LEHB14-.LFB2262
	.uleb128 .LEHE14-.LEHB14
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB15-.LFB2262
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L249-.LFB2262
	.uleb128 0
	.uleb128 .LEHB16-.LFB2262
	.uleb128 .LEHE16-.LEHB16
	.uleb128 0
	.uleb128 0
.LLSDACSE2262:
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
.LFB2266:
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
	movabsq	$2287828610704211968, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movslq	(%rdi), %rdi
	cmpq	%r13, %rdi
	ja	.L300
	salq	$2, %rdi
	call	_Znam
	movslq	(%rbx), %rdi
	movq	%rax, %rbp
	cmpq	%r13, %rdi
	ja	.L300
	salq	$2, %rdi
	call	_Znam
	movslq	(%rbx), %rdi
	movq	%rax, %r12
	cmpq	%r13, %rdi
	ja	.L300
	salq	$2, %rdi
	call	_Znam
	movslq	4(%rbx), %r15
	movq	%rax, %r13
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %r15
	ja	.L302
	leaq	(%r15,%r15,2), %rax
	leaq	8(,%rax,8), %rdi
.L302:
	call	_Znam
	leaq	8(%rax), %r14
	movq	%r15, (%rax)
	xorl	%eax, %eax
	testq	%r15, %r15
	movq	%r14, %rdx
	je	.L305
	.p2align 4,,10
	.p2align 3
.L313:
	addq	$1, %rax
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rax, %r15
	jne	.L313
.L305:
	movl	(%rbx), %edx
	xorl	%eax, %eax
	testl	%edx, %edx
	jle	.L299
	.p2align 4,,10
	.p2align 3
.L311:
	movl	$-1, 0(%rbp,%rax,4)
	movl	$-1, (%r12,%rax,4)
	movl	$-1, 0(%r13,%rax,4)
	addq	$1, %rax
	cmpl	%eax, %edx
	jg	.L311
	xorl	%r15d, %r15d
	.p2align 4,,10
	.p2align 3
.L308:
	movl	%r15d, %esi
	movq	%r13, %r9
	movq	%r14, %r8
	movq	%r12, %rcx
	movq	%rbp, %rdx
	movq	%rbx, %rdi
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	addl	$1, %r15d
	cmpl	%r15d, (%rbx)
	jg	.L308
.L299:
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
.L300:
	.cfi_restore_state
	call	__cxa_throw_bad_array_new_length
	.cfi_endproc
.LFE2266:
	.size	_ZN5Graph3BCCEv, .-_ZN5Graph3BCCEv
	.section	.text.unlikely
.LCOLDE13:
	.text
.LHOTE13:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC14:
	.string	"food.inp"
.LC15:
	.string	"food.out"
.LC16:
	.string	" "
	.section	.text.unlikely
.LCOLDB17:
	.section	.text.startup,"ax",@progbits
.LHOTB17:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB2270:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2270
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	subq	$1072, %rsp
	.cfi_def_cfa_offset 1104
	leaq	544(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1064(%rsp)
	xorl	%eax, %eax
.LEHB17:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1Ev
.LEHE17:
	leaq	32(%rsp), %rdi
.LEHB18:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1Ev
.LEHE18:
	leaq	544(%rsp), %rdi
	movl	$8, %edx
	movl	$.LC14, %esi
.LEHB19:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	leaq	32(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC15, %esi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	leaq	4(%rsp), %rsi
	leaq	544(%rsp), %rdi
	call	_ZNSirsERi
	movl	4(%rsp), %eax
	leaq	16(%rsp), %rdi
	leal	1(%rax), %esi
	call	_ZN5GraphC1Ei
	movl	4(%rsp), %eax
	xorl	%r12d, %r12d
	testl	%eax, %eax
	jle	.L320
	.p2align 4,,10
	.p2align 3
.L332:
	leaq	8(%rsp), %rsi
	leaq	544(%rsp), %rdi
	call	_ZNSirsERi
	jmp	.L319
	.p2align 4,,10
	.p2align 3
.L338:
	movslq	8(%rsp), %rax
	movl	$24, %edi
	leaq	(%rax,%rax,2), %rdx
	movq	24(%rsp), %rax
	leaq	(%rax,%rdx,8), %rbx
	call	_Znwm
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%rbx, %rsi
	movl	%ebp, 16(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	addl	$1, 20(%rsp)
.L319:
	leaq	12(%rsp), %rsi
	leaq	544(%rsp), %rdi
	call	_ZNSirsERi
	movl	12(%rsp), %ebp
	testl	%ebp, %ebp
	jne	.L338
	addl	$1, %r12d
	cmpl	%r12d, 4(%rsp)
	jg	.L332
.L320:
	leaq	16(%rsp), %rdi
	call	_ZN5Graph3BCCEv
	movq	result+24(%rip), %rbx
	cmpq	$result+8, %rbx
	je	.L324
	.p2align 4,,10
	.p2align 3
.L330:
	movl	32(%rbx), %esi
	leaq	32(%rsp), %rdi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC16, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
.LEHE19:
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	$result+8, %rax
	movq	%rax, %rbx
	jne	.L330
.L324:
	leaq	32(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	544(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1064(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L339
	addq	$1072, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L328:
	.cfi_restore_state
	movq	%rax, %rbx
.L326:
	leaq	544(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB20:
	call	_Unwind_Resume
.LEHE20:
.L329:
	leaq	32(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	jmp	.L326
.L339:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2270:
	.section	.gcc_except_table
.LLSDA2270:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2270-.LLSDACSB2270
.LLSDACSB2270:
	.uleb128 .LEHB17-.LFB2270
	.uleb128 .LEHE17-.LEHB17
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB18-.LFB2270
	.uleb128 .LEHE18-.LEHB18
	.uleb128 .L328-.LFB2270
	.uleb128 0
	.uleb128 .LEHB19-.LFB2270
	.uleb128 .LEHE19-.LEHB19
	.uleb128 .L329-.LFB2270
	.uleb128 0
	.uleb128 .LEHB20-.LFB2270
	.uleb128 .LEHE20-.LEHB20
	.uleb128 0
	.uleb128 0
.LLSDACSE2270:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE17:
	.section	.text.startup
.LHOTE17:
	.section	.text.unlikely
.LCOLDB18:
	.section	.text.startup
.LHOTB18:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_count, @function
_GLOBAL__sub_I_count:
.LFB2922:
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
	movl	$my_list, %esi
	movl	$_ZNSt3setIS_IiSt4lessIiESaIiEES0_IS3_ESaIS3_EED1Ev, %edi
	movl	$0, my_list+8(%rip)
	movq	$0, my_list+16(%rip)
	movq	$0, my_list+40(%rip)
	movq	$my_list+8, my_list+24(%rip)
	movq	$my_list+8, my_list+32(%rip)
	call	__cxa_atexit
	movl	$0, result+8(%rip)
	movq	$0, result+16(%rip)
	movl	$__dso_handle, %edx
	movq	$0, result+40(%rip)
	movq	$result+8, result+24(%rip)
	movl	$result, %esi
	movq	$result+8, result+32(%rip)
	movl	$_ZNSt3setIiSt4lessIiESaIiEED1Ev, %edi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE2922:
	.size	_GLOBAL__sub_I_count, .-_GLOBAL__sub_I_count
	.section	.text.unlikely
.LCOLDE18:
	.section	.text.startup
.LHOTE18:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_count
	.local	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time
	.comm	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time,4,4
	.globl	result
	.bss
	.align 32
	.type	result, @object
	.size	result, 48
result:
	.zero	48
	.globl	max_size
	.align 4
	.type	max_size, @object
	.size	max_size, 4
max_size:
	.zero	4
	.globl	my_list
	.align 32
	.type	my_list, @object
	.size	my_list, 48
my_list:
	.zero	48
	.globl	count
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
