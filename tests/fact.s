	.file	"fact.cpp"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB0:
	.text
.LHOTB0:
	.p2align 4,,15
	.globl	_Z4factx
	.type	_Z4factx, @function
_Z4factx:
.LFB1453:
	.cfi_startproc
	cmpq	$1, %rdi
	movl	$1, %eax
	je	.L4
	.p2align 4,,10
	.p2align 3
.L3:
	imulq	%rdi, %rax
	subq	$1, %rdi
	cmpq	$1, %rdi
	jne	.L3
	rep ret
.L4:
	rep ret
	.cfi_endproc
.LFE1453:
	.size	_Z4factx, .-_Z4factx
	.section	.text.unlikely
.LCOLDE0:
	.text
.LHOTE0:
	.section	.text.unlikely
.LCOLDB1:
	.text
.LHOTB1:
	.p2align 4,,15
	.globl	_Z3fibx
	.type	_Z3fibx, @function
_Z3fibx:
.LFB1454:
	.cfi_startproc
	cmpq	$1, %rdi
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
	jle	.L10
	movq	%rdi, %rbx
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L9:
	leaq	-1(%rbx), %rdi
	subq	$2, %rbx
	call	_Z3fibx
	addq	%rax, %rbp
	cmpq	$1, %rbx
	jg	.L9
	andl	$1, %r12d
.L8:
	leaq	(%r12,%rbp), %rax
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L10:
	.cfi_restore_state
	xorl	%ebp, %ebp
	jmp	.L8
	.cfi_endproc
.LFE1454:
	.size	_Z3fibx, .-_Z3fibx
	.section	.text.unlikely
.LCOLDE1:
	.text
.LHOTE1:
	.section	.text.unlikely
.LCOLDB2:
	.section	.text.startup,"ax",@progbits
.LHOTB2:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1455:
	.cfi_startproc
	movl	$24, %esi
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZSt4cout, %edi
	call	_ZNSo9_M_insertIxEERSoT_
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	movl	$16, %edx
	xorl	%esi, %esi
	.p2align 4,,10
	.p2align 3
.L14:
	movq	%rdx, %rdi
	call	_Z3fibx
	addq	%rax, %rsi
	subq	$2, %rdx
	jne	.L14
	addq	$1, %rsi
	movl	$_ZSt4cout, %edi
	call	_ZNSo9_M_insertIxEERSoT_
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1455:
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE2:
	.section	.text.startup
.LHOTE2:
	.section	.text.unlikely
.LCOLDB3:
	.section	.text.startup
.LHOTB3:
	.p2align 4,,15
	.type	_GLOBAL__sub_I__Z4factx, @function
_GLOBAL__sub_I__Z4factx:
.LFB1643:
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
.LFE1643:
	.size	_GLOBAL__sub_I__Z4factx, .-_GLOBAL__sub_I__Z4factx
	.section	.text.unlikely
.LCOLDE3:
	.section	.text.startup
.LHOTE3:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z4factx
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
