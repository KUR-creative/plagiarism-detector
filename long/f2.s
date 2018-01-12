	.file	"f2.cpp"
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
.LFB8478:
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
.LFE8478:
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
.LFB8522:
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
.LFE8522:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
.LCOLDE1:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EED5Ev,comdat
.LHOTE1:
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev
	.set	_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev,_ZNSt6vectorIS_IiSaIiEESaIS1_EED2Ev
	.section	.text.unlikely._ZNSt6vectorIbSaIbEED2Ev,"axG",@progbits,_ZNSt6vectorIbSaIbEED5Ev,comdat
	.align 2
.LCOLDB2:
	.section	.text._ZNSt6vectorIbSaIbEED2Ev,"axG",@progbits,_ZNSt6vectorIbSaIbEED5Ev,comdat
.LHOTB2:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIbSaIbEED2Ev
	.type	_ZNSt6vectorIbSaIbEED2Ev, @function
_ZNSt6vectorIbSaIbEED2Ev:
.LFB8525:
	.cfi_startproc
	movq	(%rdi), %rdi
	testq	%rdi, %rdi
	je	.L14
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L14:
	rep ret
	.cfi_endproc
.LFE8525:
	.size	_ZNSt6vectorIbSaIbEED2Ev, .-_ZNSt6vectorIbSaIbEED2Ev
	.section	.text.unlikely._ZNSt6vectorIbSaIbEED2Ev,"axG",@progbits,_ZNSt6vectorIbSaIbEED5Ev,comdat
.LCOLDE2:
	.section	.text._ZNSt6vectorIbSaIbEED2Ev,"axG",@progbits,_ZNSt6vectorIbSaIbEED5Ev,comdat
.LHOTE2:
	.weak	_ZNSt6vectorIbSaIbEED1Ev
	.set	_ZNSt6vectorIbSaIbEED1Ev,_ZNSt6vectorIbSaIbEED2Ev
	.section	.text.unlikely,"ax",@progbits
.LCOLDB3:
	.text
.LHOTB3:
	.p2align 4,,15
	.globl	_Z3dfsii
	.type	_Z3dfsii, @function
_Z3dfsii:
.LFB7972:
	.cfi_startproc
	movslq	%edi, %rdx
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	leaq	0(,%rdx,4), %r14
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
	movl	%esi, %r13d
	movq	%r14, %rsi
	leaq	(%rdx,%rdx,2), %r12
	movq	%rdx, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	addq	dfn(%rip), %rsi
	movl	piv(%rip), %eax
	movq	low(%rip), %rcx
	salq	$3, %r12
	addl	$1, %eax
	movl	%eax, piv(%rip)
	movl	%eax, (%rcx,%r14)
	movl	%eax, (%rsi)
	movq	par(%rip), %rax
	movq	edges(%rip), %rsi
	movl	%r13d, (%rax,%rdx,4)
	leaq	(%rsi,%r12), %rax
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	testl	%eax, %eax
	jle	.L16
	xorl	%ebx, %ebx
	jmp	.L22
	.p2align 4,,10
	.p2align 3
.L19:
	leaq	(%rcx,%r14), %rdx
	cmpl	%eax, (%rdx)
	cmovle	(%rdx), %eax
	movl	%eax, (%rdx)
.L18:
	leaq	(%rsi,%r12), %rax
	leal	1(%rbx), %edi
	addq	$1, %rbx
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	cmpl	%eax, %edi
	jge	.L16
.L22:
	movl	(%rdx,%rbx,4), %edi
	cmpl	%edi, %r13d
	je	.L18
	movq	dfn(%rip), %rax
	movslq	%edi, %r15
	movl	(%rax,%r15,4), %eax
	testl	%eax, %eax
	jne	.L19
	movl	%ebp, %esi
	call	_Z3dfsii
	movq	low(%rip), %rcx
	movq	edges(%rip), %rsi
	leaq	(%rcx,%r14), %rdx
	movl	(%rdx), %eax
	cmpl	%eax, (%rcx,%r15,4)
	cmovle	(%rcx,%r15,4), %eax
	movl	%eax, (%rdx)
	jmp	.L18
	.p2align 4,,10
	.p2align 3
.L16:
	addq	$8, %rsp
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
	.cfi_endproc
.LFE7972:
	.size	_Z3dfsii, .-_Z3dfsii
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
	.align 2
.LCOLDB4:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTB4:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_:
.LFB8192:
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
	je	.L33
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L45
.L34:
	movq	$-4, %r13
	jmp	.L26
	.p2align 4,,10
	.p2align 3
.L33:
	movl	$4, %r13d
.L26:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L32:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movl	(%r12), %ecx
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	addq	%rdx, %r12
	je	.L28
	movl	%ecx, (%r12)
.L28:
	testq	%rax, %rax
	jne	.L46
	addq	$4, %r12
	testq	%r14, %r14
	je	.L31
.L30:
	movq	%r14, %rdi
	call	_ZdlPv
.L31:
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
.L46:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$4, %r12
	call	memmove
	jmp	.L30
.L45:
	movabsq	$4611686018427387903, %rcx
	cmpq	%rcx, %rdx
	ja	.L34
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L32
	leaq	0(,%rax,8), %r13
	jmp	.L26
	.cfi_endproc
.LFE8192:
	.size	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LCOLDE4:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTE4:
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely
.LCOLDB5:
	.text
.LHOTB5:
	.p2align 4,,15
	.globl	_Z5colorii
	.type	_Z5colorii, @function
_Z5colorii:
.LFB7973:
	.cfi_startproc
	movslq	%edi, %rcx
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	leaq	(%rcx,%rcx,2), %r13
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	salq	$3, %r13
	subq	$24, %rsp
	.cfi_def_cfa_offset 64
	testl	%esi, %esi
	movl	%esi, 12(%rsp)
	jle	.L49
	movq	%r13, %rdi
	addq	bcc(%rip), %rdi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L50
	testq	%rax, %rax
	je	.L51
	movl	%esi, (%rax)
.L51:
	addq	$4, %rax
	movq	%rax, 8(%rdi)
.L49:
	movq	vis(%rip), %rsi
	movq	edges(%rip), %r8
	movq	%rcx, %rdx
	shrq	$6, %rdx
	movl	$1, %eax
	salq	%cl, %rax
	orq	%rax, (%rsi,%rdx,8)
	leaq	(%r8,%r13), %rax
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	testl	%eax, %eax
	jle	.L47
	leaq	0(,%rcx,4), %rbp
	xorl	%ebx, %ebx
	movl	$1, %r12d
	jmp	.L53
	.p2align 4,,10
	.p2align 3
.L67:
	movq	%r13, %rdi
	addq	bcc(%rip), %rdi
	movl	cpiv(%rip), %eax
	leal	1(%rax), %esi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	movl	%esi, cpiv(%rip)
	je	.L56
	testq	%rax, %rax
	je	.L57
	movl	%esi, (%rax)
	movl	cpiv(%rip), %esi
.L57:
	addq	$4, %rax
	movq	%rax, 8(%rdi)
.L66:
	movl	%ecx, %edi
	call	_Z5colorii
	movq	edges(%rip), %r8
.L54:
	leaq	(%r8,%r13), %rax
	leal	1(%rbx), %ecx
	addq	$1, %rbx
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	cmpl	%eax, %ecx
	jge	.L47
	movq	vis(%rip), %rsi
.L53:
	movslq	(%rdx,%rbx,4), %rax
	movq	%r12, %rdi
	movq	%rax, %rdx
	movq	%rax, %rcx
	shrq	$6, %rdx
	salq	%cl, %rdi
	testq	%rdi, (%rsi,%rdx,8)
	jne	.L54
	movq	low(%rip), %rdx
	movq	dfn(%rip), %rsi
	movl	(%rdx,%rax,4), %eax
	cmpl	%eax, (%rsi,%rbp)
	jle	.L67
	movl	12(%rsp), %esi
	jmp	.L66
	.p2align 4,,10
	.p2align 3
.L47:
	addq	$24, %rsp
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
	.p2align 4,,10
	.p2align 3
.L56:
	.cfi_restore_state
	movl	$cpiv, %esi
	movl	%ecx, (%rsp)
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	movl	cpiv(%rip), %esi
	movl	(%rsp), %ecx
	jmp	.L66
.L50:
	leaq	12(%rsp), %rsi
	movq	%rcx, (%rsp)
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	movq	(%rsp), %rcx
	jmp	.L49
	.cfi_endproc
.LFE7973:
	.size	_Z5colorii, .-_Z5colorii
	.section	.text.unlikely
.LCOLDE5:
	.text
.LHOTE5:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC6:
	.string	"vector::_M_default_append"
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,comdat
	.align 2
.LCOLDB7:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,comdat
.LHOTB7:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm
	.type	_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm, @function
_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm:
.LFB8220:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L114
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movabsq	$-6148914691236517205, %rdx
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
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	8(%rdi), %r13
	movq	16(%rdi), %rax
	subq	%r13, %rax
	sarq	$3, %rax
	imulq	%rdx, %rax
	cmpq	%rax, %rsi
	ja	.L70
	movq	%rsi, %rdx
	movq	%r13, %rax
	.p2align 4,,10
	.p2align 3
.L72:
	testq	%rax, %rax
	je	.L71
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
.L71:
	addq	$24, %rax
	subq	$1, %rdx
	jne	.L72
	leaq	(%rsi,%rsi,2), %rax
	leaq	0(%r13,%rax,8), %rax
	movq	%rax, 8(%rdi)
.L68:
	addq	$8, %rsp
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_restore 13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_restore 14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_restore 15
	.cfi_def_cfa_offset 8
.L114:
	rep ret
	.p2align 4,,10
	.p2align 3
.L70:
	.cfi_def_cfa_offset 64
	.cfi_offset 3, -56
	.cfi_offset 6, -48
	.cfi_offset 12, -40
	.cfi_offset 13, -32
	.cfi_offset 14, -24
	.cfi_offset 15, -16
	movq	%rdi, %rbx
	movq	(%rdi), %rdi
	movq	%r13, %rax
	movabsq	$768614336404564650, %rcx
	movq	%rsi, %r15
	subq	%rdi, %rax
	sarq	$3, %rax
	imulq	%rax, %rdx
	movq	%rcx, %rax
	subq	%rdx, %rax
	cmpq	%rax, %rsi
	ja	.L115
	cmpq	%rdx, %rsi
	movq	%rdx, %rax
	cmovnb	%rsi, %rax
	addq	%rax, %rdx
	jc	.L89
	cmpq	%rcx, %rdx
	ja	.L89
	leaq	(%rdx,%rdx,2), %r12
	salq	$3, %r12
	testq	%rdx, %rdx
	jne	.L86
	xorl	%r12d, %r12d
	xorl	%ebp, %ebp
	jmp	.L85
	.p2align 4,,10
	.p2align 3
.L89:
	movq	$-16, %r12
.L86:
	movq	%r12, %rdi
	call	_Znwm
	movq	8(%rbx), %r13
	movq	(%rbx), %rdi
	movq	%rax, %rbp
	addq	%rax, %r12
.L85:
	cmpq	%r13, %rdi
	je	.L87
	movq	%rbp, %rax
	movq	%rdi, %rdx
	.p2align 4,,10
	.p2align 3
.L78:
	testq	%rax, %rax
	je	.L77
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
.L77:
	addq	$24, %rdx
	addq	$24, %rax
	cmpq	%rdx, %r13
	jne	.L78
	addq	$24, %rdi
	movq	(%rbx), %r14
	subq	%rdi, %r13
	shrq	$3, %r13
	leaq	24(%rbp,%r13,8), %rcx
	movq	8(%rbx), %r13
.L76:
	movq	%rcx, %rax
	movq	%r15, %rdx
	.p2align 4,,10
	.p2align 3
.L80:
	testq	%rax, %rax
	je	.L79
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
.L79:
	addq	$24, %rax
	subq	$1, %rdx
	jne	.L80
	leaq	(%r15,%r15,2), %rax
	cmpq	%r13, %r14
	leaq	(%rcx,%rax,8), %r15
	je	.L81
	.p2align 4,,10
	.p2align 3
.L83:
	movq	(%r14), %rdi
	testq	%rdi, %rdi
	je	.L82
	call	_ZdlPv
.L82:
	addq	$24, %r14
	cmpq	%r13, %r14
	jne	.L83
	movq	(%rbx), %r13
.L81:
	testq	%r13, %r13
	je	.L84
	movq	%r13, %rdi
	call	_ZdlPv
.L84:
	movq	%rbp, (%rbx)
	movq	%r15, 8(%rbx)
	movq	%r12, 16(%rbx)
	jmp	.L68
.L87:
	movq	%r13, %r14
	movq	%rbp, %rcx
	jmp	.L76
.L115:
	movl	$.LC6, %edi
	call	_ZSt20__throw_length_errorPKc
	.cfi_endproc
.LFE8220:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,comdat
.LCOLDE7:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm,comdat
.LHOTE7:
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,comdat
	.align 2
.LCOLDB8:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,comdat
.LHOTB8:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm
	.type	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm, @function
_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm:
.LFB8090:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movabsq	$-6148914691236517205, %rdx
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	movq	8(%rdi), %rbp
	movq	(%rdi), %rcx
	movq	%rbp, %rax
	subq	%rcx, %rax
	sarq	$3, %rax
	imulq	%rdx, %rax
	cmpq	%rax, %rsi
	ja	.L128
	jnb	.L116
	leaq	(%rsi,%rsi,2), %rax
	movq	%rdi, %r12
	leaq	(%rcx,%rax,8), %r13
	cmpq	%rbp, %r13
	movq	%r13, %rbx
	je	.L121
	.p2align 4,,10
	.p2align 3
.L125:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L120
	call	_ZdlPv
.L120:
	addq	$24, %rbx
	cmpq	%rbx, %rbp
	jne	.L125
.L121:
	movq	%r13, 8(%r12)
.L116:
	addq	$8, %rsp
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
	.p2align 4,,10
	.p2align 3
.L128:
	.cfi_restore_state
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	subq	%rax, %rsi
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	jmp	_ZNSt6vectorIS_IiSaIiEESaIS1_EE17_M_default_appendEm
	.cfi_endproc
.LFE8090:
	.size	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm, .-_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm
	.section	.text.unlikely._ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,comdat
.LCOLDE8:
	.section	.text._ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,"axG",@progbits,_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm,comdat
.LHOTE8:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE17_M_default_appendEm,comdat
	.align 2
.LCOLDB9:
	.section	.text._ZNSt6vectorIiSaIiEE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE17_M_default_appendEm,comdat
.LHOTB9:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE17_M_default_appendEm
	.type	_ZNSt6vectorIiSaIiEE17_M_default_appendEm, @function
_ZNSt6vectorIiSaIiEE17_M_default_appendEm:
.LFB8222:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L155
	movq	8(%rdi), %rcx
	movq	16(%rdi), %rax
	subq	%rcx, %rax
	sarq	$2, %rax
	cmpq	%rax, %rsi
	ja	.L131
	movq	%rsi, %rdx
	movq	%rcx, %rax
	.p2align 4,,10
	.p2align 3
.L132:
	movl	$0, (%rax)
	addq	$4, %rax
	subq	$1, %rdx
	jne	.L132
	leaq	(%rcx,%rsi,4), %rax
	movq	%rax, 8(%rdi)
	ret
	.p2align 4,,10
	.p2align 3
.L131:
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
	movq	%rsi, %rbx
	movabsq	$4611686018427387903, %rsi
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	(%rdi), %r14
	movq	%rsi, %rdx
	subq	%r14, %rcx
	movq	%rcx, %rax
	movq	%rcx, %r12
	sarq	$2, %rax
	subq	%rax, %rdx
	movq	%rax, %rcx
	cmpq	%rdx, %rbx
	ja	.L156
	cmpq	%rax, %rbx
	movq	%rax, %rdx
	cmovnb	%rbx, %rdx
	addq	%rdx, %rax
	jc	.L143
	cmpq	%rsi, %rax
	ja	.L143
	xorl	%r13d, %r13d
	xorl	%r15d, %r15d
	testq	%rax, %rax
	jne	.L157
	.p2align 4,,10
	.p2align 3
.L140:
	testq	%rcx, %rcx
	jne	.L158
.L137:
	leaq	(%r15,%r12), %rcx
	movq	%rbx, %rax
	movq	%rcx, %rdx
	.p2align 4,,10
	.p2align 3
.L138:
	movl	$0, (%rdx)
	addq	$4, %rdx
	subq	$1, %rax
	jne	.L138
	testq	%r14, %r14
	leaq	(%rcx,%rbx,4), %rbx
	je	.L139
	movq	%r14, %rdi
	call	_ZdlPv
.L139:
	movq	%r15, 0(%rbp)
	movq	%rbx, 8(%rbp)
	movq	%r13, 16(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_restore 13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_restore 14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_restore 15
	.cfi_def_cfa_offset 8
.L155:
	rep ret
	.p2align 4,,10
	.p2align 3
.L143:
	.cfi_def_cfa_offset 64
	.cfi_offset 3, -56
	.cfi_offset 6, -48
	.cfi_offset 12, -40
	.cfi_offset 13, -32
	.cfi_offset 14, -24
	.cfi_offset 15, -16
	movq	$-4, %r13
.L141:
	movq	%r13, %rdi
	call	_Znwm
	movq	0(%rbp), %r14
	movq	8(%rbp), %r12
	movq	%rax, %r15
	addq	%rax, %r13
	subq	%r14, %r12
	movq	%r12, %rcx
	sarq	$2, %rcx
	jmp	.L140
	.p2align 4,,10
	.p2align 3
.L158:
	movq	%r12, %rdx
	movq	%r14, %rsi
	movq	%r15, %rdi
	call	memmove
	jmp	.L137
.L157:
	leaq	0(,%rax,4), %r13
	jmp	.L141
.L156:
	movl	$.LC6, %edi
	call	_ZSt20__throw_length_errorPKc
	.cfi_endproc
.LFE8222:
	.size	_ZNSt6vectorIiSaIiEE17_M_default_appendEm, .-_ZNSt6vectorIiSaIiEE17_M_default_appendEm
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE17_M_default_appendEm,comdat
.LCOLDE9:
	.section	.text._ZNSt6vectorIiSaIiEE17_M_default_appendEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE17_M_default_appendEm,comdat
.LHOTE9:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE6resizeEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE6resizeEm,comdat
	.align 2
.LCOLDB10:
	.section	.text._ZNSt6vectorIiSaIiEE6resizeEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE6resizeEm,comdat
.LHOTB10:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE6resizeEm
	.type	_ZNSt6vectorIiSaIiEE6resizeEm, @function
_ZNSt6vectorIiSaIiEE6resizeEm:
.LFB8091:
	.cfi_startproc
	movq	(%rdi), %rdx
	movq	8(%rdi), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	cmpq	%rax, %rsi
	ja	.L162
	jnb	.L159
	leaq	(%rdx,%rsi,4), %rax
	movq	%rax, 8(%rdi)
.L159:
	rep ret
	.p2align 4,,10
	.p2align 3
.L162:
	subq	%rax, %rsi
	jmp	_ZNSt6vectorIiSaIiEE17_M_default_appendEm
	.cfi_endproc
.LFE8091:
	.size	_ZNSt6vectorIiSaIiEE6resizeEm, .-_ZNSt6vectorIiSaIiEE6resizeEm
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE6resizeEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE6resizeEm,comdat
.LCOLDE10:
	.section	.text._ZNSt6vectorIiSaIiEE6resizeEm,"axG",@progbits,_ZNSt6vectorIiSaIiEE6resizeEm,comdat
.LHOTE10:
	.section	.rodata.str1.1
.LC11:
	.string	"vector<bool>::_M_fill_insert"
	.section	.text.unlikely._ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,"axG",@progbits,_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,comdat
	.align 2
.LCOLDB12:
	.section	.text._ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,"axG",@progbits,_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,comdat
.LHOTB12:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb
	.type	_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb, @function
_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb:
.LFB8312:
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
	testq	%rcx, %rcx
	movq	%rsi, 48(%rsp)
	movq	%rdx, 56(%rsp)
	je	.L163
	movq	16(%rdi), %r13
	movq	(%rdi), %rdx
	movq	%rcx, %r11
	movl	24(%rdi), %eax
	movl	8(%rdi), %r14d
	movl	%r8d, %r12d
	movq	%rsi, %rbp
	movl	56(%rsp), %ebx
	movq	%r13, %rcx
	subq	%rdx, %rcx
	leaq	(%rax,%rcx,8), %r10
	movq	32(%rdi), %rcx
	movq	%rax, %r9
	subq	%rdx, %rcx
	movq	%r10, %rdx
	salq	$3, %rcx
	subq	%r14, %rdx
	subq	%r10, %rcx
	cmpq	%rcx, %r11
	ja	.L165
	leaq	(%r11,%rax), %rdx
	leaq	63(%rdx), %rcx
	testq	%rdx, %rdx
	cmovns	%rdx, %rcx
	sarq	$6, %rcx
	leaq	0(%r13,%rcx,8), %rcx
	movq	%rcx, %r10
	movq	%rcx, 24(%rsp)
	movq	%rdx, %rcx
	sarq	$63, %rcx
	shrq	$58, %rcx
	addq	%rcx, %rdx
	andl	$63, %edx
	subq	%rcx, %rdx
	testq	%rdx, %rdx
	movq	%rdx, 8(%rsp)
	movq	%rdx, 16(%rsp)
	js	.L311
.L166:
	movl	%ebx, %ecx
	movq	%rcx, %r15
	movq	%rcx, 32(%rsp)
	movq	%r13, %rcx
	subq	%rsi, %rcx
	leaq	(%rax,%rcx,8), %rax
	subq	%r15, %rax
	movl	$1, %r15d
	testq	%rax, %rax
	jle	.L176
	movq	%rsi, 40(%rsp)
	jmp	.L292
	.p2align 4,,10
	.p2align 3
.L313:
	subl	$1, %r9d
	movq	%r15, %r14
	movl	%r9d, %ecx
	salq	%cl, %r14
	testl	%edx, %edx
	je	.L172
.L314:
	subl	$1, %edx
	movq	%r15, %rsi
	movl	%edx, %ecx
	salq	%cl, %rsi
	testq	%r14, 0(%r13)
	movq	%rsi, %rcx
	je	.L174
.L315:
	orq	%rcx, (%r10)
	subq	$1, %rax
	je	.L312
.L292:
	testl	%r9d, %r9d
	jne	.L313
	subq	$8, %r13
	testl	%edx, %edx
	movabsq	$-9223372036854775808, %r14
	movl	$63, %r9d
	jne	.L314
.L172:
	subq	$8, %r10
	testq	%r14, 0(%r13)
	movabsq	$-9223372036854775808, %rcx
	movl	$63, %edx
	jne	.L315
.L174:
	notq	%rcx
	andq	%rcx, (%r10)
	subq	$1, %rax
	jne	.L292
.L312:
	movq	40(%rsp), %rsi
.L176:
	addq	32(%rsp), %r11
	leaq	63(%r11), %rax
	testq	%r11, %r11
	cmovns	%r11, %rax
	sarq	$6, %rax
	leaq	(%rsi,%rax,8), %rdx
	movq	%r11, %rax
	sarq	$63, %rax
	shrq	$58, %rax
	addq	%rax, %r11
	andl	$63, %r11d
	subq	%rax, %r11
	js	.L316
.L169:
	cmpq	%rsi, %rdx
	movl	%r11d, %r9d
	je	.L317
	addq	$8, %rsi
	movzbl	%r8b, %r8d
	negl	%r8d
	cmpq	%rsi, %rdx
	movq	%rsi, %rax
	movslq	%r8d, %r8
	je	.L182
	.p2align 4,,10
	.p2align 3
.L283:
	movq	%r8, (%rax)
	addq	$8, %rax
	cmpq	%rax, %rdx
	jne	.L283
.L182:
	movl	$1, %r8d
	movl	%ebx, %ecx
.L181:
	testl	%ecx, %ecx
	jne	.L186
	cmpq	%rbp, %rsi
	je	.L318
	.p2align 4,,10
	.p2align 3
.L186:
	movq	%r8, %rax
	salq	%cl, %rax
	testb	%r12b, %r12b
	je	.L319
	orq	%rax, 0(%rbp)
	cmpl	$63, %ecx
	je	.L320
.L188:
	addl	$1, %ecx
	testl	%ecx, %ecx
	jne	.L186
	cmpq	%rbp, %rsi
	jne	.L186
.L318:
	movq	%rdx, %rax
	xorl	%ecx, %ecx
	movl	$1, %r8d
	.p2align 4,,10
	.p2align 3
.L249:
	cmpq	%rax, %rdx
	je	.L321
.L190:
	movq	%r8, %rsi
	salq	%cl, %rsi
	testb	%r12b, %r12b
	je	.L322
	orq	%rsi, (%rax)
	cmpl	$63, %ecx
	je	.L323
.L193:
	addl	$1, %ecx
	cmpq	%rax, %rdx
	jne	.L190
.L321:
	cmpl	%ecx, %r9d
	jne	.L190
.L195:
	cmpq	$0, 8(%rsp)
	js	.L201
	movq	24(%rsp), %rax
	movq	%rax, 16(%rdi)
.L202:
	movl	16(%rsp), %eax
	movl	%eax, 24(%rdi)
.L163:
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
	.p2align 4,,10
	.p2align 3
.L319:
	.cfi_restore_state
	notq	%rax
	andq	%rax, 0(%rbp)
	cmpl	$63, %ecx
	jne	.L188
.L320:
	addq	$8, %rbp
	xorl	%ecx, %ecx
	jmp	.L181
	.p2align 4,,10
	.p2align 3
.L165:
	movabsq	$9223372036854775744, %rcx
	movl	%r8d, 16(%rsp)
	movq	%r11, %r14
	movq	%rcx, %rax
	movq	%rsi, 8(%rsp)
	movq	%rdi, %r15
	subq	%rdx, %rax
	cmpq	%rax, %r11
	ja	.L324
	cmpq	%rdx, %r11
	movq	%rdx, %rax
	cmovnb	%r11, %rax
	addq	%rdx, %rax
	cmpq	%rcx, %rax
	ja	.L264
	cmpq	%rax, %rdx
	ja	.L264
	addq	$63, %rax
	shrq	$6, %rax
	salq	$3, %rax
	movq	%rax, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L204:
	movq	24(%rsp), %rdi
	call	_Znwm
	movq	8(%rsp), %rcx
	movq	%rax, %r13
	movq	(%r15), %rax
	subq	%rax, %rcx
	movq	%rax, 32(%rsp)
	movq	%rcx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L206
	movq	32(%rsp), %rsi
	movq	%rcx, %rdx
	movq	%r13, %rdi
	movq	%rcx, 40(%rsp)
	call	memmove
	movq	40(%rsp), %rcx
.L206:
	movl	%ebx, %r9d
	leaq	0(%r13,%rcx), %rdx
	testq	%r9, %r9
	je	.L265
	movq	8(%rsp), %r11
	movq	%r9, %rdi
	xorl	%eax, %eax
	xorl	%esi, %esi
	movl	$1, %r10d
	movq	%r9, 40(%rsp)
	jmp	.L214
	.p2align 4,,10
	.p2align 3
.L326:
	orq	%r8, (%rdx)
	cmpl	$63, %esi
	je	.L210
.L327:
	addl	$1, %esi
	cmpl	$63, %eax
	je	.L212
.L328:
	addl	$1, %eax
	subq	$1, %rdi
	je	.L325
.L214:
	movl	%eax, %ecx
	movq	%r10, %r8
	movq	%r10, %r9
	salq	%cl, %r8
	movl	%esi, %ecx
	salq	%cl, %r9
	testq	%r9, (%r11)
	jne	.L326
	notq	%r8
	andq	%r8, (%rdx)
	cmpl	$63, %esi
	jne	.L327
.L210:
	addq	$8, %r11
	xorl	%esi, %esi
	cmpl	$63, %eax
	jne	.L328
.L212:
	addq	$8, %rdx
	xorl	%eax, %eax
	subq	$1, %rdi
	jne	.L214
.L325:
	movq	40(%rsp), %r9
	movl	%eax, %r11d
.L207:
	addq	%r14, %r11
	leaq	63(%r11), %rcx
	testq	%r11, %r11
	cmovns	%r11, %rcx
	sarq	$6, %rcx
	leaq	(%rdx,%rcx,8), %rsi
	movq	%r11, %rcx
	sarq	$63, %rcx
	shrq	$58, %rcx
	movq	%rsi, %rdi
	addq	%rcx, %r11
	andl	$63, %r11d
	subq	%rcx, %r11
	testq	%r11, %r11
	movq	%r11, 40(%rsp)
	movq	%r11, %r10
	js	.L329
.L215:
	cmpq	%rdx, %rdi
	movl	$1, %r8d
	je	.L217
	movzbl	16(%rsp), %r8d
	leaq	8(%rdx), %r14
	movq	%r14, %rcx
	negl	%r8d
	cmpq	%r14, %rdi
	movslq	%r8d, %r8
	je	.L220
	.p2align 4,,10
	.p2align 3
.L284:
	movq	%r8, (%rcx)
	addq	$8, %rcx
	cmpq	%rcx, %rdi
	jne	.L284
.L220:
	movl	$1, %r8d
	movq	%rsi, 16(%rsp)
.L219:
	cmpq	%rdx, %r14
	jne	.L224
	testl	%eax, %eax
	je	.L330
	.p2align 4,,10
	.p2align 3
.L224:
	movl	%eax, %ecx
	movq	%r8, %rsi
	salq	%cl, %rsi
	testb	%r12b, %r12b
	movq	%rsi, %rcx
	je	.L331
	orq	%rcx, (%rdx)
	cmpl	$63, %eax
	je	.L332
.L226:
	addl	$1, %eax
	cmpq	%rdx, %r14
	jne	.L224
	testl	%eax, %eax
	jne	.L224
.L330:
	movq	16(%rsp), %rsi
	movq	%rdi, %rax
	xorl	%ecx, %ecx
	movl	$1, %edx
.L256:
	cmpq	%rax, %rdi
	je	.L333
.L228:
	movq	%rdx, %r8
	salq	%cl, %r8
	testb	%r12b, %r12b
	je	.L334
	orq	%r8, (%rax)
	cmpl	$63, %ecx
	je	.L335
.L231:
	addl	$1, %ecx
	cmpq	%rax, %rdi
	jne	.L228
.L333:
	cmpl	%ecx, %r10d
	jne	.L228
.L233:
	testq	%r11, %r11
	js	.L336
.L239:
	movq	16(%r15), %rdx
	movl	24(%r15), %ecx
	subq	8(%rsp), %rdx
	movl	40(%rsp), %eax
	leaq	(%rcx,%rdx,8), %rdx
	subq	%r9, %rdx
	testq	%rdx, %rdx
	jle	.L240
	movl	$1, %r8d
	jmp	.L247
	.p2align 4,,10
	.p2align 3
.L337:
	orq	%rdi, (%rsi)
	cmpl	$63, %ebx
	je	.L243
.L338:
	addl	$1, %ebx
	cmpl	$63, %eax
	je	.L245
.L339:
	addl	$1, %eax
	subq	$1, %rdx
	je	.L240
.L247:
	movl	%eax, %ecx
	movq	%r8, %rdi
	movq	%r8, %r10
	salq	%cl, %rdi
	movl	%ebx, %ecx
	salq	%cl, %r10
	testq	%r10, 0(%rbp)
	jne	.L337
	notq	%rdi
	andq	%rdi, (%rsi)
	cmpl	$63, %ebx
	jne	.L338
.L243:
	addq	$8, %rbp
	xorl	%ebx, %ebx
	cmpl	$63, %eax
	jne	.L339
.L245:
	addq	$8, %rsi
	xorl	%eax, %eax
	subq	$1, %rdx
	jne	.L247
.L240:
	movl	%eax, 24(%r15)
	movq	32(%rsp), %rax
	movq	%rsi, 16(%r15)
	testq	%rax, %rax
	je	.L248
	movq	%rax, %rdi
	call	_ZdlPv
.L248:
	movq	24(%rsp), %rax
	movq	%r13, (%r15)
	movl	$0, 8(%r15)
	addq	%r13, %rax
	movq	%rax, 32(%r15)
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
	.p2align 4,,10
	.p2align 3
.L322:
	.cfi_restore_state
	notq	%rsi
	andq	%rsi, (%rax)
	cmpl	$63, %ecx
	jne	.L193
.L323:
	addq	$8, %rax
	xorl	%ecx, %ecx
	jmp	.L249
	.p2align 4,,10
	.p2align 3
.L235:
	movl	%eax, %ecx
	movq	%r8, %r14
	salq	%cl, %r14
	testb	%r12b, %r12b
	movq	%r14, %rcx
	je	.L340
	orq	%rcx, (%rdx)
.L236:
	cmpl	$63, %eax
	je	.L341
	addl	$1, %eax
.L217:
	cmpl	%eax, %r10d
	jne	.L235
	cmpq	%rdx, %rdi
	jne	.L235
	jmp	.L233
	.p2align 4,,10
	.p2align 3
.L331:
	notq	%rcx
	andq	%rcx, (%rdx)
	cmpl	$63, %eax
	jne	.L226
.L332:
	addq	$8, %rdx
	xorl	%eax, %eax
	jmp	.L219
	.p2align 4,,10
	.p2align 3
.L334:
	notq	%r8
	andq	%r8, (%rax)
	cmpl	$63, %ecx
	jne	.L231
.L335:
	addq	$8, %rax
	xorl	%ecx, %ecx
	jmp	.L256
	.p2align 4,,10
	.p2align 3
.L201:
	movq	8(%rsp), %rax
	addq	$64, %rax
	movq	%rax, 16(%rsp)
	movq	24(%rsp), %rax
	subq	$8, %rax
	movq	%rax, 16(%rdi)
	jmp	.L202
	.p2align 4,,10
	.p2align 3
.L264:
	movabsq	$1152921504606846968, %rax
	movq	%rax, 24(%rsp)
	jmp	.L204
	.p2align 4,,10
	.p2align 3
.L311:
	addq	$64, %rdx
	leaq	-8(%r10), %r10
	jmp	.L166
	.p2align 4,,10
	.p2align 3
.L316:
	addq	$64, %r11
	subq	$8, %rdx
	jmp	.L169
	.p2align 4,,10
	.p2align 3
.L340:
	notq	%rcx
	andq	%rcx, (%rdx)
	jmp	.L236
	.p2align 4,,10
	.p2align 3
.L329:
	leaq	64(%r11), %r10
	leaq	-8(%rsi), %rdi
	jmp	.L215
	.p2align 4,,10
	.p2align 3
.L336:
	leaq	64(%r11), %rax
	subq	$8, %rsi
	movq	%rax, 40(%rsp)
	jmp	.L239
.L341:
	addq	$8, %rdx
	xorl	%eax, %eax
	jmp	.L217
.L317:
	movl	$1, %esi
	movl	%ebx, %ecx
.L179:
	cmpq	%rbp, %rdx
	jne	.L197
.L344:
	cmpl	%ecx, %r9d
	je	.L195
.L197:
	movq	%rsi, %rax
	salq	%cl, %rax
	testb	%r12b, %r12b
	je	.L342
	orq	%rax, 0(%rbp)
.L198:
	cmpl	$63, %ecx
	je	.L343
	addl	$1, %ecx
	cmpq	%rbp, %rdx
	je	.L344
	jmp	.L197
	.p2align 4,,10
	.p2align 3
.L342:
	notq	%rax
	andq	%rax, 0(%rbp)
	jmp	.L198
	.p2align 4,,10
	.p2align 3
.L343:
	addq	$8, %rbp
	xorl	%ecx, %ecx
	jmp	.L179
.L265:
	xorl	%r11d, %r11d
	xorl	%eax, %eax
	jmp	.L207
.L324:
	movl	$.LC11, %edi
	call	_ZSt20__throw_length_errorPKc
	.cfi_endproc
.LFE8312:
	.size	_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb, .-_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb
	.section	.text.unlikely._ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,"axG",@progbits,_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,comdat
.LCOLDE12:
	.section	.text._ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,"axG",@progbits,_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb,comdat
.LHOTE12:
	.section	.text.unlikely._ZNSt6vectorIbSaIbEE6resizeEmb,"axG",@progbits,_ZNSt6vectorIbSaIbEE6resizeEmb,comdat
	.align 2
.LCOLDB13:
	.section	.text._ZNSt6vectorIbSaIbEE6resizeEmb,"axG",@progbits,_ZNSt6vectorIbSaIbEE6resizeEmb,comdat
.LHOTB13:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIbSaIbEE6resizeEmb
	.type	_ZNSt6vectorIbSaIbEE6resizeEmb, @function
_ZNSt6vectorIbSaIbEE6resizeEmb:
.LFB8092:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	subq	$16, %rsp
	.cfi_def_cfa_offset 32
	movq	16(%rdi), %r10
	movl	24(%rdi), %r9d
	movq	(%rdi), %rcx
	movl	8(%rdi), %eax
	movq	%r10, %rbx
	subq	%rcx, %rbx
	movq	%r9, %r11
	leaq	(%r9,%rbx,8), %r9
	subq	%rax, %r9
	cmpq	%r9, %rsi
	jnb	.L346
	addq	%rax, %rsi
	leaq	63(%rsi), %rax
	testq	%rsi, %rsi
	cmovns	%rsi, %rax
	sarq	$6, %rax
	leaq	(%rcx,%rax,8), %rdx
	movq	%rsi, %rax
	sarq	$63, %rax
	shrq	$58, %rax
	addq	%rax, %rsi
	andl	$63, %esi
	subq	%rax, %rsi
	js	.L350
.L347:
	movq	%rdx, 16(%rdi)
	movl	%esi, 24(%rdi)
	addq	$16, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L350:
	.cfi_restore_state
	addq	$64, %rsi
	subq	$8, %rdx
	jmp	.L347
	.p2align 4,,10
	.p2align 3
.L346:
	movl	%r11d, 8(%rsp)
	movzbl	%dl, %r8d
	movq	8(%rsp), %rdx
	movq	%rsi, %rcx
	movq	%r10, %rsi
	subq	%r9, %rcx
	call	_ZNSt6vectorIbSaIbEE14_M_fill_insertESt13_Bit_iteratormb
	addq	$16, %rsp
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8092:
	.size	_ZNSt6vectorIbSaIbEE6resizeEmb, .-_ZNSt6vectorIbSaIbEE6resizeEmb
	.section	.text.unlikely._ZNSt6vectorIbSaIbEE6resizeEmb,"axG",@progbits,_ZNSt6vectorIbSaIbEE6resizeEmb,comdat
.LCOLDE13:
	.section	.text._ZNSt6vectorIbSaIbEE6resizeEmb,"axG",@progbits,_ZNSt6vectorIbSaIbEE6resizeEmb,comdat
.LHOTE13:
	.section	.rodata.str1.1
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
.LFB7974:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA7974
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	$8, %edx
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	$.LC14, %esi
	subq	$1056, %rsp
	.cfi_def_cfa_offset 1088
	leaq	528(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1048(%rsp)
	xorl	%eax, %eax
.LEHB0:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE0:
	leaq	16(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC15, %esi
.LEHB1:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE1:
	leaq	528(%rsp), %rdi
	movl	$N, %esi
.LEHB2:
	call	_ZNSirsERi
	movl	N(%rip), %eax
	movl	$edges, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm
	movl	N(%rip), %eax
	movl	$bcc, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm
	movl	N(%rip), %eax
	movl	$dfn, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIiSaIiEE6resizeEm
	movl	N(%rip), %eax
	movl	$par, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIiSaIiEE6resizeEm
	movl	N(%rip), %eax
	movl	$low, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIiSaIiEE6resizeEm
	movl	N(%rip), %eax
	xorl	%edx, %edx
	movl	$vis, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIbSaIbEE6resizeEmb
	movl	N(%rip), %edx
	xorl	%ebx, %ebx
	testl	%edx, %edx
	jle	.L359
	.p2align 4,,10
	.p2align 3
.L397:
	leaq	4(%rsp), %rsi
	leaq	528(%rsp), %rdi
	call	_ZNSirsERi
	jmp	.L354
	.p2align 4,,10
	.p2align 3
.L408:
	testq	%rax, %rax
	je	.L357
	movl	%edx, (%rax)
.L357:
	addq	$4, %rax
	movq	%rax, 8(%rdi)
.L354:
	leaq	8(%rsp), %rsi
	leaq	528(%rsp), %rdi
	call	_ZNSirsERi
	movl	8(%rsp), %edx
	testl	%edx, %edx
	je	.L355
	movslq	4(%rsp), %rax
	leaq	(%rax,%rax,2), %rcx
	movq	edges(%rip), %rax
	leaq	(%rax,%rcx,8), %rdi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	jne	.L408
	leaq	8(%rsp), %rsi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	jmp	.L354
	.p2align 4,,10
	.p2align 3
.L355:
	addl	$1, %ebx
	cmpl	%ebx, N(%rip)
	jg	.L397
.L359:
	xorl	%esi, %esi
	movl	$1, %edi
	call	_Z3dfsii
	xorl	%esi, %esi
	movl	$1, %edi
	call	_Z5colorii
	movl	cpiv(%rip), %eax
	movl	$ans, %edi
	leal	1(%rax), %esi
	movslq	%esi, %rsi
	call	_ZNSt6vectorIS_IiSaIiEESaIS1_EE6resizeEm
	movl	N(%rip), %eax
	movl	$1, 12(%rsp)
	movl	$1, %ecx
	movq	ans(%rip), %rsi
	movq	bcc(%rip), %r8
	testl	%eax, %eax
	jle	.L362
	.p2align 4,,10
	.p2align 3
.L390:
	movslq	%ecx, %rax
	leaq	(%rax,%rax,2), %rax
	leaq	(%r8,%rax,8), %rax
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	testl	%eax, %eax
	jle	.L363
	xorl	%ebx, %ebx
	jmp	.L367
	.p2align 4,,10
	.p2align 3
.L409:
	testq	%rax, %rax
	je	.L365
	movl	%ecx, (%rax)
.L365:
	addq	$4, %rax
	movq	%rax, 8(%rdi)
.L366:
	movslq	12(%rsp), %rax
	leal	1(%rbx), %edi
	addq	$1, %rbx
	movq	%rax, %rcx
	leaq	(%rax,%rax,2), %rax
	leaq	(%r8,%rax,8), %rax
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	subq	%rdx, %rax
	sarq	$2, %rax
	cmpl	%eax, %edi
	jge	.L363
.L367:
	movslq	(%rdx,%rbx,4), %rax
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %rdi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	jne	.L409
	leaq	12(%rsp), %rsi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	movq	ans(%rip), %rsi
	movq	bcc(%rip), %r8
	jmp	.L366
	.p2align 4,,10
	.p2align 3
.L363:
	addl	$1, %ecx
	cmpl	%ecx, N(%rip)
	movl	%ecx, 12(%rsp)
	jge	.L390
.L362:
	movq	ans+8(%rip), %rax
	movabsq	$-6148914691236517205, %rdx
	xorl	%ecx, %ecx
	xorl	%edi, %edi
	subq	%rsi, %rax
	sarq	$3, %rax
	imulq	%rdx, %rax
	leaq	8(%rsi), %rdx
	testl	%eax, %eax
	movl	%eax, %r8d
	jle	.L371
.L389:
	movq	(%rdx), %rax
	subq	-8(%rdx), %rax
	sarq	$2, %rax
	cmpl	%edi, %eax
	jle	.L373
	movslq	%ecx, %rbp
	movl	%eax, %edi
.L373:
	addl	$1, %ecx
	addq	$24, %rdx
	cmpl	%r8d, %ecx
	jne	.L389
	testl	%edi, %edi
	je	.L371
	leaq	0(%rbp,%rbp,2), %r12
	leal	-1(%rdi), %ebp
	xorl	%ebx, %ebx
	salq	$3, %r12
	salq	$2, %rbp
	jmp	.L376
	.p2align 4,,10
	.p2align 3
.L410:
	movq	ans(%rip), %rsi
	addq	$4, %rbx
.L376:
	movq	(%rsi,%r12), %rax
	leaq	16(%rsp), %rdi
	movl	(%rax,%rbx), %esi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC16, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	cmpq	%rbx, %rbp
	jne	.L410
.L371:
	leaq	16(%rsp), %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
.LEHE2:
	leaq	16(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	528(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1048(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L411
	addq	$1056, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L381:
	.cfi_restore_state
	movq	%rax, %rbx
.L378:
	leaq	528(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB3:
	call	_Unwind_Resume
.LEHE3:
.L382:
	leaq	16(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	jmp	.L378
.L411:
	call	__stack_chk_fail
	.cfi_endproc
.LFE7974:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA7974:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE7974-.LLSDACSB7974
.LLSDACSB7974:
	.uleb128 .LEHB0-.LFB7974
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB7974
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L381-.LFB7974
	.uleb128 0
	.uleb128 .LEHB2-.LFB7974
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L382-.LFB7974
	.uleb128 0
	.uleb128 .LEHB3-.LFB7974
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
.LLSDACSE7974:
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
	.type	_GLOBAL__sub_I_N, @function
_GLOBAL__sub_I_N:
.LFB8527:
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
	movl	$edges, %esi
	movl	$_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev, %edi
	movq	$0, edges(%rip)
	movq	$0, edges+8(%rip)
	movq	$0, edges+16(%rip)
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$bcc, %esi
	movl	$_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev, %edi
	movq	$0, bcc(%rip)
	movq	$0, bcc+8(%rip)
	movq	$0, bcc+16(%rip)
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$dfn, %esi
	movl	$_ZNSt6vectorIiSaIiEED1Ev, %edi
	movq	$0, dfn(%rip)
	movq	$0, dfn+8(%rip)
	movq	$0, dfn+16(%rip)
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$par, %esi
	movl	$_ZNSt6vectorIiSaIiEED1Ev, %edi
	movq	$0, par(%rip)
	movq	$0, par+8(%rip)
	movq	$0, par+16(%rip)
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$low, %esi
	movl	$_ZNSt6vectorIiSaIiEED1Ev, %edi
	movq	$0, low(%rip)
	movq	$0, low+8(%rip)
	movq	$0, low+16(%rip)
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$vis, %esi
	movl	$_ZNSt6vectorIbSaIbEED1Ev, %edi
	movq	$0, vis(%rip)
	movl	$0, vis+8(%rip)
	movq	$0, vis+16(%rip)
	movl	$0, vis+24(%rip)
	movq	$0, vis+32(%rip)
	call	__cxa_atexit
	movq	$0, ans(%rip)
	movq	$0, ans+8(%rip)
	movl	$__dso_handle, %edx
	movq	$0, ans+16(%rip)
	movl	$ans, %esi
	movl	$_ZNSt6vectorIS_IiSaIiEESaIS1_EED1Ev, %edi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE8527:
	.size	_GLOBAL__sub_I_N, .-_GLOBAL__sub_I_N
	.section	.text.unlikely
.LCOLDE18:
	.section	.text.startup
.LHOTE18:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_N
	.globl	cpiv
	.data
	.align 4
	.type	cpiv, @object
	.size	cpiv, 4
cpiv:
	.long	1
	.globl	piv
	.bss
	.align 4
	.type	piv, @object
	.size	piv, 4
piv:
	.zero	4
	.globl	ans
	.align 16
	.type	ans, @object
	.size	ans, 24
ans:
	.zero	24
	.globl	vis
	.align 32
	.type	vis, @object
	.size	vis, 40
vis:
	.zero	40
	.globl	low
	.align 16
	.type	low, @object
	.size	low, 24
low:
	.zero	24
	.globl	par
	.align 16
	.type	par, @object
	.size	par, 24
par:
	.zero	24
	.globl	dfn
	.align 16
	.type	dfn, @object
	.size	dfn, 24
dfn:
	.zero	24
	.globl	bcc
	.align 16
	.type	bcc, @object
	.size	bcc, 24
bcc:
	.zero	24
	.globl	edges
	.align 16
	.type	edges, @object
	.size	edges, 24
edges:
	.zero	24
	.globl	N
	.align 4
	.type	N, @object
	.size	N, 4
N:
	.zero	4
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
