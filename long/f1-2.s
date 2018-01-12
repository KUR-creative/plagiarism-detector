	.file	"1-2.cpp"
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
.LFB2158:
	.cfi_startproc
	movl	%esi, (%rdi)
	movl	%edx, 4(%rdi)
	ret
	.cfi_endproc
.LFE2158:
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
.LFB2164:
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
.LFE2164:
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
.LFB2166:
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
.LFE2166:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.text.unlikely
.LCOLDB3:
	.text
.LHOTB3:
	.p2align 4,,15
	.globl	_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE
	.type	_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE, @function
_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE:
.LFB8667:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	leaq	8(%rsi), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	24(%rsi), %rbx
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	cmpq	%rbp, %rbx
	je	.L15
	movq	%rdi, %r12
	.p2align 4,,10
	.p2align 3
.L20:
	movl	32(%rbx), %esi
	movq	%r12, %rdi
	call	_ZNSolsEi
	leaq	7(%rsp), %rsi
	movl	$1, %edx
	movq	%rax, %rdi
	movb	$32, 7(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %rbp
	movq	%rax, %rbx
	jne	.L20
.L15:
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L23
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
.L23:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE8667:
	.size	_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE, .-_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
	.align 2
.LCOLDB4:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTB4:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_:
.LFB8933:
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
	je	.L35
	movl	(%rsi), %ecx
	jmp	.L26
	.p2align 4,,10
	.p2align 3
.L41:
	movq	16(%rbx), %rax
	testq	%rax, %rax
	je	.L27
.L42:
	movq	%rax, %rbx
.L26:
	movl	32(%rbx), %edx
	cmpl	%ecx, %edx
	jg	.L41
	movq	24(%rbx), %rax
	testq	%rax, %rax
	jne	.L42
.L27:
	cmpl	%ecx, %edx
	movq	%rbx, %rax
	jg	.L25
	cmpl	%ecx, %edx
	jl	.L31
.L39:
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
.L35:
	.cfi_restore_state
	movq	%r12, %rbx
	.p2align 4,,10
	.p2align 3
.L25:
	cmpq	%rbx, 24(%r13)
	je	.L31
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movl	(%r14), %ecx
	movl	32(%rax), %edx
	cmpl	%ecx, %edx
	jge	.L39
.L31:
	cmpq	%rbx, %r12
	je	.L37
	xorl	%r15d, %r15d
	movl	32(%rbx), %eax
	cmpl	%eax, (%r14)
	setl	%r15b
.L32:
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
.L37:
	.cfi_restore_state
	movl	$1, %r15d
	jmp	.L32
	.cfi_endproc
.LFE8933:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LCOLDE4:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTE4:
	.section	.text.unlikely
	.align 2
.LCOLDB5:
	.text
.LHOTB5:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.type	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, @function
_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE:
.LFB2167:
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
	movl	%esi, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rcx, %r13
	subq	$88, %rsp
	.cfi_def_cfa_offset 144
	movq	%rdx, 8(%rsp)
	movslq	%esi, %rdx
	movq	%rcx, 72(%rsp)
	leaq	0(,%rdx,4), %rsi
	movq	%rdi, 40(%rsp)
	movq	%r9, 24(%rsp)
	movl	$0, 52(%rsp)
	addq	%rsi, %rax
	addq	%rsi, %r13
	movq	%rsi, 32(%rsp)
	movq	%rax, %rcx
	movq	%rax, 64(%rsp)
	movl	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EEE4time(%rip), %eax
	addl	$1, %eax
	movl	%eax, 0(%r13)
	movl	%eax, _ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EEE4time(%rip)
	movl	%eax, (%rcx)
	leaq	(%rdx,%rdx,2), %rax
	movq	8(%rdi), %rcx
	salq	$3, %rax
	movq	%rax, 16(%rsp)
	addq	%rcx, %rax
	movq	(%rax), %rbp
	cmpq	%rax, %rbp
	je	.L43
	movq	%r8, %rbx
	jmp	.L55
	.p2align 4,,10
	.p2align 3
.L45:
	movq	24(%rsp), %rax
	movq	32(%rsp), %rsi
	cmpl	(%rax,%rsi), %r15d
	je	.L48
	cmpl	0(%r13), %edx
	jge	.L48
	movl	%edx, 0(%r13)
	movl	$24, %edi
	call	_Znwm
	movq	%rbx, %rsi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r12d, 16(%rax)
	movl	%r15d, 20(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
.L63:
	movq	40(%rsp), %rax
	movq	8(%rax), %rcx
.L48:
	movq	16(%rsp), %rax
	movq	0(%rbp), %rbp
	addq	%rcx, %rax
	cmpq	%rax, %rbp
	je	.L43
.L55:
	movslq	16(%rbp), %rax
	movq	8(%rsp), %rdx
	movl	(%rdx,%rax,4), %edx
	movq	%rax, %r15
	leaq	0(,%rax,4), %r11
	cmpl	$-1, %edx
	jne	.L45
	movq	24(%rsp), %r14
	movl	$24, %edi
	movq	%r11, 56(%rsp)
	addl	$1, 52(%rsp)
	movl	%r12d, (%r14,%rax,4)
	call	_Znwm
	movq	%rbx, %rsi
	movq	%rax, %rdi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r12d, 16(%rax)
	movl	%r15d, 20(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	subq	$8, %rsp
	.cfi_def_cfa_offset 152
	addq	$1, 16(%rbx)
	movq	%r14, %r9
	pushq	152(%rsp)
	.cfi_def_cfa_offset 160
	movq	88(%rsp), %r14
	movq	%rbx, %r8
	movq	24(%rsp), %rdx
	movq	56(%rsp), %rdi
	movl	%r15d, %esi
	movq	%r14, %rcx
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	movq	72(%rsp), %r11
	movl	0(%r13), %eax
	popq	%rdx
	.cfi_def_cfa_offset 152
	popq	%rcx
	.cfi_def_cfa_offset 144
	addq	%r14, %r11
	cmpl	%eax, (%r11)
	cmovle	(%r11), %eax
	movl	%eax, 0(%r13)
	movq	64(%rsp), %rax
	movl	(%rax), %eax
	cmpl	$1, %eax
	je	.L64
	jle	.L63
	cmpl	(%r11), %eax
	jg	.L63
.L61:
	movq	%rbp, 56(%rsp)
	movq	144(%rsp), %r14
	jmp	.L57
	.p2align 4,,10
	.p2align 3
.L49:
	movslq	_ZL9bcc_label(%rip), %rax
	addq	$16, %rsi
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	20(%rax), %rsi
	movslq	_ZL9bcc_label(%rip), %rax
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rbp
	subq	$1, 16(%rbx)
	movq	%rbp, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbp, %rdi
	call	_ZdlPv
.L57:
	movq	8(%rbx), %rsi
	cmpl	16(%rsi), %r12d
	jne	.L49
	cmpl	20(%rsi), %r15d
	jne	.L49
	movslq	_ZL9bcc_label(%rip), %rax
	addq	$16, %rsi
	movq	56(%rsp), %rbp
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	144(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	20(%rax), %rsi
	movslq	_ZL9bcc_label(%rip), %rax
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	144(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	subq	$1, 16(%rbx)
	movq	%rax, %rdi
	movq	%rax, 56(%rsp)
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	56(%rsp), %rax
	movq	%rax, %rdi
	call	_ZdlPv
	movq	40(%rsp), %rax
	addl	$1, count(%rip)
	addl	$1, _ZL9bcc_label(%rip)
	movq	8(%rax), %rcx
	jmp	.L48
	.p2align 4,,10
	.p2align 3
.L43:
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
.L64:
	.cfi_restore_state
	cmpl	$1, 52(%rsp)
	jne	.L61
	jmp	.L63
	.cfi_endproc
.LFE2167:
	.size	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, .-_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.section	.text.unlikely
.LCOLDE5:
	.text
.LHOTE5:
	.section	.text.unlikely
	.align 2
.LCOLDB6:
	.text
.LHOTB6:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.type	_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, @function
_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE:
.LFB2168:
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
	movabsq	$2287828610704211968, %rbp
	subq	$40, %rsp
	.cfi_def_cfa_offset 96
	movslq	(%rdi), %rax
	cmpq	%rbp, %rax
	ja	.L66
	movq	%rdi, %r13
	leaq	0(,%rax,4), %rdi
	movq	%rsi, %rbx
	call	_Znam
	movq	%rax, %r12
	movslq	0(%r13), %rax
	cmpq	%rbp, %rax
	ja	.L66
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movq	%rax, 8(%rsp)
	movslq	0(%r13), %rax
	cmpq	%rbp, %rax
	ja	.L66
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movslq	4(%r13), %rbp
	movq	%rax, 16(%rsp)
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %rbp
	ja	.L68
	leaq	0(%rbp,%rbp,2), %rax
	leaq	8(,%rax,8), %rdi
.L68:
	call	_Znam
	movq	%rbp, (%rax)
	movq	%rax, %r14
	leaq	8(%rax), %rax
	xorl	%edx, %edx
	testq	%rbp, %rbp
	movq	%rax, 24(%rsp)
	je	.L71
	.p2align 4,,10
	.p2align 3
.L85:
	addq	$1, %rdx
	movq	$0, 16(%rax)
	movq	%rax, (%rax)
	movq	%rax, 8(%rax)
	addq	$24, %rax
	cmpq	%rdx, %rbp
	jne	.L85
.L71:
	movl	0(%r13), %edx
	xorl	%eax, %eax
	testl	%edx, %edx
	jle	.L65
	.p2align 4,,10
	.p2align 3
.L82:
	movq	8(%rsp), %rcx
	movl	$-1, (%r12,%rax,4)
	movl	$-1, (%rcx,%rax,4)
	movq	16(%rsp), %rcx
	movl	$-1, (%rcx,%rax,4)
	addq	$1, %rax
	cmpl	%eax, %edx
	jg	.L82
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L78:
	cmpl	$-1, (%r12,%rbp,4)
	je	.L89
.L73:
	cmpq	$0, 24(%r14)
	je	.L74
	.p2align 4,,10
	.p2align 3
.L81:
	movq	16(%r14), %rax
	leaq	16(%rax), %rsi
	movslq	_ZL9bcc_label(%rip), %rax
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	%rbx, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	16(%r14), %rax
	leaq	20(%rax), %rsi
	movslq	_ZL9bcc_label(%rip), %rax
	leaq	(%rax,%rax,2), %rdi
	salq	$4, %rdi
	addq	%rbx, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIRKiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	16(%r14), %r15
	subq	$1, 24(%r14)
	movq	%r15, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r15, %rdi
	call	_ZdlPv
	cmpq	$0, 24(%r14)
	jne	.L81
	addl	$1, count(%rip)
.L74:
	leal	1(%rbp), %eax
	addq	$1, %rbp
	cmpl	%eax, 0(%r13)
	jg	.L78
.L65:
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
.L89:
	.cfi_restore_state
	subq	$8, %rsp
	.cfi_def_cfa_offset 104
	movq	%r12, %rdx
	movl	%ebp, %esi
	pushq	%rbx
	.cfi_def_cfa_offset 112
	movq	32(%rsp), %r9
	movq	%r13, %rdi
	movq	40(%rsp), %r8
	movq	24(%rsp), %rcx
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	popq	%rax
	.cfi_def_cfa_offset 104
	popq	%rdx
	.cfi_def_cfa_offset 96
	jmp	.L73
.L66:
	call	__cxa_throw_bad_array_new_length
	.cfi_endproc
.LFE2168:
	.size	_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, .-_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
	.align 2
.LCOLDB7:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTB7:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE:
.LFB8979:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L100
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
.L96:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	16(%rbx), %rbp
	movq	%rbx, %rdi
	call	_ZdlPv
	testq	%rbp, %rbp
	movq	%rbp, %rbx
	jne	.L96
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L100:
	rep ret
	.cfi_endproc
.LFE8979:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LCOLDE7:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTE7:
	.section	.text.unlikely
.LCOLDB8:
	.text
.LHOTB8:
	.p2align 4,,15
	.globl	_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE
	.type	_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE, @function
_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE:
.LFB8668:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8668
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdi, %rax
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	leaq	2408(%rdi), %rdx
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rsi, %r13
	addq	$8, %rax
	subq	$72, %rsp
	.cfi_def_cfa_offset 128
	movq	%fs:40, %rcx
	movq	%rcx, 56(%rsp)
	xorl	%ecx, %ecx
	movq	%rdi, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L102:
	movl	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 32(%rax)
	movq	%rax, 16(%rax)
	movq	%rax, 24(%rax)
	addq	$48, %rax
	cmpq	%rax, %rdx
	jne	.L102
	leaq	32(%rsp), %rdi
	movl	$100, %esi
	movl	$0, _ZL9bcc_label(%rip)
.LEHB0:
	call	_ZN5GraphC1Ei
	leaq	1200(%r13), %rax
	movq	%rax, 16(%rsp)
	.p2align 4,,10
	.p2align 3
.L107:
	movq	8(%r13), %rdx
	subq	0(%r13), %rdx
	sarq	$2, %rdx
	testl	%edx, %edx
	je	.L106
	movq	0(%r13), %rax
	cmpl	$2, %edx
	movl	(%rax), %r15d
	jle	.L108
	movslq	%r15d, %rcx
	subl	$3, %edx
	movl	$4, %ebp
	leaq	(%rcx,%rcx,2), %r14
	leaq	8(,%rdx,4), %rcx
	salq	$3, %r14
	movq	%rcx, 8(%rsp)
	jmp	.L109
	.p2align 4,,10
	.p2align 3
.L120:
	movq	0(%r13), %rax
.L109:
	movl	$24, %edi
	movq	%r14, %r12
	movslq	(%rax,%rbp), %rbx
	addq	40(%rsp), %r12
	call	_Znwm
	movl	%ebx, 16(%rax)
	movq	%rax, %rdi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%r12, %rsi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%r12)
	movq	40(%rsp), %rax
	leaq	(%rbx,%rbx,2), %rdx
	movl	$24, %edi
	addl	$1, 36(%rsp)
	leaq	(%rax,%rdx,8), %rbx
	call	_Znwm
	movq	$0, (%rax)
	movq	%rbx, %rsi
	movq	%rax, %rdi
	movq	$0, 8(%rax)
	movl	%r15d, 16(%rax)
	addq	$4, %rbp
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
	addl	$1, 36(%rsp)
	cmpq	%rbp, 8(%rsp)
	jne	.L120
.L108:
	addq	$24, %r13
	cmpq	16(%rsp), %r13
	jne	.L107
.L106:
	movq	24(%rsp), %rsi
	leaq	32(%rsp), %rdi
	call	_ZN5Graph3BCCERSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
.LEHE0:
	movq	56(%rsp), %rcx
	xorq	%fs:40, %rcx
	movq	24(%rsp), %rax
	jne	.L121
	addq	$72, %rsp
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
.L114:
	.cfi_restore_state
	movq	%rax, %rbp
	movq	24(%rsp), %rax
	leaq	2400(%rax), %rbx
.L112:
	subq	$48, %rbx
	movq	16(%rbx), %rsi
	movq	%rbx, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	cmpq	%rbx, 24(%rsp)
	jne	.L112
	movq	%rbp, %rdi
.LEHB1:
	call	_Unwind_Resume
.LEHE1:
.L121:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8668:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA8668:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8668-.LLSDACSB8668
.LLSDACSB8668:
	.uleb128 .LEHB0-.LFB8668
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L114-.LFB8668
	.uleb128 0
	.uleb128 .LEHB1-.LFB8668
	.uleb128 .LEHE1-.LEHB1
	.uleb128 0
	.uleb128 0
.LLSDACSE8668:
	.text
	.size	_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE, .-_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE
	.section	.text.unlikely
.LCOLDE8:
	.text
.LHOTE8:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
	.align 2
.LCOLDB9:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTB9:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_:
.LFB8993:
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
	je	.L130
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L142
.L131:
	movq	$-4, %r13
	jmp	.L123
	.p2align 4,,10
	.p2align 3
.L130:
	movl	$4, %r13d
.L123:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L129:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movl	(%r12), %ecx
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	addq	%rdx, %r12
	je	.L125
	movl	%ecx, (%r12)
.L125:
	testq	%rax, %rax
	jne	.L143
	addq	$4, %r12
	testq	%r14, %r14
	je	.L128
.L127:
	movq	%r14, %rdi
	call	_ZdlPv
.L128:
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
.L143:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$4, %r12
	call	memmove
	jmp	.L127
.L142:
	movabsq	$4611686018427387903, %rcx
	cmpq	%rcx, %rdx
	ja	.L131
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L129
	leaq	0(,%rax,8), %r13
	jmp	.L123
	.cfi_endproc
.LFE8993:
	.size	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LCOLDE9:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTE9:
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely
.LCOLDB10:
	.text
.LHOTB10:
	.p2align 4,,15
	.globl	_Z9read_fromRSiRi
	.type	_Z9read_fromRSiRi, @function
_Z9read_fromRSiRi:
.LFB8657:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8657
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdx, %r15
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	leaq	1200(%rdi), %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %r14
	movq	%rsi, %rbp
	subq	$24, %rsp
	.cfi_def_cfa_offset 80
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	movq	%rdi, %rax
	.p2align 4,,10
	.p2align 3
.L145:
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	addq	$24, %rax
	movq	$0, -8(%rax)
	cmpq	%r13, %rax
	jne	.L145
	movq	%rsp, %rsi
	movq	%rbp, %rdi
.LEHB2:
	call	_ZNSirsERi
	movl	(%rsp), %eax
	testl	%eax, %eax
	jle	.L146
	movq	%r14, %rbx
	xorl	%r12d, %r12d
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L173:
	testq	%rax, %rax
	movl	4(%rsp), %edx
	je	.L148
	movl	%edx, (%rax)
	movl	4(%rsp), %edx
.L148:
	addq	$4, %rax
	testl	%edx, %edx
	movq	%rax, 8(%rbx)
	je	.L172
.L150:
	leaq	4(%rsp), %rsi
	movq	%rbp, %rdi
	call	_ZNSirsERi
	movq	8(%rbx), %rax
	cmpq	16(%rbx), %rax
	jne	.L173
	leaq	4(%rsp), %rsi
	movq	%rbx, %rdi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
.LEHE2:
	movl	4(%rsp), %edx
	testl	%edx, %edx
	jne	.L150
	.p2align 4,,10
	.p2align 3
.L172:
	movl	(%rsp), %eax
	addl	$1, %r12d
	addq	$24, %rbx
	cmpl	%r12d, %eax
	jg	.L150
.L146:
	movq	8(%rsp), %rcx
	xorq	%fs:40, %rcx
	movl	%eax, (%r15)
	movq	%r14, %rax
	jne	.L174
	addq	$24, %rsp
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
.L157:
	.cfi_restore_state
	movq	%rax, %rbx
.L170:
	cmpq	%r13, %r14
	je	.L153
	subq	$24, %r13
	movq	0(%r13), %rdi
	testq	%rdi, %rdi
	je	.L170
	call	_ZdlPv
	jmp	.L170
.L174:
	call	__stack_chk_fail
.L153:
	movq	%rbx, %rdi
.LEHB3:
	call	_Unwind_Resume
.LEHE3:
	.cfi_endproc
.LFE8657:
	.section	.gcc_except_table
.LLSDA8657:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8657-.LLSDACSB8657
.LLSDACSB8657:
	.uleb128 .LEHB2-.LFB8657
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L157-.LFB8657
	.uleb128 0
	.uleb128 .LEHB3-.LFB8657
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
.LLSDACSE8657:
	.text
	.size	_Z9read_fromRSiRi, .-_Z9read_fromRSiRi
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 2
.LCOLDB11:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTB11:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_:
.LFB9240:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA9240
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
.LEHB4:
	call	_Znwm
.LEHE4:
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
	je	.L176
	movq	%r14, %rcx
	movq	%r15, %rdx
	movq	%r13, %rdi
.LEHB5:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%r15)
.L176:
	movq	16(%rbx), %rbp
	movq	%r15, %r12
	testq	%rbp, %rbp
	je	.L188
	.p2align 4,,10
	.p2align 3
.L192:
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
	je	.L178
	movq	%r14, %rcx
	movq	%rbx, %rdx
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE5:
	movq	%rax, 24(%rbx)
.L178:
	movq	16(%rbp), %rbp
	movq	%rbx, %r12
	testq	%rbp, %rbp
	jne	.L192
.L188:
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
.L183:
	.cfi_restore_state
.L181:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	%r15, %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.LEHB6:
	call	__cxa_rethrow
.LEHE6:
.L184:
	movq	%rax, %rbx
.L182:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB7:
	call	_Unwind_Resume
.LEHE7:
	.cfi_endproc
.LFE9240:
	.section	.gcc_except_table
	.align 4
.LLSDA9240:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT9240-.LLSDATTD9240
.LLSDATTD9240:
	.byte	0x1
	.uleb128 .LLSDACSE9240-.LLSDACSB9240
.LLSDACSB9240:
	.uleb128 .LEHB4-.LFB9240
	.uleb128 .LEHE4-.LEHB4
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB5-.LFB9240
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L183-.LFB9240
	.uleb128 0x1
	.uleb128 .LEHB6-.LFB9240
	.uleb128 .LEHE6-.LEHB6
	.uleb128 .L184-.LFB9240
	.uleb128 0
	.uleb128 .LEHB7-.LFB9240
	.uleb128 .LEHE7-.LEHB7
	.uleb128 0
	.uleb128 0
.LLSDACSE9240:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT9240:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LCOLDE11:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTE11:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,comdat
	.align 2
.LCOLDB12:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,comdat
.LHOTB12:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_:
.LFB9305:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rsi, %rbp
	movq	%rdi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	16(%rdi), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	leaq	8(%rbx), %rax
	movq	$0, 16(%rbx)
	movq	$0, 40(%rbx)
	movq	%rax, 24(%rbx)
	movq	%rax, 32(%rbx)
	movq	16(%rbp), %rdx
	testq	%rdx, %rdx
	je	.L198
	movq	%rdx, 16(%rbx)
	movq	24(%rbp), %rcx
	movq	%rcx, 24(%rbx)
	movq	32(%rbp), %rcx
	movq	%rcx, 32(%rbx)
	movq	%rax, 8(%rdx)
	leaq	8(%rbp), %rax
	movq	$0, 16(%rbp)
	movq	%rax, 24(%rbp)
	movq	%rax, 32(%rbp)
	movq	40(%rbp), %rax
	movq	%rax, 40(%rbx)
	movq	$0, 40(%rbp)
.L198:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	movq	%rbx, %rax
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9305:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,comdat
.LCOLDE12:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_,comdat
.LHOTE12:
	.section	.text.unlikely
.LCOLDB13:
	.text
.LHOTB13:
	.p2align 4,,15
	.type	_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81, @function
_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81:
.LFB9529:
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
	subq	$1, %rax
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %rbp
	subq	$120, %rsp
	.cfi_def_cfa_offset 176
	movq	%rdx, 32(%rsp)
	movq	%rax, %rdx
	movq	%rcx, 40(%rsp)
	shrq	$63, %rdx
	movq	%rsi, 16(%rsp)
	addq	%rdx, %rax
	sarq	%rax
	movq	%fs:40, %rcx
	movq	%rcx, 104(%rsp)
	xorl	%ecx, %ecx
	cmpq	%rax, %rsi
	movq	%rax, 24(%rsp)
	jge	.L271
	movq	16(%rsp), %rax
	leaq	(%rax,%rax,2), %r12
	movq	%rax, %r15
	salq	$4, %r12
	addq	%rdi, %r12
	jmp	.L215
	.p2align 4,,10
	.p2align 3
.L206:
	jbe	.L209
.L208:
	subq	$1, %r15
	leaq	(%r15,%r15,2), %rbx
	salq	$4, %rbx
	addq	%rbp, %rbx
.L209:
	movq	%rbx, %rsi
	movq	%r12, %rdi
	movq	%rbx, %r13
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	cmpq	24(%rsp), %r15
	jge	.L205
	movq	%rbx, %r12
.L215:
	leaq	1(%r15), %rax
	leaq	(%rax,%rax), %r15
	leaq	(%r15,%rax,4), %rbx
	salq	$4, %rbx
	leaq	-48(%rbp,%rbx), %rax
	addq	%rbp, %rbx
	movq	40(%rax), %rcx
	cmpq	%rcx, 40(%rbx)
	jne	.L206
	movq	24(%rax), %r13
	leaq	8(%rax), %rsi
	movq	24(%rbx), %r14
	leaq	8(%rbx), %rax
	movq	%rsi, 8(%rsp)
	movq	%rax, %rcx
	cmpq	%r13, %rsi
	movq	%rax, (%rsp)
	setne	%al
	cmpq	%r14, %rcx
	movl	%eax, %edi
	jne	.L269
	jmp	.L207
	.p2align 4,,10
	.p2align 3
.L212:
	movl	32(%r13), %eax
	cmpl	%eax, 32(%r14)
	jl	.L208
	jg	.L209
	movq	%r14, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r13, %rdi
	movq	%rax, %r14
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 8(%rsp)
	movq	%rax, %r13
	setne	%al
	cmpq	%r14, (%rsp)
	movl	%eax, %edi
	je	.L207
.L269:
	testb	%al, %al
	jne	.L212
.L207:
	cmpq	%r14, (%rsp)
	jne	.L209
	testb	%dil, %dil
	jne	.L208
	jmp	.L209
.L271:
	leaq	(%rsi,%rsi,2), %r13
	movq	%rsi, %r15
	salq	$4, %r13
	addq	%rdi, %r13
	.p2align 4,,10
	.p2align 3
.L205:
	movq	32(%rsp), %rax
	testb	$1, %al
	jne	.L216
	subq	$2, %rax
	movq	%rax, %rcx
	shrq	$63, %rcx
	addq	%rcx, %rax
	sarq	%rax
	cmpq	%r15, %rax
	je	.L272
.L216:
	movq	40(%rsp), %rdx
	leaq	56(%rsp), %rax
	movl	$0, 56(%rsp)
	movq	$0, 64(%rsp)
	movq	$0, 88(%rsp)
	movq	%rax, 72(%rsp)
	movq	%rax, 80(%rsp)
	movq	16(%rdx), %rcx
	testq	%rcx, %rcx
	je	.L217
	movq	24(%rdx), %rsi
	movq	%rcx, 64(%rsp)
	movq	%rsi, 72(%rsp)
	movq	32(%rdx), %rsi
	movq	%rsi, 80(%rsp)
	movq	%rax, 8(%rcx)
	leaq	8(%rdx), %rax
	movq	$0, 16(%rdx)
	movq	%rax, 24(%rdx)
	movq	%rax, 32(%rdx)
	movq	40(%rdx), %rax
	movq	$0, 40(%rdx)
	movq	%rax, 88(%rsp)
.L217:
	cmpq	16(%rsp), %r15
	jle	.L218
	leaq	-1(%r15), %rdx
	leaq	56(%rsp), %rax
	movq	%r13, %r14
	movq	%rdx, %rbx
	movq	%rax, (%rsp)
	shrq	$63, %rbx
	addq	%rdx, %rbx
	sarq	%rbx
	.p2align 4,,10
	.p2align 3
.L227:
	leaq	(%rbx,%rbx,2), %r12
	movq	88(%rsp), %rax
	salq	$4, %r12
	addq	%rbp, %r12
	cmpq	%rax, 40(%r12)
	je	.L273
	ja	.L221
.L234:
	movq	%r14, %r13
.L218:
	leaq	48(%rsp), %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	movq	64(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	104(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L274
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
.L273:
	.cfi_restore_state
	movq	72(%rsp), %r13
	cmpq	(%rsp), %r13
	leaq	8(%r12), %rax
	movq	24(%r12), %r15
	movq	%rax, %rcx
	movq	%rax, 8(%rsp)
	setne	%al
	cmpq	%r15, %rcx
	movl	%eax, %esi
	je	.L220
	testb	%al, %al
	je	.L220
	movl	32(%r15), %eax
	cmpl	%eax, 32(%r13)
	jg	.L221
	jge	.L223
	jmp	.L234
	.p2align 4,,10
	.p2align 3
.L275:
	testb	%al, %al
	je	.L220
	movl	32(%r13), %eax
	cmpl	%eax, 32(%r15)
	jl	.L221
	jg	.L234
.L223:
	movq	%r15, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r13, %rdi
	movq	%rax, %r15
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	(%rsp), %rax
	movq	%rax, %r13
	setne	%al
	cmpq	%r15, 8(%rsp)
	movl	%eax, %esi
	jne	.L275
.L220:
	cmpq	%r15, 8(%rsp)
	jne	.L234
	testb	%sil, %sil
	je	.L234
	.p2align 4,,10
	.p2align 3
.L221:
	movq	%r12, %rsi
	movq	%r14, %rdi
	movq	%r12, %r13
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	leaq	-1(%rbx), %rax
	movq	%rax, %rdx
	shrq	$63, %rdx
	addq	%rdx, %rax
	sarq	%rax
	cmpq	%rbx, 16(%rsp)
	jge	.L218
	movq	%r12, %r14
	movq	%rax, %rbx
	jmp	.L227
.L272:
	leaq	1(%r15), %rdx
	movq	%r13, %rdi
	leaq	(%rdx,%rdx), %rbx
	leaq	(%rbx,%rdx,4), %rax
	leaq	-1(%rbx), %r15
	salq	$4, %rax
	leaq	(%r15,%r15,2), %r13
	leaq	-48(%rbp,%rax), %rsi
	salq	$4, %r13
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	addq	%rbp, %r13
	jmp	.L216
.L274:
	call	__stack_chk_fail
	.cfi_endproc
.LFE9529:
	.size	_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81, .-_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81
	.section	.text.unlikely
.LCOLDE13:
	.text
.LHOTE13:
	.section	.text.unlikely
.LCOLDB14:
	.text
.LHOTB14:
	.p2align 4,,15
	.type	_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87, @function
_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87:
.LFB9535:
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
	subq	$72, %rsp
	.cfi_def_cfa_offset 128
	movq	16(%rdi), %rdx
	movq	%fs:40, %rax
	movq	%rax, 56(%rsp)
	xorl	%eax, %eax
	leaq	8(%rsp), %rax
	movl	$0, 8(%rsp)
	movq	$0, 16(%rsp)
	testq	%rdx, %rdx
	movq	$0, 40(%rsp)
	movq	%rax, 24(%rsp)
	movq	%rax, 32(%rsp)
	je	.L290
	movq	24(%rdi), %rcx
	movq	%rdx, 16(%rsp)
	movq	%rcx, 24(%rsp)
	movq	32(%rdi), %rcx
	movq	%rcx, 32(%rsp)
	movq	%rax, 8(%rdx)
	leaq	8(%rdi), %rax
	movq	$0, 16(%rdi)
	movq	%rax, 24(%rdi)
	movq	%rax, 32(%rdi)
	movq	40(%rdi), %rax
	movq	$0, 40(%rdi)
	movq	%rax, 40(%rsp)
.L277:
	leaq	-48(%rdi), %r12
	movq	%rdi, %r13
	leaq	8(%rsp), %r15
	jmp	.L287
	.p2align 4,,10
	.p2align 3
.L278:
	jnb	.L281
.L280:
	movq	%r12, %rsi
	movq	%r13, %rdi
	subq	$48, %r12
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	movq	40(%rsp), %rax
	subq	$48, %r13
.L287:
	cmpq	%rax, 40(%r12)
	jne	.L278
	movq	24(%r12), %rbp
	leaq	8(%r12), %r14
	movq	24(%rsp), %rbx
	cmpq	%r14, %rbp
	setne	%al
	cmpq	%r15, %rbx
	movl	%eax, %edx
	jne	.L307
	jmp	.L279
	.p2align 4,,10
	.p2align 3
.L284:
	movl	32(%rbp), %eax
	cmpl	%eax, 32(%rbx)
	jl	.L280
	jg	.L281
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rbp, %rdi
	movq	%rax, %rbx
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %r14
	movq	%rax, %rbp
	setne	%al
	cmpq	%r15, %rbx
	movl	%eax, %edx
	je	.L279
.L307:
	testb	%al, %al
	jne	.L284
.L279:
	cmpq	%r15, %rbx
	jne	.L281
	testb	%dl, %dl
	jne	.L280
	.p2align 4,,10
	.p2align 3
.L281:
	movq	%rsp, %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	movq	16(%rsp), %rsi
	movq	%rsp, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	56(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L309
	addq	$72, %rsp
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
.L290:
	.cfi_restore_state
	xorl	%eax, %eax
	jmp	.L277
.L309:
	call	__stack_chk_fail
	.cfi_endproc
.LFE9535:
	.size	_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87, .-_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87
	.section	.text.unlikely
.LCOLDE14:
	.text
.LHOTE14:
	.section	.text.unlikely
.LCOLDB15:
	.text
.LHOTB15:
	.p2align 4,,15
	.type	_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89, @function
_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89:
.LFB9537:
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
	subq	$120, %rsp
	.cfi_def_cfa_offset 176
	movq	%fs:40, %rax
	movq	%rax, 104(%rsp)
	xorl	%eax, %eax
	cmpq	%rsi, %rdi
	movq	%rsi, 40(%rsp)
	je	.L310
	leaq	48(%rdi), %rax
	movq	%rdi, %r12
	cmpq	%rax, %rsi
	je	.L310
	leaq	8(%rdi), %rax
	leaq	96(%rdi), %rbp
	leaq	56(%rsp), %r14
	movq	%rax, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L327:
	movq	-8(%rbp), %r13
	cmpq	40(%r12), %r13
	leaq	-48(%rbp), %rax
	movq	%rbp, 16(%rsp)
	movq	%rax, 8(%rsp)
	je	.L353
	jbe	.L316
.L315:
	movq	-32(%rbp), %rax
	movl	$0, 56(%rsp)
	movq	$0, 64(%rsp)
	movq	$0, 88(%rsp)
	movq	%r14, 72(%rsp)
	movq	%r14, 80(%rsp)
	testq	%rax, %rax
	je	.L322
	movq	-24(%rbp), %rdx
	movq	%rax, 64(%rsp)
	movq	%rdx, 72(%rsp)
	movq	-16(%rbp), %rdx
	movq	%rdx, 80(%rsp)
	movq	%r14, 8(%rax)
	leaq	-40(%rbp), %rax
	movq	$0, -32(%rbp)
	movq	%r13, 88(%rsp)
	movq	%rax, -24(%rbp)
	movq	%rax, -16(%rbp)
	movq	$0, -8(%rbp)
.L322:
	movq	8(%rsp), %rbx
	movabsq	$-6148914691236517205, %rax
	leaq	-48(%rbp), %r13
	subq	%r12, %rbx
	sarq	$4, %rbx
	imulq	%rax, %rbx
	testq	%rbx, %rbx
	jle	.L325
	.p2align 4,,10
	.p2align 3
.L342:
	movq	%r13, %rdi
	subq	$48, %r13
	movq	%r13, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	subq	$1, %rbx
	jne	.L342
.L325:
	leaq	48(%rsp), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	movq	64(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.L324:
	addq	$48, %rbp
	movq	16(%rsp), %rdx
	cmpq	%rdx, 40(%rsp)
	jne	.L327
.L310:
	movq	104(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L354
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
.L353:
	.cfi_restore_state
	movq	24(%r12), %r15
	cmpq	%r15, 24(%rsp)
	leaq	-40(%rbp), %rax
	movq	-24(%rbp), %rbx
	movq	%rax, %rcx
	movq	%rax, 32(%rsp)
	setne	%al
	cmpq	%rbx, %rcx
	movl	%eax, %esi
	jne	.L352
	jmp	.L314
	.p2align 4,,10
	.p2align 3
.L319:
	movl	32(%r15), %eax
	cmpl	%eax, 32(%rbx)
	jl	.L315
	jg	.L316
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r15, %rdi
	movq	%rax, %rbx
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 24(%rsp)
	movq	%rax, %r15
	setne	%al
	cmpq	%rbx, 32(%rsp)
	movl	%eax, %esi
	je	.L314
.L352:
	testb	%al, %al
	jne	.L319
.L314:
	cmpq	%rbx, 32(%rsp)
	jne	.L316
	testb	%sil, %sil
	jne	.L315
	.p2align 4,,10
	.p2align 3
.L316:
	movq	8(%rsp), %rdi
	call	_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87
	jmp	.L324
.L354:
	call	__stack_chk_fail
	.cfi_endproc
.LFE9537:
	.size	_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89, .-_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89
	.section	.text.unlikely
.LCOLDE15:
	.text
.LHOTE15:
	.section	.text.unlikely
.LCOLDB16:
	.text
.LHOTB16:
	.p2align 4,,15
	.type	_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90, @function
_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90:
.LFB9538:
	.cfi_startproc
	movq	%rsi, %rax
	subq	%rdi, %rax
	cmpq	$815, %rax
	jle	.L356
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	leaq	768(%rdi), %rbx
	movq	%rsi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	%rbx, %rsi
	call	_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89
	cmpq	%rbx, %rbp
	je	.L355
	.p2align 4,,10
	.p2align 3
.L361:
	movq	%rbx, %rdi
	addq	$48, %rbx
	call	_ZSt25__unguarded_linear_insertIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops14_Val_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_.isra.87
	cmpq	%rbx, %rbp
	jne	.L361
.L355:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L356:
	jmp	_ZSt16__insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.89
	.cfi_endproc
.LFE9538:
	.size	_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90, .-_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90
	.section	.text.unlikely
.LCOLDE16:
	.text
.LHOTE16:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,comdat
	.align 2
.LCOLDB17:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,comdat
.LHOTB17:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_:
.LFB9429:
	.cfi_startproc
	movq	16(%rdi), %rax
	testq	%rax, %rax
	je	.L370
	movq	16(%rsi), %rdx
	testq	%rdx, %rdx
	je	.L371
	movq	%rdx, 16(%rdi)
	movq	%rax, 16(%rsi)
	movq	24(%rsi), %rdx
	movq	24(%rdi), %rax
	movq	%rdx, 24(%rdi)
	movq	%rax, 24(%rsi)
	movq	32(%rsi), %rdx
	movq	32(%rdi), %rax
	movq	%rdx, 32(%rdi)
	movq	%rax, 32(%rsi)
	leaq	8(%rdi), %rdx
	movq	16(%rdi), %rax
	movq	%rdx, 8(%rax)
	movq	16(%rsi), %rax
	leaq	8(%rsi), %rdx
	movq	%rdx, 8(%rax)
	movq	40(%rdi), %rax
	movq	40(%rsi), %rdx
	movq	%rdx, 40(%rdi)
	movq	%rax, 40(%rsi)
.L363:
	rep ret
	.p2align 4,,10
	.p2align 3
.L370:
	movq	16(%rsi), %rax
	testq	%rax, %rax
	je	.L363
	movq	%rax, 16(%rdi)
	movq	24(%rsi), %rdx
	movq	%rdx, 24(%rdi)
	movq	32(%rsi), %rdx
	movq	%rdx, 32(%rdi)
	leaq	8(%rdi), %rdx
	movq	%rdx, 8(%rax)
	movq	40(%rsi), %rax
	movq	%rax, 40(%rdi)
	leaq	8(%rsi), %rax
	movq	$0, 16(%rsi)
	movq	$0, 40(%rsi)
	movq	%rax, 24(%rsi)
	movq	%rax, 32(%rsi)
	ret
	.p2align 4,,10
	.p2align 3
.L371:
	movq	%rax, 16(%rsi)
	movq	24(%rdi), %rdx
	movq	%rdx, 24(%rsi)
	movq	32(%rdi), %rdx
	movq	%rdx, 32(%rsi)
	leaq	8(%rsi), %rdx
	movq	%rdx, 8(%rax)
	movq	40(%rdi), %rax
	movq	%rax, 40(%rsi)
	leaq	8(%rdi), %rax
	movq	$0, 16(%rdi)
	movq	$0, 40(%rdi)
	movq	%rax, 24(%rdi)
	movq	%rax, 32(%rdi)
	ret
	.cfi_endproc
.LFE9429:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,comdat
.LCOLDE17:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_,comdat
.LHOTE17:
	.section	.text.unlikely
.LCOLDB18:
	.text
.LHOTB18:
	.p2align 4,,15
	.type	_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_, @function
_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_:
.LFB9118:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rsi, %rax
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	subq	%rdi, %rax
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$200, %rsp
	.cfi_def_cfa_offset 256
	movq	%rsi, 40(%rsp)
	movq	%rdi, 24(%rsp)
	movq	%fs:40, %rsi
	movq	%rsi, 184(%rsp)
	xorl	%esi, %esi
	cmpq	$815, %rax
	movq	%rdx, 48(%rsp)
	jle	.L372
	testq	%rdx, %rdx
	je	.L458
	leaq	96(%rdi), %rcx
	leaq	8(%rdi), %rbp
	movq	%rcx, 64(%rsp)
	leaq	56(%rdi), %rcx
	movq	%rcx, 56(%rsp)
	leaq	48(%rdi), %rcx
	movq	%rcx, 72(%rsp)
.L375:
	sarq	$4, %rax
	movabsq	$-6148914691236517205, %rsi
	subq	$1, 48(%rsp)
	imulq	%rsi, %rax
	sarq	%rax
	leaq	(%rax,%rax,2), %rbx
	movq	24(%rsp), %rax
	salq	$4, %rbx
	addq	%rax, %rbx
	movq	88(%rax), %r14
	movq	40(%rbx), %r12
	cmpq	%r12, %r14
	je	.L600
	jbe	.L386
.L385:
	movq	40(%rsp), %rax
	movq	-8(%rax), %r13
	cmpq	%r13, %r12
	je	.L601
.L392:
	ja	.L423
.L395:
	cmpq	%r13, %r14
	je	.L602
.L402:
	jbe	.L405
.L591:
	movq	40(%rsp), %rax
	leaq	-48(%rax), %r13
.L404:
	movq	24(%rsp), %rdi
	movq	%r13, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
.L401:
	movq	24(%rsp), %rax
	movq	40(%rsp), %rbx
	movq	40(%rax), %r13
	movq	64(%rsp), %rax
	movq	%rax, 8(%rsp)
	jmp	.L411
	.p2align 4,,10
	.p2align 3
.L431:
	addq	$48, 8(%rsp)
.L411:
	movq	8(%rsp), %rcx
	movq	%rcx, %rax
	subq	$48, %rax
	cmpq	%r13, -8(%rcx)
	movq	%rax, 16(%rsp)
	movq	%rax, 32(%rsp)
	je	.L603
	ja	.L431
	subq	$48, %rbx
	cmpq	%r13, 40(%rbx)
	je	.L604
	.p2align 4,,10
	.p2align 3
.L438:
	jnb	.L441
.L432:
	subq	$48, %rbx
	cmpq	%r13, 40(%rbx)
	jne	.L438
.L604:
	movq	24(%rsp), %rax
	leaq	8(%rbx), %r15
	movq	24(%rbx), %r14
	movq	24(%rax), %r12
	jmp	.L597
	.p2align 4,,10
	.p2align 3
.L605:
	testb	%al, %al
	je	.L439
	movl	32(%r14), %eax
	cmpl	%eax, 32(%r12)
	jl	.L432
	jg	.L441
	movq	%r12, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r14, %rdi
	movq	%rax, %r12
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rax, %r14
.L597:
	cmpq	%r14, %r15
	setne	%al
	cmpq	%r12, %rbp
	movl	%eax, %edx
	jne	.L605
.L439:
	cmpq	%r12, %rbp
	jne	.L441
	testb	%dl, %dl
	jne	.L432
	.p2align 4,,10
	.p2align 3
.L441:
	cmpq	16(%rsp), %rbx
	jbe	.L606
	movq	16(%rsp), %rdi
	movq	%rbx, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	movq	24(%rsp), %rax
	movq	40(%rax), %r13
	jmp	.L431
	.p2align 4,,10
	.p2align 3
.L603:
	movq	24(%rsp), %rax
	movq	-24(%rcx), %r12
	leaq	-40(%rcx), %r14
	movq	24(%rax), %r15
	cmpq	%r15, %rbp
	setne	%al
	cmpq	%r14, %r12
	movl	%eax, %esi
	je	.L430
	testb	%al, %al
	je	.L430
	movl	32(%r12), %eax
	cmpl	%eax, 32(%r15)
	jg	.L431
	jge	.L434
	jmp	.L432
	.p2align 4,,10
	.p2align 3
.L607:
	testb	%al, %al
	je	.L430
	movl	32(%r15), %eax
	cmpl	%eax, 32(%r12)
	jl	.L431
	jg	.L432
.L434:
	movq	%r12, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r15, %rdi
	movq	%rax, %r12
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %rbp
	movq	%rax, %r15
	setne	%al
	cmpq	%r14, %r12
	movl	%eax, %esi
	jne	.L607
.L430:
	cmpq	%r14, %r12
	jne	.L432
	testb	%sil, %sil
	jne	.L431
	jmp	.L432
	.p2align 4,,10
	.p2align 3
.L606:
	subq	$8, %rsp
	.cfi_def_cfa_offset 264
	movzbl	264(%rsp), %eax
	pushq	%rax
	.cfi_def_cfa_offset 272
	movq	32(%rsp), %rbx
	movq	64(%rsp), %rdx
	movq	56(%rsp), %rsi
	movq	%rbx, %rdi
	call	_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_
	movq	%rbx, %rax
	subq	40(%rsp), %rax
	popq	%rdx
	.cfi_def_cfa_offset 264
	popq	%rcx
	.cfi_def_cfa_offset 256
	cmpq	$815, %rax
	jle	.L372
	cmpq	$0, 48(%rsp)
	je	.L374
	movq	16(%rsp), %rsi
	movq	%rsi, 40(%rsp)
	jmp	.L375
.L611:
	movq	8(%rsp), %rbx
	movq	16(%rsp), %r12
	movq	%r15, %rbp
.L386:
	movq	40(%rsp), %rax
	movq	-8(%rax), %r13
	cmpq	%r13, %r14
	je	.L608
	ja	.L405
.L414:
	cmpq	%r13, %r12
	je	.L609
	ja	.L591
.L423:
	movq	24(%rsp), %rdi
	movq	%rbx, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	jmp	.L401
.L608:
	movq	%rax, %rsi
	subq	$40, %rax
	movq	-24(%rsi), %r14
	movq	24(%rsp), %rsi
	movq	%rax, 8(%rsp)
	cmpq	%r14, %rax
	movq	72(%rsi), %r15
	setne	%al
	cmpq	%r15, 56(%rsp)
	movl	%eax, %ecx
	jne	.L598
	jmp	.L413
	.p2align 4,,10
	.p2align 3
.L417:
	movl	32(%r14), %eax
	cmpl	%eax, 32(%r15)
	jl	.L405
	jg	.L414
	movq	%r15, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r14, %rdi
	movq	%rax, %r15
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 8(%rsp)
	movq	%rax, %r14
	setne	%al
	cmpq	%r15, 56(%rsp)
	movl	%eax, %ecx
	je	.L413
.L598:
	testb	%al, %al
	jne	.L417
.L413:
	cmpq	%r15, 56(%rsp)
	jne	.L414
	testb	%cl, %cl
	je	.L414
.L405:
	movq	72(%rsp), %rsi
	movq	24(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	jmp	.L401
.L600:
	movq	24(%rbx), %r13
	leaq	8(%rbx), %rax
	movq	24(%rsp), %rsi
	movq	%rax, %rdx
	cmpq	%r13, %rax
	movq	72(%rsi), %r15
	setne	%al
	cmpq	%r15, 56(%rsp)
	movl	%eax, %ecx
	je	.L384
	testb	%al, %al
	je	.L384
	movl	32(%r13), %eax
	cmpl	%eax, 32(%r15)
	jl	.L385
	jg	.L386
	movq	%rbx, 8(%rsp)
	movq	%r12, 16(%rsp)
	movq	%rdx, %rbx
	movq	%r15, %r12
	movq	%rbp, %r15
	movq	56(%rsp), %rbp
	jmp	.L388
.L612:
	testb	%al, %al
	je	.L563
	movl	32(%r13), %eax
	cmpl	%eax, 32(%r12)
	jl	.L610
	jg	.L611
.L388:
	movq	%r12, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r13, %rdi
	movq	%rax, %r12
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %rbx
	movq	%rax, %r13
	setne	%al
	cmpq	%r12, %rbp
	movl	%eax, %ecx
	jne	.L612
.L563:
	movq	%r15, %rbp
	movq	8(%rsp), %rbx
	movq	%r12, %r15
	movq	16(%rsp), %r12
.L384:
	cmpq	%r15, 56(%rsp)
	jne	.L386
	testb	%cl, %cl
	je	.L386
	movq	40(%rsp), %rax
	movq	-8(%rax), %r13
	cmpq	%r13, %r12
	jne	.L392
.L601:
	movq	%rax, %rsi
	movq	24(%rbx), %r15
	subq	$40, %rax
	movq	-24(%rsi), %r12
	leaq	8(%rbx), %rcx
	movq	%rax, 16(%rsp)
	movq	%rcx, 8(%rsp)
	cmpq	%r12, %rax
	setne	%al
	cmpq	%r15, %rcx
	movl	%eax, %esi
	jne	.L586
	jmp	.L393
	.p2align 4,,10
	.p2align 3
.L398:
	movl	32(%r12), %eax
	cmpl	%eax, 32(%r15)
	jl	.L423
	jg	.L395
	movq	%r15, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r12, %rdi
	movq	%rax, %r15
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 16(%rsp)
	movq	%rax, %r12
	setne	%al
	cmpq	%r15, 8(%rsp)
	movl	%eax, %esi
	je	.L393
.L586:
	testb	%al, %al
	jne	.L398
.L393:
	cmpq	%r15, 8(%rsp)
	jne	.L395
	testb	%sil, %sil
	jne	.L423
	cmpq	%r13, %r14
	jne	.L402
.L602:
	movq	40(%rsp), %rax
	leaq	-48(%rax), %r13
	movq	-24(%rax), %r14
	movq	24(%rsp), %rax
	leaq	8(%r13), %rbx
	movq	72(%rax), %r12
	jmp	.L590
.L613:
	testb	%al, %al
	je	.L403
	movl	32(%r14), %eax
	cmpl	%eax, 32(%r12)
	jl	.L404
	jg	.L405
	movq	%r12, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r14, %rdi
	movq	%rax, %r12
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rax, %r14
.L590:
	cmpq	%r14, %rbx
	setne	%al
	cmpq	%r12, 56(%rsp)
	movl	%eax, %edx
	jne	.L613
.L403:
	cmpq	%r12, 56(%rsp)
	jne	.L405
	testb	%dl, %dl
	jne	.L404
	movq	72(%rsp), %rsi
	movq	24(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE4swapERS5_
	jmp	.L401
	.p2align 4,,10
	.p2align 3
.L378:
	movq	96(%rsp), %rsi
	leaq	80(%rsp), %rdi
	leaq	88(%rsp), %rbx
	leaq	136(%rsp), %rbp
	movabsq	$-6148914691236517205, %r12
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	32(%rsp), %r13
	movq	24(%rsp), %r14
.L382:
	subq	$48, %r13
	movq	16(%r13), %rax
	movl	$0, 88(%rsp)
	movq	$0, 96(%rsp)
	movq	$0, 120(%rsp)
	movq	%rbx, 104(%rsp)
	movq	%rbx, 112(%rsp)
	testq	%rax, %rax
	je	.L380
	movq	24(%r13), %rdx
	movq	%rax, 96(%rsp)
	movq	%rdx, 104(%rsp)
	movq	32(%r13), %rdx
	movq	%rdx, 112(%rsp)
	movq	%rbx, 8(%rax)
	leaq	8(%r13), %rax
	movq	$0, 16(%r13)
	movq	%rax, 24(%r13)
	movq	%rax, 32(%r13)
	movq	40(%r13), %rax
	movq	$0, 40(%r13)
	movq	%rax, 120(%rsp)
.L380:
	movq	%r14, %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSEOS5_
	movq	96(%rsp), %rax
	movl	$0, 136(%rsp)
	movq	$0, 144(%rsp)
	movq	$0, 168(%rsp)
	movq	%rbp, 152(%rsp)
	movq	%rbp, 160(%rsp)
	testq	%rax, %rax
	je	.L381
	movq	104(%rsp), %rdx
	movq	%rax, 144(%rsp)
	movq	%rdx, 152(%rsp)
	movq	112(%rsp), %rdx
	movq	%rdx, 160(%rsp)
	movq	%rbp, 8(%rax)
	movq	120(%rsp), %rax
	movq	$0, 96(%rsp)
	movq	%rbx, 104(%rsp)
	movq	%rbx, 112(%rsp)
	movq	$0, 120(%rsp)
	movq	%rax, 168(%rsp)
.L381:
	movq	%r13, %r15
	leaq	128(%rsp), %rcx
	xorl	%esi, %esi
	subq	%r14, %r15
	movq	%r14, %rdi
	movq	%r15, %rdx
	sarq	$4, %rdx
	imulq	%r12, %rdx
	call	_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	96(%rsp), %rsi
	leaq	80(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	cmpq	$95, %r15
	jg	.L382
.L372:
	movq	184(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L614
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
.L609:
	.cfi_restore_state
	movq	40(%rsp), %rax
	movq	24(%rbx), %r14
	leaq	8(%rbx), %r12
	leaq	-48(%rax), %r13
	movq	-24(%rax), %r15
	leaq	8(%r13), %rcx
	cmpq	%r15, %rcx
	movq	%rcx, 8(%rsp)
	setne	%al
	cmpq	%r14, %r12
	movl	%eax, %ecx
	jne	.L593
	jmp	.L421
	.p2align 4,,10
	.p2align 3
.L426:
	movl	32(%r15), %eax
	cmpl	%eax, 32(%r14)
	jl	.L404
	jg	.L423
	movq	%r14, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r15, %rdi
	movq	%rax, %r14
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, 8(%rsp)
	movq	%rax, %r15
	setne	%al
	cmpq	%r14, %r12
	movl	%eax, %ecx
	je	.L421
.L593:
	testb	%al, %al
	jne	.L426
.L421:
	cmpq	%r14, %r12
	jne	.L423
	testb	%cl, %cl
	jne	.L404
	jmp	.L423
.L458:
	movq	40(%rsp), %rsi
	movq	%rsi, 32(%rsp)
.L374:
	sarq	$4, %rax
	movabsq	$-6148914691236517205, %r13
	movq	24(%rsp), %rsi
	imulq	%rax, %r13
	leaq	88(%rsp), %r14
	leaq	136(%rsp), %r12
	leaq	-2(%r13), %rbp
	sarq	%rbp
	leaq	0(%rbp,%rbp,2), %rax
	salq	$4, %rax
	leaq	8(%rsi,%rax), %rbx
	jmp	.L379
.L615:
	movq	16(%rbx), %rdx
	movq	%rax, 96(%rsp)
	movq	%rdx, 104(%rsp)
	movq	24(%rbx), %rdx
	movq	%rdx, 112(%rsp)
	movq	%r14, 8(%rax)
	movq	32(%rbx), %rax
	movq	$0, 8(%rbx)
	movq	%rbx, 16(%rbx)
	movq	%rbx, 24(%rbx)
	movq	$0, 32(%rbx)
	movl	$0, 136(%rsp)
	movq	%rax, 120(%rsp)
	movq	96(%rsp), %rax
	movq	$0, 144(%rsp)
	movq	$0, 168(%rsp)
	movq	%r12, 152(%rsp)
	movq	%r12, 160(%rsp)
	testq	%rax, %rax
	je	.L377
	movq	104(%rsp), %rdx
	movq	%rax, 144(%rsp)
	movq	%rdx, 152(%rsp)
	movq	112(%rsp), %rdx
	movq	%rdx, 160(%rsp)
	movq	%r12, 8(%rax)
	movq	120(%rsp), %rax
	movq	$0, 96(%rsp)
	movq	%r14, 104(%rsp)
	movq	%r14, 112(%rsp)
	movq	$0, 120(%rsp)
	movq	%rax, 168(%rsp)
.L377:
	movq	24(%rsp), %rdi
	leaq	128(%rsp), %rcx
	movq	%r13, %rdx
	movq	%rbp, %rsi
	subq	$48, %rbx
	call	_ZSt13__adjust_heapIPSt3setIiSt4lessIiESaIiEElS4_N9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_T0_SH_T1_T2_.isra.81
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	testq	%rbp, %rbp
	je	.L378
	movq	96(%rsp), %rsi
	leaq	80(%rsp), %rdi
	subq	$1, %rbp
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.L379:
	movq	8(%rbx), %rax
	movl	$0, 88(%rsp)
	movq	$0, 96(%rsp)
	movq	$0, 120(%rsp)
	movq	%r14, 104(%rsp)
	movq	%r14, 112(%rsp)
	testq	%rax, %rax
	jne	.L615
	movl	$0, 136(%rsp)
	movq	$0, 144(%rsp)
	movq	$0, 168(%rsp)
	movq	%r12, 152(%rsp)
	movq	%r12, 160(%rsp)
	jmp	.L377
.L610:
	movq	8(%rsp), %rbx
	movq	16(%rsp), %r12
	movq	%r15, %rbp
	jmp	.L385
.L614:
	call	__stack_chk_fail
	.cfi_endproc
.LFE9118:
	.size	_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_, .-_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_
	.section	.text.unlikely
.LCOLDE18:
	.text
.LHOTE18:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC19:
	.string	"food.inp"
.LC20:
	.string	"food.out"
	.section	.text.unlikely
.LCOLDB21:
	.section	.text.startup,"ax",@progbits
.LHOTB21:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB8678:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8678
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	$8, %edx
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movl	$.LC19, %esi
	subq	$4744, %rsp
	.cfi_def_cfa_offset 4784
	leaq	592(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 4728(%rsp)
	xorl	%eax, %eax
.LEHB8:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE8:
	leaq	80(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC20, %esi
.LEHB9:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE9:
	leaq	1120(%rsp), %rbp
	leaq	12(%rsp), %rdx
	leaq	592(%rsp), %rsi
	movq	%rbp, %rdi
.LEHB10:
	call	_Z9read_fromRSiRi
.LEHE10:
	leaq	2320(%rsp), %rbx
	movq	%rbp, %rsi
	movq	%rbx, %rdi
.LEHB11:
	call	_Z11get_bcc_arrRKSt5arrayISt6vectorIiSaIiEELm50EE
.LEHE11:
	subq	$8, %rsp
	.cfi_def_cfa_offset 4792
	leaq	2400(%rbx), %r12
	movl	$10, %edx
	pushq	$0
	.cfi_def_cfa_offset 4800
	movq	%rbx, %rdi
	movq	%r12, %rsi
	call	_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_
	movq	%r12, %rsi
	movq	%rbx, %rdi
	call	_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90
	movq	2352(%rsp), %rsi
	leaq	56(%rsp), %rdx
	movl	$0, 56(%rsp)
	movq	$0, 64(%rsp)
	movq	$0, 88(%rsp)
	movq	%rdx, 72(%rsp)
	movq	%rdx, 80(%rsp)
	testq	%rsi, %rsi
	popq	%rax
	.cfi_def_cfa_offset 4792
	popq	%rcx
	.cfi_def_cfa_offset 4784
	je	.L620
	leaq	32(%rsp), %rax
	leaq	16(%rsp), %rcx
	movq	%rax, %rdi
	movq	%rax, 16(%rsp)
.LEHB12:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE12:
	movq	%rax, 48(%rsp)
	movq	%rax, %rcx
	jmp	.L624
	.p2align 4,,10
	.p2align 3
.L636:
	movq	%rdx, %rcx
.L624:
	movq	16(%rcx), %rdx
	testq	%rdx, %rdx
	jne	.L636
	movq	%rcx, 56(%rsp)
	jmp	.L625
	.p2align 4,,10
	.p2align 3
.L637:
	movq	%rdx, %rax
.L625:
	movq	24(%rax), %rdx
	testq	%rdx, %rdx
	jne	.L637
	movq	%rax, 64(%rsp)
	movq	2360(%rsp), %rax
	movq	%rax, 72(%rsp)
.L620:
	leaq	32(%rsp), %rsi
	leaq	80(%rsp), %rdi
.LEHB13:
	call	_Z8write_toRSoRKSt3setIiSt4lessIiESaIiEE
.LEHE13:
	movq	48(%rsp), %rsi
	leaq	32(%rsp), %rdi
	leaq	2272(%rsp), %r12
	addq	$2352, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.p2align 4,,10
	.p2align 3
.L626:
	movq	16(%rbx), %rsi
	movq	%rbx, %rdi
	subq	$48, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	cmpq	%rbx, %r12
	jne	.L626
	leaq	1176(%rbp), %rbx
	leaq	1096(%rsp), %rbp
	.p2align 4,,10
	.p2align 3
.L628:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L627
	call	_ZdlPv
.L627:
	subq	$24, %rbx
	cmpq	%rbp, %rbx
	jne	.L628
	leaq	80(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	592(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	4728(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L661
	addq	$4744, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
.L638:
	.cfi_restore_state
	movq	%rax, %rbx
.L634:
	leaq	592(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB14:
	call	_Unwind_Resume
.LEHE14:
.L661:
	call	__stack_chk_fail
.L640:
	movq	48(%rsp), %rsi
	leaq	32(%rsp), %rdi
	leaq	2400(%rbx), %r13
	movq	%rax, %r12
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.L656:
	subq	$48, %r13
	movq	16(%r13), %rsi
	movq	%r13, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	cmpq	%rbx, %r13
	jne	.L656
	movq	%r12, %rbx
	leaq	1200(%rbp), %r12
.L655:
	subq	$24, %r12
	movq	(%r12), %rdi
	testq	%rdi, %rdi
	je	.L631
	call	_ZdlPv
.L631:
	cmpq	%rbp, %r12
	jne	.L655
	jmp	.L633
.L642:
	movq	%rax, %r12
	leaq	2400(%rbx), %r13
	jmp	.L656
.L641:
	movq	%rax, %rbx
	leaq	1200(%rbp), %r12
	jmp	.L655
.L639:
	movq	%rax, %rbx
.L633:
	leaq	80(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	jmp	.L634
	.cfi_endproc
.LFE8678:
	.section	.gcc_except_table
.LLSDA8678:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8678-.LLSDACSB8678
.LLSDACSB8678:
	.uleb128 .LEHB8-.LFB8678
	.uleb128 .LEHE8-.LEHB8
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB9-.LFB8678
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L638-.LFB8678
	.uleb128 0
	.uleb128 .LEHB10-.LFB8678
	.uleb128 .LEHE10-.LEHB10
	.uleb128 .L639-.LFB8678
	.uleb128 0
	.uleb128 .LEHB11-.LFB8678
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L641-.LFB8678
	.uleb128 0
	.uleb128 .LEHB12-.LFB8678
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L642-.LFB8678
	.uleb128 0
	.uleb128 .LEHB13-.LFB8678
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L640-.LFB8678
	.uleb128 0
	.uleb128 .LEHB14-.LFB8678
	.uleb128 .LEHE14-.LEHB14
	.uleb128 0
	.uleb128 0
.LLSDACSE8678:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE21:
	.section	.text.startup
.LHOTE21:
	.section	.text.unlikely
.LCOLDB22:
	.text
.LHOTB22:
	.p2align 4,,15
	.globl	_Z10result_bccRSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.type	_Z10result_bccRSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, @function
_Z10result_bccRSt5arrayISt3setIiSt4lessIiESaIiEELm50EE:
.LFB8650:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	leaq	2400(%rsi), %r12
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rsi, %rbp
	movq	%rdi, %rbx
	movl	$10, %edx
	movq	%r12, %rsi
	movq	%rbp, %rdi
	subq	$24, %rsp
	.cfi_def_cfa_offset 56
	movq	%fs:40, %rax
	movq	%rax, 16(%rsp)
	xorl	%eax, %eax
	pushq	$0
	.cfi_def_cfa_offset 64
	call	_ZSt16__introsort_loopIPSt3setIiSt4lessIiESaIiEElN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_T1_
	movq	%r12, %rsi
	movq	%rbp, %rdi
	call	_ZSt22__final_insertion_sortIPSt3setIiSt4lessIiESaIiEEN9__gnu_cxx5__ops15_Iter_comp_iterIZ10result_bccRSt5arrayIS4_Lm50EEEUlRKS4_SD_E_EEEvT_SG_T0_.isra.90
	popq	%rax
	.cfi_def_cfa_offset 56
	popq	%rdx
	.cfi_def_cfa_offset 48
	leaq	8(%rbx), %rdx
	movq	$0, 16(%rbx)
	movl	$0, 8(%rbx)
	movq	$0, 40(%rbx)
	movq	%rdx, 24(%rbx)
	movq	%rdx, 32(%rbx)
	movq	16(%rbp), %rsi
	testq	%rsi, %rsi
	je	.L662
	movq	%rsp, %rcx
	movq	%rbx, %rdi
	movq	%rbx, (%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_11_Alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 16(%rbx)
	movq	%rax, %rcx
	jmp	.L665
	.p2align 4,,10
	.p2align 3
.L668:
	movq	%rdx, %rcx
.L665:
	movq	16(%rcx), %rdx
	testq	%rdx, %rdx
	jne	.L668
	movq	%rcx, 24(%rbx)
	jmp	.L666
	.p2align 4,,10
	.p2align 3
.L669:
	movq	%rdx, %rax
.L666:
	movq	24(%rax), %rdx
	testq	%rdx, %rdx
	jne	.L669
	movq	%rax, 32(%rbx)
	movq	40(%rbp), %rax
	movq	%rax, 40(%rbx)
.L662:
	movq	8(%rsp), %rdi
	xorq	%fs:40, %rdi
	movq	%rbx, %rax
	jne	.L674
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
.L674:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE8650:
	.size	_Z10result_bccRSt5arrayISt3setIiSt4lessIiESaIiEELm50EE, .-_Z10result_bccRSt5arrayISt3setIiSt4lessIiESaIiEELm50EE
	.section	.text.unlikely
.LCOLDE22:
	.text
.LHOTE22:
	.section	.text.unlikely
.LCOLDB23:
	.section	.text.startup
.LHOTB23:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_count, @function
_GLOBAL__sub_I_count:
.LFB9447:
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
.LFE9447:
	.size	_GLOBAL__sub_I_count, .-_GLOBAL__sub_I_count
	.section	.text.unlikely
.LCOLDE23:
	.section	.text.startup
.LHOTE23:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_count
	.local	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EEE4time
	.comm	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_RSt5arrayISt3setIiSt4lessIiESaIiEELm50EEE4time,4,4
	.local	_ZL9bcc_label
	.comm	_ZL9bcc_label,4,4
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
