	.file	"4.cpp"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB0:
	.text
.LHOTB0:
	.p2align 4,,15
	.globl	_Zmld6triple
	.type	_Zmld6triple, @function
_Zmld6triple:
.LFB1805:
	.cfi_startproc
	movsd	24(%rsp), %xmm1
	movq	%rdi, %rax
	movsd	16(%rsp), %xmm2
	mulsd	%xmm0, %xmm1
	mulsd	%xmm0, %xmm2
	mulsd	8(%rsp), %xmm0
	movsd	%xmm1, 16(%rdi)
	movsd	%xmm2, 8(%rdi)
	movsd	%xmm0, (%rdi)
	ret
	.cfi_endproc
.LFE1805:
	.size	_Zmld6triple, .-_Zmld6triple
	.section	.text.unlikely
.LCOLDE0:
	.text
.LHOTE0:
	.section	.text.unlikely
.LCOLDB1:
	.text
.LHOTB1:
	.p2align 4,,15
	.globl	_Zpl6tripleS_
	.type	_Zpl6tripleS_, @function
_Zpl6tripleS_:
.LFB1806:
	.cfi_startproc
	movsd	24(%rsp), %xmm0
	movq	%rdi, %rax
	movsd	16(%rsp), %xmm1
	movsd	8(%rsp), %xmm2
	addsd	48(%rsp), %xmm0
	addsd	40(%rsp), %xmm1
	addsd	32(%rsp), %xmm2
	movsd	%xmm0, 16(%rdi)
	movsd	%xmm1, 8(%rdi)
	movsd	%xmm2, (%rdi)
	ret
	.cfi_endproc
.LFE1806:
	.size	_Zpl6tripleS_, .-_Zpl6tripleS_
	.section	.text.unlikely
.LCOLDE1:
	.text
.LHOTE1:
	.section	.text.unlikely
.LCOLDB2:
	.text
.LHOTB2:
	.p2align 4,,15
	.globl	_Z4dist6tripleS_
	.type	_Z4dist6tripleS_, @function
_Z4dist6tripleS_:
.LFB1807:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movsd	16(%rsp), %xmm2
	movsd	24(%rsp), %xmm0
	subsd	40(%rsp), %xmm2
	movsd	32(%rsp), %xmm1
	subsd	48(%rsp), %xmm0
	subsd	56(%rsp), %xmm1
	mulsd	%xmm2, %xmm2
	mulsd	%xmm0, %xmm0
	mulsd	%xmm1, %xmm1
	addsd	%xmm0, %xmm2
	addsd	%xmm2, %xmm1
	sqrtsd	%xmm1, %xmm0
	ucomisd	%xmm0, %xmm0
	jp	.L8
.L4:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	ret
.L8:
	.cfi_restore_state
	movapd	%xmm1, %xmm0
	call	sqrt
	jmp	.L4
	.cfi_endproc
.LFE1807:
	.size	_Z4dist6tripleS_, .-_Z4dist6tripleS_
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC5:
	.string	"connect.inp"
.LC6:
	.string	"connect.out"
	.section	.text.unlikely
.LCOLDB9:
	.section	.text.startup,"ax",@progbits
.LHOTB9:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1809:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1809
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movl	$8, %edx
	movl	$.LC5, %esi
	subq	$1288, %rsp
	.cfi_def_cfa_offset 1312
	leaq	752(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1272(%rsp)
	xorl	%eax, %eax
.LEHB0:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE0:
	leaq	240(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC6, %esi
.LEHB1:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE1:
	leaq	872(%rsp), %rdi
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	je	.L10
	leaq	192(%rsp), %rbx
	leaq	36(%rbx), %rbp
	.p2align 4,,10
	.p2align 3
.L11:
	leaq	752(%rsp), %rdi
	movq	%rbx, %rsi
.LEHB2:
	call	_ZNSirsERi
	addq	$4, %rbx
	cmpq	%rbp, %rbx
	jne	.L11
	pxor	%xmm1, %xmm1
	pxor	%xmm6, %xmm6
	pxor	%xmm5, %xmm5
	cvtsi2sd	192(%rsp), %xmm1
	movsd	%xmm1, 8(%rsp)
	pxor	%xmm1, %xmm1
	cvtsi2sd	204(%rsp), %xmm6
	movapd	%xmm6, %xmm7
	movsd	%xmm6, 120(%rsp)
	pxor	%xmm3, %xmm3
	cvtsi2sd	200(%rsp), %xmm5
	movsd	%xmm5, 24(%rsp)
	cvtsi2sd	196(%rsp), %xmm1
	movsd	%xmm1, 16(%rsp)
	pxor	%xmm1, %xmm1
	pxor	%xmm0, %xmm0
	cvtsi2sd	208(%rsp), %xmm3
	movapd	%xmm3, %xmm5
	movsd	%xmm3, 112(%rsp)
	cvtsi2sd	212(%rsp), %xmm1
	movapd	%xmm1, %xmm4
	movsd	.LC3(%rip), %xmm1
	cvtsi2sd	216(%rsp), %xmm0
	movsd	%xmm0, 128(%rsp)
	pxor	%xmm0, %xmm0
	movsd	%xmm1, 32(%rsp)
	pxor	%xmm1, %xmm1
	movsd	%xmm4, 104(%rsp)
	cvtsi2sd	220(%rsp), %xmm0
	movsd	%xmm0, 136(%rsp)
	pxor	%xmm0, %xmm0
	mulsd	%xmm1, %xmm7
	movsd	%xmm4, 80(%rsp)
	mulsd	%xmm1, %xmm5
	cvtsi2sd	224(%rsp), %xmm0
	movsd	%xmm0, 144(%rsp)
	movsd	%xmm7, 72(%rsp)
	movapd	%xmm4, %xmm7
	movsd	%xmm5, 64(%rsp)
	movapd	%xmm3, %xmm5
	mulsd	%xmm1, %xmm7
	movsd	%xmm5, 88(%rsp)
	movsd	%xmm7, 56(%rsp)
	movapd	%xmm6, %xmm7
	movsd	%xmm7, 96(%rsp)
	.p2align 4,,10
	.p2align 3
.L12:
	movsd	.LC3(%rip), %xmm0
	movsd	8(%rsp), %xmm2
	subsd	%xmm1, %xmm0
	movsd	16(%rsp), %xmm4
	movsd	%xmm1, 48(%rsp)
	mulsd	%xmm0, %xmm2
	mulsd	%xmm0, %xmm4
	mulsd	24(%rsp), %xmm0
	addsd	72(%rsp), %xmm2
	addsd	56(%rsp), %xmm0
	movsd	%xmm2, 160(%rsp)
	movsd	64(%rsp), %xmm2
	addsd	%xmm4, %xmm2
	movsd	%xmm0, 176(%rsp)
	movsd	%xmm2, 168(%rsp)
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1320
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1328
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1336
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1344
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1352
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1360
	call	_Z4dist6tripleS_
	movsd	%xmm0, 88(%rsp)
	movsd	.LC3(%rip), %xmm0
	movsd	56(%rsp), %xmm2
	subsd	80(%rsp), %xmm0
	mulsd	%xmm0, %xmm2
	addsd	144(%rsp), %xmm2
	movsd	%xmm2, 208(%rsp)
	movsd	64(%rsp), %xmm2
	mulsd	%xmm0, %xmm2
	mulsd	72(%rsp), %xmm0
	addsd	136(%rsp), %xmm2
	addsd	128(%rsp), %xmm0
	movsd	%xmm2, 216(%rsp)
	movsd	%xmm0, 224(%rsp)
	addq	$48, %rsp
	.cfi_def_cfa_offset 1312
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1320
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1328
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1336
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1344
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1352
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1360
	call	_Z4dist6tripleS_
	addq	$48, %rsp
	.cfi_def_cfa_offset 1312
	movsd	40(%rsp), %xmm3
	movsd	48(%rsp), %xmm1
	ucomisd	%xmm0, %xmm3
	jp	.L28
	je	.L39
	jbe	.L28
	movsd	32(%rsp), %xmm0
	movsd	120(%rsp), %xmm7
	subsd	%xmm1, %xmm0
	movsd	112(%rsp), %xmm5
	movsd	104(%rsp), %xmm4
	andpd	.LC8(%rip), %xmm0
	mulsd	.LC7(%rip), %xmm0
	addsd	%xmm0, %xmm1
	mulsd	%xmm1, %xmm7
	mulsd	%xmm1, %xmm5
	mulsd	%xmm1, %xmm4
	movsd	%xmm7, 72(%rsp)
	movsd	%xmm5, 64(%rsp)
	movsd	%xmm4, 56(%rsp)
	jmp	.L12
	.p2align 4,,10
	.p2align 3
.L28:
	ucomisd	%xmm3, %xmm0
	jbe	.L12
	movsd	32(%rsp), %xmm6
	movsd	112(%rsp), %xmm4
	movapd	%xmm6, %xmm0
	movsd	120(%rsp), %xmm7
	subsd	%xmm1, %xmm0
	andpd	.LC8(%rip), %xmm0
	mulsd	.LC7(%rip), %xmm0
	subsd	%xmm0, %xmm6
	mulsd	%xmm6, %xmm4
	movsd	%xmm6, 32(%rsp)
	mulsd	%xmm6, %xmm7
	movsd	%xmm4, 88(%rsp)
	movsd	104(%rsp), %xmm4
	movsd	%xmm7, 96(%rsp)
	mulsd	%xmm6, %xmm4
	movsd	%xmm4, 80(%rsp)
	jmp	.L12
	.p2align 4,,10
	.p2align 3
.L39:
	addsd	32(%rsp), %xmm1
	movsd	.LC3(%rip), %xmm0
	movsd	120(%rsp), %xmm3
	movsd	8(%rsp), %xmm2
	mulsd	.LC7(%rip), %xmm1
	subsd	%xmm1, %xmm0
	mulsd	%xmm1, %xmm3
	mulsd	%xmm0, %xmm2
	addsd	%xmm3, %xmm2
	movsd	112(%rsp), %xmm3
	mulsd	%xmm1, %xmm3
	mulsd	104(%rsp), %xmm1
	movsd	%xmm2, 160(%rsp)
	movsd	16(%rsp), %xmm2
	mulsd	%xmm0, %xmm2
	mulsd	24(%rsp), %xmm0
	addsd	%xmm3, %xmm2
	addsd	%xmm0, %xmm1
	movsd	%xmm2, 168(%rsp)
	movsd	%xmm1, 176(%rsp)
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1320
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1328
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1336
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1344
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1352
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1360
	call	_Z4dist6tripleS_
	addq	$48, %rsp
	.cfi_def_cfa_offset 1312
	call	ceil
	movl	$_ZSt4cout, %edi
	call	_ZNSo9_M_insertIdEERSoT_
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1320
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1328
	pushq	144(%rsp)
	.cfi_def_cfa_offset 1336
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1344
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1352
	pushq	200(%rsp)
	.cfi_def_cfa_offset 1360
	call	_Z4dist6tripleS_
	addq	$48, %rsp
	.cfi_def_cfa_offset 1312
	call	ceil
	leaq	240(%rsp), %rdi
	call	_ZNSo9_M_insertIdEERSoT_
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
.L10:
	leaq	752(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE5closeEv
	leaq	240(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE5closeEv
.LEHE2:
	leaq	240(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	752(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1272(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L40
	addq	$1288, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L40:
	.cfi_restore_state
	call	__stack_chk_fail
.L24:
	leaq	240(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L21:
	leaq	752(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB3:
	call	_Unwind_Resume
.LEHE3:
.L23:
	movq	%rax, %rbx
	jmp	.L21
	.cfi_endproc
.LFE1809:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA1809:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1809-.LLSDACSB1809
.LLSDACSB1809:
	.uleb128 .LEHB0-.LFB1809
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1809
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L23-.LFB1809
	.uleb128 0
	.uleb128 .LEHB2-.LFB1809
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L24-.LFB1809
	.uleb128 0
	.uleb128 .LEHB3-.LFB1809
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
.LLSDACSE1809:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE9:
	.section	.text.startup
.LHOTE9:
	.section	.text.unlikely
.LCOLDB10:
	.section	.text.startup
.LHOTB10:
	.p2align 4,,15
	.type	_GLOBAL__sub_I__Zmld6triple, @function
_GLOBAL__sub_I__Zmld6triple:
.LFB2070:
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
.LFE2070:
	.size	_GLOBAL__sub_I__Zmld6triple, .-_GLOBAL__sub_I__Zmld6triple
	.section	.text.unlikely
.LCOLDE10:
	.section	.text.startup
.LHOTE10:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Zmld6triple
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1072693248
	.align 8
.LC7:
	.long	0
	.long	1071644672
	.section	.rodata.cst16,"aM",@progbits,16
	.align 16
.LC8:
	.long	4294967295
	.long	2147483647
	.long	0
	.long	0
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
