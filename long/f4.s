	.file	"f4.cpp"
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
	.section	.text.unlikely._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED5Ev,comdat
	.align 2
.LCOLDB1:
	.section	.text._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED5Ev,comdat
.LHOTB1:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev
	.type	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev, @function
_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev:
.LFB9894:
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
	je	.L3
	movq	%rdi, %r12
	.p2align 4,,10
	.p2align 3
.L5:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L4
	call	_ZdlPv
.L4:
	addq	$24, %rbx
	cmpq	%rbx, %rbp
	jne	.L5
	movq	(%r12), %rbp
.L3:
	testq	%rbp, %rbp
	je	.L2
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
.L2:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9894:
	.size	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev, .-_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev
	.section	.text.unlikely._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED5Ev,comdat
.LCOLDE1:
	.section	.text._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED5Ev,comdat
.LHOTE1:
	.weak	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED1Ev
	.set	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED1Ev,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED2Ev
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.type	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103, @function
_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103:
.LFB10000:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA10000
	cmpq	%rdi, %rsi
	jbe	.L28
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movq	%rdi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rsi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdi, %rbx
	.p2align 4,,10
	.p2align 3
.L24:
	movl	$512, %edi
.LEHB0:
	call	_Znwm
.LEHE0:
	movq	%rax, (%rbx)
	addq	$8, %rbx
	cmpq	%rbx, %rbp
	ja	.L24
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L28:
	rep ret
.L23:
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	.cfi_offset 6, -24
	.cfi_offset 12, -16
	movq	%rax, %rdi
	call	__cxa_begin_catch
	cmpq	%rbx, %r12
	jnb	.L19
.L25:
	movq	(%r12), %rdi
	addq	$8, %r12
	call	_ZdlPv
	cmpq	%rbx, %r12
	jb	.L25
.L19:
.LEHB1:
	call	__cxa_rethrow
.LEHE1:
.L22:
	movq	%rax, %rbx
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
	.cfi_endproc
.LFE10000:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
	.align 4
.LLSDA10000:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT10000-.LLSDATTD10000
.LLSDATTD10000:
	.byte	0x1
	.uleb128 .LLSDACSE10000-.LLSDACSB10000
.LLSDACSB10000:
	.uleb128 .LEHB0-.LFB10000
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L23-.LFB10000
	.uleb128 0x1
	.uleb128 .LEHB1-.LFB10000
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L22-.LFB10000
	.uleb128 0
	.uleb128 .LEHB2-.LFB10000
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE10000:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT10000:
	.text
	.size	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103, .-_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.set	_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.84,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103
	.section	.text.unlikely
.LCOLDB3:
	.text
.LHOTB3:
	.p2align 4,,15
	.globl	_Z17getElementbyStacki
	.type	_Z17getElementbyStacki, @function
_Z17getElementbyStacki:
.LFB8680:
	.cfi_startproc
	movq	fdata+24(%rip), %rax
	movl	$-1, %edx
	cmpq	$fdata+8, %rax
	je	.L40
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	cmpl	48(%rax), %edi
	movl	%edi, %ebx
	jne	.L34
	jmp	.L32
	.p2align 4,,10
	.p2align 3
.L35:
	cmpl	%ebx, 48(%rax)
	je	.L32
.L34:
	movq	%rax, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpq	$fdata+8, %rax
	jne	.L35
	movl	$-1, %edx
	movl	%edx, %eax
	popq	%rbx
	.cfi_remember_state
	.cfi_restore 3
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L32:
	.cfi_restore_state
	movl	32(%rax), %edx
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 8
	movl	%edx, %eax
	ret
.L40:
	movl	%edx, %eax
	ret
	.cfi_endproc
.LFE8680:
	.size	_Z17getElementbyStacki, .-_Z17getElementbyStacki
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.text.unlikely
.LCOLDB4:
	.text
.LHOTB4:
	.p2align 4,,15
	.globl	_Z5judgeRSt6vectorIiSaIiEES2_
	.type	_Z5judgeRSt6vectorIiSaIiEES2_, @function
_Z5judgeRSt6vectorIiSaIiEES2_:
.LFB8697:
	.cfi_startproc
	movq	(%rdi), %r8
	movq	8(%rdi), %rcx
	subq	%r8, %rcx
	sarq	$2, %rcx
	testq	%rcx, %rcx
	je	.L46
	movq	(%rsi), %rsi
	movl	(%rsi), %eax
	cmpl	%eax, (%r8)
	jg	.L48
	movl	$0, %edx
	je	.L49
	jmp	.L46
	.p2align 4,,10
	.p2align 3
.L45:
	movl	(%rsi,%rax,4), %edi
	cmpl	%edi, (%r8,%rax,4)
	jg	.L48
	jne	.L46
.L49:
	leal	1(%rdx), %eax
	cmpq	%rcx, %rax
	movq	%rax, %rdx
	jb	.L45
.L46:
	movl	$1, %eax
	ret
	.p2align 4,,10
	.p2align 3
.L48:
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE8697:
	.size	_Z5judgeRSt6vectorIiSaIiEES2_, .-_Z5judgeRSt6vectorIiSaIiEES2_
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC5:
	.string	"food.out"
	.section	.text.unlikely
.LCOLDB6:
	.text
.LHOTB6:
	.p2align 4,,15
	.globl	_Z9print_resRSt6vectorIiSaIiEE
	.type	_Z9print_resRSt6vectorIiSaIiEE, @function
_Z9print_resRSt6vectorIiSaIiEE:
.LFB8698:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8698
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
	movq	%rdi, %rbp
	subq	$552, %rsp
	.cfi_def_cfa_offset 592
	leaq	264(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 536(%rsp)
	xorl	%eax, %eax
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+8(%rip), %r12
	movb	$0, 488(%rsp)
	leaq	16(%rsp), %rdi
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+16(%rip), %r13
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 264(%rsp)
	xorl	%esi, %esi
	movq	$0, 480(%rsp)
	movb	$0, 489(%rsp)
	addq	-24(%r12), %rdi
	movq	$0, 496(%rsp)
	movq	$0, 504(%rsp)
	movq	$0, 512(%rsp)
	movq	$0, 520(%rsp)
	movq	%r12, 16(%rsp)
	movq	%r13, (%rdi)
.LEHB3:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE3:
	leaq	16(%rsp), %rax
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 16(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 264(%rsp)
	leaq	8(%rax), %rdi
.LEHB4:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE4:
	leaq	16(%rsp), %rax
	leaq	24(%rsp), %rsi
	leaq	248(%rax), %rdi
.LEHB5:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	16(%rsp), %rax
	movl	$48, %edx
	movl	$.LC5, %esi
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	16(%rsp), %rdi
	movq	16(%rsp), %rax
	je	.L75
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE5:
.L53:
	movq	0(%rbp), %rbx
	cmpq	8(%rbp), %rbx
	je	.L60
	.p2align 4,,10
	.p2align 3
.L69:
	movl	(%rbx), %esi
	leaq	16(%rsp), %rdi
.LEHB6:
	call	_ZNSolsEi
	leaq	15(%rsp), %rsi
	movl	$1, %edx
	movq	%rax, %rdi
	movb	$32, 15(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	addq	$4, %rbx
	cmpq	%rbx, 8(%rbp)
	jne	.L69
.L60:
	leaq	16(%rsp), %rax
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE6:
	testq	%rax, %rax
	je	.L76
.L62:
	leaq	24(%rsp), %rdi
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 16(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 264(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 24(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	128(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	80(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 24(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r12), %rax
	leaq	264(%rsp), %rdi
	movq	%r13, 16(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 264(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	536(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L77
	addq	$552, %rsp
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
.L75:
	.cfi_restore_state
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB7:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE7:
	jmp	.L53
.L76:
	movq	16(%rsp), %rax
	leaq	16(%rsp), %rdi
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB8:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE8:
	jmp	.L62
.L65:
	leaq	16(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB9:
	call	_Unwind_Resume
.L68:
	leaq	24(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rax
.L55:
	movq	-24(%r12), %rdx
	movq	%rax, %rbx
	movq	%r13, 16(%rsp,%rdx)
.L56:
	leaq	264(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 264(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE9:
.L67:
	jmp	.L55
.L66:
	movq	%rax, %rbx
	jmp	.L56
.L77:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8698:
	.section	.gcc_except_table
.LLSDA8698:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8698-.LLSDACSB8698
.LLSDACSB8698:
	.uleb128 .LEHB3-.LFB8698
	.uleb128 .LEHE3-.LEHB3
	.uleb128 .L66-.LFB8698
	.uleb128 0
	.uleb128 .LEHB4-.LFB8698
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L67-.LFB8698
	.uleb128 0
	.uleb128 .LEHB5-.LFB8698
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L68-.LFB8698
	.uleb128 0
	.uleb128 .LEHB6-.LFB8698
	.uleb128 .LEHE6-.LEHB6
	.uleb128 .L65-.LFB8698
	.uleb128 0
	.uleb128 .LEHB7-.LFB8698
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L68-.LFB8698
	.uleb128 0
	.uleb128 .LEHB8-.LFB8698
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L65-.LFB8698
	.uleb128 0
	.uleb128 .LEHB9-.LFB8698
	.uleb128 .LEHE9-.LEHB9
	.uleb128 0
	.uleb128 0
.LLSDACSE8698:
	.text
	.size	_Z9print_resRSt6vectorIiSaIiEE, .-_Z9print_resRSt6vectorIiSaIiEE
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely
.LCOLDB7:
	.text
.LHOTB7:
	.p2align 4,,15
	.globl	_Z14print_subgraphRSt6vectorISt4pairIiiESaIS1_EE
	.type	_Z14print_subgraphRSt6vectorISt4pairIiiESaIS1_EE, @function
_Z14print_subgraphRSt6vectorISt4pairIiiESaIS1_EE:
.LFB8699:
	.cfi_startproc
	rep ret
	.cfi_endproc
.LFE8699:
	.size	_Z14print_subgraphRSt6vectorISt4pairIiiESaIS1_EE, .-_Z14print_subgraphRSt6vectorISt4pairIiiESaIS1_EE
	.section	.text.unlikely
.LCOLDE7:
	.text
.LHOTE7:
	.section	.rodata.str1.1
.LC8:
	.string	"):"
	.section	.text.unlikely
.LCOLDB9:
	.text
.LHOTB9:
	.p2align 4,,15
	.globl	_Z8print_rpv
	.type	_Z8print_rpv, @function
_Z8print_rpv:
.LFB8700:
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
	movq	fdata+24(%rip), %rbx
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	cmpq	$fdata+8, %rbx
	jne	.L95
	jmp	.L87
	.p2align 4,,10
	.p2align 3
.L102:
	movsbl	67(%rbp), %esi
.L85:
	movq	%r12, %rdi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpq	$fdata+8, %rax
	movq	%rax, %rbx
	je	.L87
.L95:
	movl	32(%rbx), %ebp
	leaq	7(%rsp), %rsi
	movl	$1, %edx
	movl	$_ZSt4cout, %edi
	movb	$40, 7(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%ebp, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi
	movl	$2, %edx
	movl	$.LC8, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	44(%rbx), %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movq	%rax, %r12
	movq	(%rax), %rax
	movq	-24(%rax), %rax
	movq	240(%r12,%rax), %rbp
	testq	%rbp, %rbp
	je	.L81
	cmpb	$0, 56(%rbp)
	jne	.L102
	movq	%rbp, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L85
	movq	%rbp, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L85
	.p2align 4,,10
	.p2align 3
.L87:
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbx
	testq	%rbx, %rbx
	je	.L81
	cmpb	$0, 56(%rbx)
	je	.L88
	movsbl	67(%rbx), %esi
.L89:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L103
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
	.p2align 4,,10
	.p2align 3
.L88:
	.cfi_restore_state
	movq	%rbx, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%rbx), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L89
	movq	%rbx, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L89
.L81:
	call	_ZSt16__throw_bad_castv
.L103:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8700:
	.size	_Z8print_rpv, .-_Z8print_rpv
	.section	.text.unlikely
.LCOLDE9:
	.text
.LHOTE9:
	.section	.text.unlikely
.LCOLDB10:
	.text
.LHOTB10:
	.p2align 4,,15
	.globl	_Z12print_vectorRSt6vectorIiSaIiEE
	.type	_Z12print_vectorRSt6vectorIiSaIiEE, @function
_Z12print_vectorRSt6vectorIiSaIiEE:
.LFB8701:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$24, %rsp
	.cfi_def_cfa_offset 48
	movq	8(%rdi), %rbp
	movq	(%rdi), %rbx
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	cmpq	%rbp, %rbx
	je	.L109
	.p2align 4,,10
	.p2align 3
.L114:
	movl	(%rbx), %esi
	movl	$_ZSt4cout, %edi
	addq	$4, %rbx
	call	_ZNSolsEi
	leaq	7(%rsp), %rsi
	movl	$1, %edx
	movq	%rax, %rdi
	movb	$32, 7(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	cmpq	%rbx, %rbp
	jne	.L114
.L109:
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbx
	testq	%rbx, %rbx
	je	.L120
	cmpb	$0, 56(%rbx)
	je	.L110
	movsbl	67(%rbx), %esi
.L111:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L121
	addq	$24, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L110:
	.cfi_restore_state
	movq	%rbx, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%rbx), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L111
	movq	%rbx, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L111
.L121:
	call	__stack_chk_fail
.L120:
	call	_ZSt16__throw_bad_castv
	.cfi_endproc
.LFE8701:
	.size	_Z12print_vectorRSt6vectorIiSaIiEE, .-_Z12print_vectorRSt6vectorIiSaIiEE
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.section	.rodata.str1.1
.LC11:
	.string	"\n --- print edgeStack --- "
.LC12:
	.string	", "
.LC13:
	.string	")"
	.section	.text.unlikely
.LCOLDB14:
	.text
.LHOTB14:
	.p2align 4,,15
	.globl	_Z10print_edgeSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEE
	.type	_Z10print_edgeSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEE, @function
_Z10print_edgeSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEE:
.LFB8702:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	$26, %edx
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	$.LC11, %esi
	movq	%rdi, %rbx
	movl	$_ZSt4cout, %edi
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbp
	testq	%rbp, %rbp
	je	.L128
	cmpb	$0, 56(%rbp)
	je	.L124
	movsbl	67(%rbp), %esi
.L125:
	movl	$_ZSt4cout, %edi
	jmp	.L145
	.p2align 4,,10
	.p2align 3
.L147:
	movsbl	67(%r12), %esi
.L130:
	movq	%rbp, %rdi
.L145:
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
	movq	48(%rbx), %rdi
	cmpq	16(%rbx), %rdi
	je	.L122
	cmpq	%rdi, 56(%rbx)
	je	.L146
	movl	-8(%rdi), %ebp
	movl	-4(%rdi), %r12d
	subq	$8, %rdi
	movq	%rdi, 48(%rbx)
.L133:
	leaq	7(%rsp), %rsi
	movl	$1, %edx
	movl	$_ZSt4cout, %edi
	movb	$40, 7(%rsp)
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%ebp, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi
	movl	$2, %edx
	movq	%rax, %rbp
	movl	$.LC12, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%r12d, %esi
	movq	%rbp, %rdi
	call	_ZNSolsEi
	movl	$1, %edx
	movq	%rax, %rbp
	movl	$.LC13, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	0(%rbp), %rax
	movq	-24(%rax), %rax
	movq	240(%rbp,%rax), %r12
	testq	%r12, %r12
	je	.L128
	cmpb	$0, 56(%r12)
	jne	.L147
	movq	%r12, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%r12), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L130
	movq	%r12, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L130
	.p2align 4,,10
	.p2align 3
.L146:
	movq	72(%rbx), %rax
	movq	-8(%rax), %rax
	movl	504(%rax), %ebp
	movl	508(%rax), %r12d
	call	_ZdlPv
	movq	72(%rbx), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 72(%rbx)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 56(%rbx)
	addq	$504, %rax
	movq	%rax, 48(%rbx)
	movq	%rdx, 64(%rbx)
	jmp	.L133
	.p2align 4,,10
	.p2align 3
.L122:
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L148
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
	.p2align 4,,10
	.p2align 3
.L124:
	.cfi_restore_state
	movq	%rbp, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L125
	movq	%rbp, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L125
.L128:
	call	_ZSt16__throw_bad_castv
.L148:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8702:
	.size	_Z10print_edgeSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEE, .-_Z10print_edgeSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEE
	.section	.text.unlikely
.LCOLDE14:
	.text
.LHOTE14:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
	.align 2
.LCOLDB15:
	.section	.text._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LHOTB15:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEEaSERKS1_
	.type	_ZNSt6vectorIiSaIiEEaSERKS1_, @function
_ZNSt6vectorIiSaIiEEaSERKS1_:
.LFB8907:
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
	je	.L150
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
	ja	.L173
	movq	8(%rdi), %rdi
	movq	%rdi, %rax
	subq	%r13, %rax
	movq	%rax, %rcx
	sarq	$2, %rcx
	cmpq	%rcx, %r14
	jbe	.L174
	testq	%rcx, %rcx
	jne	.L175
.L160:
	leaq	(%r15,%rax), %rsi
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	testq	%rax, %rax
	jne	.L161
.L172:
	addq	%r13, %rbp
.L157:
	movq	%rbp, 8(%rbx)
.L150:
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
.L174:
	.cfi_restore_state
	testq	%r14, %r14
	je	.L172
	movq	%rbp, %rdx
	movq	%r15, %rsi
	movq	%r13, %rdi
	call	memmove
	addq	(%rbx), %rbp
	jmp	.L157
	.p2align 4,,10
	.p2align 3
.L173:
	xorl	%r12d, %r12d
	testq	%r14, %r14
	je	.L155
	movabsq	$4611686018427387903, %rax
	cmpq	%rax, %r14
	ja	.L176
	movq	%rbp, %rdi
	call	_Znwm
	testq	%r14, %r14
	movq	%rax, %r12
	movq	(%rbx), %r13
	jne	.L177
.L155:
	testq	%r13, %r13
	je	.L156
.L178:
	movq	%r13, %rdi
	call	_ZdlPv
.L156:
	addq	%r12, %rbp
	movq	%r12, (%rbx)
	movq	%rbp, 16(%rbx)
	jmp	.L157
	.p2align 4,,10
	.p2align 3
.L177:
	movq	%rbp, %rdx
	movq	%r15, %rsi
	movq	%rax, %rdi
	call	memmove
	testq	%r13, %r13
	jne	.L178
	jmp	.L156
	.p2align 4,,10
	.p2align 3
.L161:
	call	memmove
	addq	(%rbx), %rbp
	jmp	.L157
	.p2align 4,,10
	.p2align 3
.L175:
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
	jmp	.L160
.L176:
	call	_ZSt17__throw_bad_allocv
	.cfi_endproc
.LFE8907:
	.size	_ZNSt6vectorIiSaIiEEaSERKS1_, .-_ZNSt6vectorIiSaIiEEaSERKS1_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LCOLDE15:
	.section	.text._ZNSt6vectorIiSaIiEEaSERKS1_,"axG",@progbits,_ZNSt6vectorIiSaIiEEaSERKS1_,comdat
.LHOTE15:
	.section	.text.unlikely._ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED5Ev,comdat
	.align 2
.LCOLDB16:
	.section	.text._ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED5Ev,comdat
.LHOTB16:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	.type	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev, @function
_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev:
.LFB9018:
	.cfi_startproc
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
	movq	(%rdi), %rdi
	testq	%rdi, %rdi
	je	.L179
	movq	72(%r12), %rax
	movq	40(%r12), %rbx
	leaq	8(%rax), %rbp
	cmpq	%rbx, %rbp
	jbe	.L181
	.p2align 4,,10
	.p2align 3
.L182:
	movq	(%rbx), %rdi
	addq	$8, %rbx
	call	_ZdlPv
	cmpq	%rbx, %rbp
	ja	.L182
	movq	(%r12), %rdi
.L181:
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L179:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9018:
	.size	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev, .-_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED5Ev,comdat
.LCOLDE16:
	.section	.text._ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED5Ev,comdat
.LHOTE16:
	.weak	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED1Ev
	.set	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED1Ev,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	.section	.text.unlikely._ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev,"axG",@progbits,_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED5Ev,comdat
	.align 2
.LCOLDB17:
	.section	.text._ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev,"axG",@progbits,_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED5Ev,comdat
.LHOTB17:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev
	.type	_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev, @function
_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev:
.LFB9885:
	.cfi_startproc
	jmp	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	.cfi_endproc
.LFE9885:
	.size	_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev, .-_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev
	.section	.text.unlikely._ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev,"axG",@progbits,_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED5Ev,comdat
.LCOLDE17:
	.section	.text._ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev,"axG",@progbits,_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED5Ev,comdat
.LHOTE17:
	.weak	_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED1Ev
	.set	_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED1Ev,_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
	.align 2
.LCOLDB18:
	.section	.text._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LHOTB18:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIiSaIiEED2Ev
	.type	_ZNSt11_Deque_baseIiSaIiEED2Ev, @function
_ZNSt11_Deque_baseIiSaIiEED2Ev:
.LFB9037:
	.cfi_startproc
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
	movq	(%rdi), %rdi
	testq	%rdi, %rdi
	je	.L186
	movq	72(%r12), %rax
	movq	40(%r12), %rbx
	leaq	8(%rax), %rbp
	cmpq	%rbx, %rbp
	jbe	.L188
	.p2align 4,,10
	.p2align 3
.L189:
	movq	(%rbx), %rdi
	addq	$8, %rbx
	call	_ZdlPv
	cmpq	%rbx, %rbp
	ja	.L189
	movq	(%r12), %rdi
.L188:
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L186:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9037:
	.size	_ZNSt11_Deque_baseIiSaIiEED2Ev, .-_ZNSt11_Deque_baseIiSaIiEED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LCOLDE18:
	.section	.text._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LHOTE18:
	.weak	_ZNSt11_Deque_baseIiSaIiEED1Ev
	.set	_ZNSt11_Deque_baseIiSaIiEED1Ev,_ZNSt11_Deque_baseIiSaIiEED2Ev
	.section	.text.unlikely._ZNSt5stackIiSt5dequeIiSaIiEEED2Ev,"axG",@progbits,_ZNSt5stackIiSt5dequeIiSaIiEEED5Ev,comdat
	.align 2
.LCOLDB19:
	.section	.text._ZNSt5stackIiSt5dequeIiSaIiEEED2Ev,"axG",@progbits,_ZNSt5stackIiSt5dequeIiSaIiEEED5Ev,comdat
.LHOTB19:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev
	.type	_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev, @function
_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev:
.LFB9888:
	.cfi_startproc
	jmp	_ZNSt11_Deque_baseIiSaIiEED2Ev
	.cfi_endproc
.LFE9888:
	.size	_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev, .-_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev
	.section	.text.unlikely._ZNSt5stackIiSt5dequeIiSaIiEEED2Ev,"axG",@progbits,_ZNSt5stackIiSt5dequeIiSaIiEEED5Ev,comdat
.LCOLDE19:
	.section	.text._ZNSt5stackIiSt5dequeIiSaIiEEED2Ev,"axG",@progbits,_ZNSt5stackIiSt5dequeIiSaIiEEED5Ev,comdat
.LHOTE19:
	.weak	_ZNSt5stackIiSt5dequeIiSaIiEEED1Ev
	.set	_ZNSt5stackIiSt5dequeIiSaIiEEED1Ev,_ZNSt5stackIiSt5dequeIiSaIiEEED2Ev
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
	.align 2
.LCOLDB20:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTB20:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_:
.LFB9084:
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
	je	.L201
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L213
.L202:
	movq	$-4, %r13
	jmp	.L194
	.p2align 4,,10
	.p2align 3
.L201:
	movl	$4, %r13d
.L194:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L200:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movl	(%r12), %ecx
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	addq	%rdx, %r12
	je	.L196
	movl	%ecx, (%r12)
.L196:
	testq	%rax, %rax
	jne	.L214
	addq	$4, %r12
	testq	%r14, %r14
	je	.L199
.L198:
	movq	%r14, %rdi
	call	_ZdlPv
.L199:
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
.L214:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$4, %r12
	call	memmove
	jmp	.L198
.L213:
	movabsq	$4611686018427387903, %rcx
	cmpq	%rcx, %rdx
	ja	.L202
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L200
	leaq	0(,%rax,8), %r13
	jmp	.L194
	.cfi_endproc
.LFE9084:
	.size	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LCOLDE20:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_,comdat
.LHOTE20:
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIRKiEEEvDpOT_,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB21:
	.section	.text._ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTB21:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.type	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, @function
_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_:
.LFB9139:
	.cfi_startproc
	pushq	%r14
	.cfi_def_cfa_offset 16
	.cfi_offset 14, -16
	pushq	%r13
	.cfi_def_cfa_offset 24
	.cfi_offset 13, -24
	movq	%rsi, %r14
	pushq	%r12
	.cfi_def_cfa_offset 32
	.cfi_offset 12, -32
	pushq	%rbp
	.cfi_def_cfa_offset 40
	.cfi_offset 6, -40
	movq	%rdi, %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movq	8(%rbp), %r8
	movq	(%rdi), %rdi
	movq	%r8, %rdx
	subq	%rdi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L224
	leaq	(%rax,%rax), %rcx
	cmpq	%rcx, %rax
	jbe	.L239
.L225:
	movq	$-8, %rbx
.L216:
	movq	%rbx, %rdi
	call	_Znwm
	movq	8(%rbp), %r8
	movq	0(%rbp), %rdi
	leaq	8(%rax), %r12
	movq	%rax, %r13
	addq	%rax, %rbx
	movq	%r8, %rdx
	subq	%rdi, %rdx
.L223:
	addq	%r13, %rdx
	je	.L218
	movq	(%r14), %rax
	movq	%rax, (%rdx)
.L218:
	cmpq	%rdi, %r8
	je	.L219
	movq	%rdi, %rdx
	movq	%r13, %rcx
	.p2align 4,,10
	.p2align 3
.L221:
	testq	%rcx, %rcx
	je	.L220
	movq	(%rdx), %rsi
	movq	%rsi, (%rcx)
.L220:
	addq	$8, %rdx
	addq	$8, %rcx
	cmpq	%r8, %rdx
	jne	.L221
	leaq	8(%rdi), %rax
	subq	%rax, %rdx
	shrq	$3, %rdx
	leaq	16(%r13,%rdx,8), %r12
.L219:
	testq	%rdi, %rdi
	je	.L222
	call	_ZdlPv
.L222:
	movq	%r13, 0(%rbp)
	movq	%r12, 8(%rbp)
	movq	%rbx, 16(%rbp)
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
.L224:
	.cfi_restore_state
	movl	$8, %ebx
	jmp	.L216
.L239:
	movabsq	$2305843009213693951, %rsi
	cmpq	%rsi, %rcx
	ja	.L225
	testq	%rcx, %rcx
	jne	.L240
	movl	$8, %r12d
	xorl	%ebx, %ebx
	xorl	%r13d, %r13d
	jmp	.L223
.L240:
	salq	$4, %rax
	movq	%rax, %rbx
	jmp	.L216
	.cfi_endproc
.LFE9139:
	.size	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, .-_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LCOLDE21:
	.section	.text._ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTE21:
	.weak	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_
	.set	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_,_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,comdat
	.align 2
.LCOLDB22:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,comdat
.LHOTB22:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E
	.type	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E, @function
_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E:
.LFB9159:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L255
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
.L250:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E
	movq	40(%rbx), %rdi
	movq	16(%rbx), %rbp
	testq	%rdi, %rdi
	je	.L243
	call	_ZdlPv
.L243:
	movq	%rbx, %rdi
	movq	%rbp, %rbx
	call	_ZdlPv
	testq	%rbp, %rbp
	jne	.L250
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L255:
	rep ret
	.cfi_endproc
.LFE9159:
	.size	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E, .-_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,comdat
.LCOLDE22:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E,comdat
.LHOTE22:
	.section	.text.unlikely._ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,comdat
	.align 2
.LCOLDB23:
	.section	.text._ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,comdat
.LHOTB23:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm
	.type	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm, @function
_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm:
.LFB9253:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA9253
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	$8, %eax
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbx
	movq	%rsi, %rdi
	movq	%rsi, %rbp
	shrq	$6, %rdi
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	leaq	1(%rdi), %r13
	addq	$3, %rdi
	cmpq	$8, %rdi
	cmovb	%rax, %rdi
	movq	%rdi, 8(%rbx)
	salq	$3, %rdi
.LEHB10:
	call	_Znwm
.LEHE10:
	movq	8(%rbx), %rdx
	movq	%rax, (%rbx)
	subq	%r13, %rdx
	shrq	%rdx
	leaq	(%rax,%rdx,8), %r12
	leaq	(%r12,%r13,8), %r13
	movq	%r12, %rdi
	movq	%r13, %rsi
.LEHB11:
	call	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE15_M_create_nodesEPPS1_S5_.isra.103
.LEHE11:
	movq	(%r12), %rdx
	andl	$63, %ebp
	movq	%r12, 40(%rbx)
	leaq	512(%rdx), %rax
	movq	%rdx, 24(%rbx)
	movq	%rdx, 16(%rbx)
	movq	%rax, 32(%rbx)
	leaq	-8(%r13), %rax
	movq	%rax, 72(%rbx)
	movq	-8(%r13), %rax
	movq	%rax, 56(%rbx)
	leaq	512(%rax), %rcx
	leaq	(%rax,%rbp,8), %rax
	movq	%rcx, 64(%rbx)
	movq	%rax, 48(%rbx)
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
.L259:
	.cfi_restore_state
.L257:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	$0, (%rbx)
	movq	$0, 8(%rbx)
.LEHB12:
	call	__cxa_rethrow
.LEHE12:
.L260:
	movq	%rax, %rbx
.L258:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB13:
	call	_Unwind_Resume
.LEHE13:
	.cfi_endproc
.LFE9253:
	.section	.gcc_except_table
	.align 4
.LLSDA9253:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT9253-.LLSDATTD9253
.LLSDATTD9253:
	.byte	0x1
	.uleb128 .LLSDACSE9253-.LLSDACSB9253
.LLSDACSB9253:
	.uleb128 .LEHB10-.LFB9253
	.uleb128 .LEHE10-.LEHB10
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB11-.LFB9253
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L259-.LFB9253
	.uleb128 0x1
	.uleb128 .LEHB12-.LFB9253
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L260-.LFB9253
	.uleb128 0
	.uleb128 .LEHB13-.LFB9253
	.uleb128 .LEHE13-.LEHB13
	.uleb128 0
	.uleb128 0
.LLSDACSE9253:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT9253:
	.section	.text._ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,comdat
	.size	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm, .-_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm
	.section	.text.unlikely._ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,comdat
.LCOLDE23:
	.section	.text._ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm,comdat
.LHOTE23:
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
	.align 2
.LCOLDB24:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LHOTB24:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
	.type	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm, @function
_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm:
.LFB9264:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA9264
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	$8, %eax
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbx
	movq	%rsi, %rdi
	movq	%rsi, %rbp
	shrq	$7, %rdi
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	leaq	1(%rdi), %r13
	addq	$3, %rdi
	cmpq	$8, %rdi
	cmovb	%rax, %rdi
	movq	%rdi, 8(%rbx)
	salq	$3, %rdi
.LEHB14:
	call	_Znwm
.LEHE14:
	movq	8(%rbx), %rdx
	movq	%rax, (%rbx)
	subq	%r13, %rdx
	shrq	%rdx
	leaq	(%rax,%rdx,8), %r12
	leaq	(%r12,%r13,8), %r13
	movq	%r12, %rdi
	movq	%r13, %rsi
.LEHB15:
	call	_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.84
.LEHE15:
	movq	(%r12), %rdx
	andl	$127, %ebp
	movq	%r12, 40(%rbx)
	leaq	512(%rdx), %rax
	movq	%rdx, 24(%rbx)
	movq	%rdx, 16(%rbx)
	movq	%rax, 32(%rbx)
	leaq	-8(%r13), %rax
	movq	%rax, 72(%rbx)
	movq	-8(%r13), %rax
	movq	%rax, 56(%rbx)
	leaq	512(%rax), %rcx
	leaq	(%rax,%rbp,4), %rax
	movq	%rcx, 64(%rbx)
	movq	%rax, 48(%rbx)
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
.L266:
	.cfi_restore_state
.L264:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	$0, (%rbx)
	movq	$0, 8(%rbx)
.LEHB16:
	call	__cxa_rethrow
.LEHE16:
.L267:
	movq	%rax, %rbx
.L265:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB17:
	call	_Unwind_Resume
.LEHE17:
	.cfi_endproc
.LFE9264:
	.section	.gcc_except_table
	.align 4
.LLSDA9264:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT9264-.LLSDATTD9264
.LLSDATTD9264:
	.byte	0x1
	.uleb128 .LLSDACSE9264-.LLSDACSB9264
.LLSDACSB9264:
	.uleb128 .LEHB14-.LFB9264
	.uleb128 .LEHE14-.LEHB14
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB15-.LFB9264
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L266-.LFB9264
	.uleb128 0x1
	.uleb128 .LEHB16-.LFB9264
	.uleb128 .LEHE16-.LEHB16
	.uleb128 .L267-.LFB9264
	.uleb128 0
	.uleb128 .LEHB17-.LFB9264
	.uleb128 .LEHE17-.LEHB17
	.uleb128 0
	.uleb128 0
.LLSDACSE9264:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT9264:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
	.size	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm, .-_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LCOLDE24:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LHOTE24:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,comdat
	.align 2
.LCOLDB25:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,comdat
.LHOTB25:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E
	.type	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E, @function
_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E:
.LFB9278:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L284
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
.L279:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E
	movq	56(%rbx), %rdi
	movq	16(%rbx), %rbp
	testq	%rdi, %rdi
	je	.L272
	call	_ZdlPv
.L272:
	movq	%rbx, %rdi
	movq	%rbp, %rbx
	call	_ZdlPv
	testq	%rbp, %rbp
	jne	.L279
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L284:
	rep ret
	.cfi_endproc
.LFE9278:
	.size	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E, .-_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,comdat
.LCOLDE25:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E,comdat
.LHOTE25:
	.section	.text.unlikely._ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev,"axG",@progbits,_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED5Ev,comdat
	.align 2
.LCOLDB26:
	.section	.text._ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev,"axG",@progbits,_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED5Ev,comdat
.LHOTB26:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev
	.type	_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev, @function
_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev:
.LFB9891:
	.cfi_startproc
	movq	16(%rdi), %rsi
	jmp	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE8_M_eraseEPSt13_Rb_tree_nodeIS3_E
	.cfi_endproc
.LFE9891:
	.size	_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev, .-_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev
	.section	.text.unlikely._ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev,"axG",@progbits,_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED5Ev,comdat
.LCOLDE26:
	.section	.text._ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev,"axG",@progbits,_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED5Ev,comdat
.LHOTE26:
	.weak	_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED1Ev
	.set	_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED1Ev,_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED2Ev
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,comdat
	.align 2
.LCOLDB27:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,comdat
.LHOTB27:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_
	.type	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_, @function
_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_:
.LFB9312:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	leaq	8(%rdi), %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	16(%rdi), %rdx
	testq	%rdx, %rdx
	je	.L288
	movl	(%rsi), %r8d
	jmp	.L289
	.p2align 4,,10
	.p2align 3
.L299:
	movq	16(%rdx), %rax
	testq	%rax, %rax
	je	.L290
.L300:
	movq	%rax, %rdx
.L289:
	movl	32(%rdx), %ecx
	cmpl	%r8d, %ecx
	jg	.L299
	movq	24(%rdx), %rax
	testq	%rax, %rax
	jne	.L300
.L290:
	cmpl	%r8d, %ecx
	movq	%rdx, %rbx
	movq	%rdx, %rax
	jg	.L288
.L293:
	xorl	%edx, %edx
	cmpl	%ecx, %r8d
	cmovg	%rdx, %rax
	cmovg	%rbx, %rdx
.L295:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L288:
	.cfi_restore_state
	xorl	%eax, %eax
	cmpq	24(%rdi), %rbx
	movq	%rbx, %rdx
	je	.L295
	movq	%rsi, %rbp
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movl	0(%rbp), %r8d
	movl	32(%rax), %ecx
	jmp	.L293
	.cfi_endproc
.LFE9312:
	.size	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_, .-_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,comdat
.LCOLDE27:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_,comdat
.LHOTE27:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,comdat
	.align 2
.LCOLDB28:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,comdat
.LHOTB28:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_
	.type	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_, @function
_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_:
.LFB9333:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	leaq	8(%rdi), %rax
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbp
	movq	%rdx, %r13
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	cmpq	%rax, %rsi
	je	.L314
	movl	(%rdx), %r12d
	cmpl	32(%rsi), %r12d
	movq	%rsi, %rbx
	jge	.L305
	movq	24(%rdi), %rax
	cmpq	%rsi, %rax
	movq	%rax, %rdx
	je	.L312
	movq	%rsi, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	cmpl	32(%rax), %r12d
	movq	%rax, %rdx
	jle	.L303
	cmpq	$0, 24(%rax)
	movl	$0, %ecx
	movq	%rcx, %rax
	cmovne	%rbx, %rax
	cmovne	%rbx, %rdx
.L312:
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
.L305:
	.cfi_restore_state
	jle	.L309
	movq	32(%rdi), %rdx
	xorl	%eax, %eax
	cmpq	%rsi, %rdx
	je	.L312
	movq	%rsi, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpl	32(%rax), %r12d
	movq	%rax, %rdx
	jge	.L303
	cmpq	$0, 24(%rbx)
	movl	$0, %ecx
	movq	%rcx, %rax
	cmovne	%rdx, %rax
	cmove	%rbx, %rdx
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
.L314:
	.cfi_restore_state
	cmpq	$0, 40(%rdi)
	je	.L303
	movq	32(%rdi), %rbx
	movl	(%rdx), %eax
	cmpl	%eax, 32(%rbx)
	jl	.L304
.L303:
	movq	%r13, %rsi
	movq	%rbp, %rdi
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_
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
.L309:
	.cfi_restore_state
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%rsi, %rax
	xorl	%edx, %edx
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
.L304:
	.cfi_restore_state
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	movq	%rbx, %rdx
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9333:
	.size	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_, .-_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,comdat
.LCOLDE28:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_,comdat
.LHOTE28:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,comdat
	.align 2
.LCOLDB29:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,comdat
.LHOTB29:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	.type	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_, @function
_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_:
.LFB9116:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movq	%rcx, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbp
	movl	$80, %edi
	movq	%rsi, %r12
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	call	_Znwm
	movq	%rax, %rbx
	movq	0(%r13), %rax
	movq	%r12, %rsi
	leaq	32(%rbx), %rdx
	movq	%rbp, %rdi
	movl	(%rax), %eax
	movq	$0, 56(%rbx)
	movq	$0, 64(%rbx)
	movq	$0, 72(%rbx)
	movl	$-1, 40(%rbx)
	movl	$-1, 44(%rbx)
	movl	%eax, 32(%rbx)
	movl	$0, 48(%rbx)
	movb	$0, 52(%rbx)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS3_ERS1_
	testq	%rdx, %rdx
	movq	%rax, %r12
	je	.L316
	testq	%rax, %rax
	leaq	8(%rbp), %rcx
	je	.L317
.L319:
	movl	$1, %edi
.L318:
	movq	%rbx, %rsi
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 40(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%rbx, %rax
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
.L316:
	.cfi_restore_state
	movq	56(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L321
	call	_ZdlPv
.L321:
	movq	%rbx, %rdi
	call	_ZdlPv
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%r12, %rax
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
.L317:
	.cfi_restore_state
	cmpq	%rdx, %rcx
	je	.L319
	xorl	%edi, %edi
	movl	32(%rdx), %eax
	cmpl	%eax, 32(%rbx)
	setl	%dil
	jmp	.L318
	.cfi_endproc
.LFE9116:
	.size	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_, .-_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,comdat
.LCOLDE29:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,comdat
.LHOTE29:
	.weak	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIIRKSt21piecewise_construct_tSt5tupleIIRS1_EESE_IIEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	.set	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIIRKSt21piecewise_construct_tSt5tupleIIRS1_EESE_IIEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_,_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	.section	.text.unlikely
.LCOLDB30:
	.text
.LHOTB30:
	.p2align 4,,15
	.globl	_Z10minBystackii
	.type	_Z10minBystackii, @function
_Z10minBystackii:
.LFB8676:
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
	subq	$48, %rsp
	.cfi_def_cfa_offset 80
	movq	fdata+16(%rip), %rdx
	movq	%fs:40, %rax
	movq	%rax, 40(%rsp)
	xorl	%eax, %eax
	movl	%edi, 12(%rsp)
	movl	%esi, 8(%rsp)
	testq	%rdx, %rdx
	je	.L343
	movl	%edi, %ecx
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L328
	.p2align 4,,10
	.p2align 3
.L358:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L329
.L328:
	cmpl	32(%rax), %ecx
	jle	.L358
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L328
.L329:
	cmpq	$fdata+8, %rsi
	je	.L327
	cmpl	32(%rsi), %ecx
	jge	.L359
.L327:
	leaq	31(%rsp), %rbp
	leaq	32(%rsp), %rbx
	leaq	12(%rsp), %rax
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%rbp, %r8
	movq	%rbx, %rcx
	movq	%rax, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	48(%rax), %r12d
	testq	%rdx, %rdx
	je	.L360
.L340:
	movl	8(%rsp), %ecx
	movl	$fdata+8, %eax
	jmp	.L333
	.p2align 4,,10
	.p2align 3
.L361:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L334
.L333:
	cmpl	%ecx, 32(%rdx)
	jge	.L361
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L333
.L334:
	cmpq	$fdata+8, %rax
	je	.L355
	cmpl	%ecx, 32(%rax)
	jg	.L355
	cmpl	%r12d, 48(%rax)
	jg	.L362
.L338:
	movl	8(%rsp), %eax
.L339:
	movq	40(%rsp), %rdi
	xorq	%fs:40, %rdi
	jne	.L363
	addq	$48, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L355:
	.cfi_restore_state
	leaq	31(%rsp), %rbp
	leaq	32(%rsp), %rbx
.L337:
	leaq	8(%rsp), %rdx
	movq	%rbp, %r8
	movq	%rbx, %rcx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movq	%rdx, 32(%rsp)
	movl	$_ZStL19piecewise_construct, %edx
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	cmpl	%r12d, 48(%rax)
	jle	.L338
.L362:
	movl	12(%rsp), %eax
	jmp	.L339
	.p2align 4,,10
	.p2align 3
.L359:
	movl	48(%rsi), %r12d
	jmp	.L340
.L360:
	movl	$fdata+8, %eax
	jmp	.L337
.L343:
	movl	$fdata+8, %esi
	jmp	.L327
.L363:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8676:
	.size	_Z10minBystackii, .-_Z10minBystackii
	.section	.text.unlikely
.LCOLDE30:
	.text
.LHOTE30:
	.section	.text.unlikely._ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB31:
	.section	.text._ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LHOTB31:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.type	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_, @function
_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_:
.LFB9343:
	.cfi_startproc
	movq	64(%rdi), %rcx
	movq	48(%rdi), %rax
	leaq	-8(%rcx), %rdx
	cmpq	%rdx, %rax
	je	.L365
	testq	%rax, %rax
	je	.L366
	movq	(%rsi), %rdx
	movq	%rdx, (%rax)
.L366:
	addq	$8, %rax
	movq	%rax, 48(%rdi)
	ret
	.p2align 4,,10
	.p2align 3
.L365:
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
	movq	%rsi, %rbp
	movq	%rdi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	72(%rdi), %r12
	movq	(%rdi), %rcx
	movq	8(%rdi), %rdx
	movq	%r12, %rax
	subq	%rcx, %rax
	movq	%rdx, %rsi
	sarq	$3, %rax
	subq	%rax, %rsi
	cmpq	$1, %rsi
	jbe	.L392
.L368:
	movl	$512, %edi
	call	_Znwm
	movq	%rax, 8(%r12)
	movq	48(%rbx), %rax
	testq	%rax, %rax
	je	.L376
	movq	0(%rbp), %rdx
	movq	%rdx, (%rax)
.L376:
	movq	72(%rbx), %rax
	leaq	8(%rax), %rdx
	movq	%rdx, 72(%rbx)
	movq	8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 56(%rbx)
	movq	%rax, 48(%rbx)
	movq	%rdx, 64(%rbx)
	addq	$8, %rsp
	.cfi_remember_state
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
	ret
	.p2align 4,,10
	.p2align 3
.L392:
	.cfi_restore_state
	movq	40(%rdi), %rsi
	movq	%r12, %r14
	subq	%rsi, %r14
	sarq	$3, %r14
	leaq	1(%r14), %r13
	addq	$2, %r14
	leaq	(%r14,%r14), %rax
	cmpq	%rax, %rdx
	jbe	.L369
	subq	%r14, %rdx
	shrq	%rdx
	leaq	(%rcx,%rdx,8), %r14
	cmpq	%r14, %rsi
	jbe	.L370
	leaq	8(%r12), %rdx
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	jne	.L393
.L391:
	salq	$3, %r13
.L372:
	movq	%r14, 40(%rbx)
	movq	(%r14), %rax
	leaq	-8(%r14,%r13), %r12
	movq	%r12, 72(%rbx)
	movq	%rax, 24(%rbx)
	addq	$512, %rax
	movq	%rax, 32(%rbx)
	movq	(%r12), %rax
	movq	%rax, 56(%rbx)
	addq	$512, %rax
	movq	%rax, 64(%rbx)
	jmp	.L368
	.p2align 4,,10
	.p2align 3
.L369:
	testq	%rdx, %rdx
	je	.L377
	leaq	2(%rdx,%rdx), %r12
	movabsq	$2305843009213693951, %rax
	cmpq	%rax, %r12
	ja	.L394
.L374:
	leaq	0(,%r12,8), %rdi
	call	_Znwm
	movq	%rax, %r15
	movq	%r12, %rax
	movq	40(%rbx), %rsi
	subq	%r14, %rax
	shrq	%rax
	leaq	(%r15,%rax,8), %r14
	movq	72(%rbx), %rax
	leaq	8(%rax), %rdx
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	jne	.L395
.L375:
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	%r15, (%rbx)
	movq	%r12, 8(%rbx)
	jmp	.L391
.L377:
	movl	$3, %r12d
	jmp	.L374
.L393:
	movq	%r14, %rdi
	salq	$3, %r13
	call	memmove
	jmp	.L372
.L395:
	movq	%r14, %rdi
	call	memmove
	jmp	.L375
.L370:
	leaq	8(%r12), %rdx
	salq	$3, %r13
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L372
	movq	%r13, %rdi
	subq	%rdx, %rdi
	addq	%r14, %rdi
	call	memmove
	jmp	.L372
.L394:
	call	_ZSt17__throw_bad_allocv
	.cfi_endproc
.LFE9343:
	.size	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_, .-_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LCOLDE31:
	.section	.text._ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,"axG",@progbits,_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_,comdat
.LHOTE31:
	.weak	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIIS1_EEEvDpOT_
	.set	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIIS1_EEEvDpOT_,_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,comdat
	.align 2
.LCOLDB32:
	.section	.text._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,comdat
.LHOTB32:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_
	.type	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_, @function
_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_:
.LFB9351:
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
	je	.L407
	leaq	(%rcx,%rcx), %rsi
	cmpq	%rsi, %rcx
	jbe	.L424
.L408:
	movq	$-16, %r13
.L397:
	movq	%r13, %rdi
	call	_Znwm
	movq	8(%rbp), %r14
	movq	%rax, %r12
	addq	%rax, %r13
	movq	0(%rbp), %rax
	leaq	24(%r12), %r15
	movq	%r14, %rdx
	subq	%rax, %rdx
.L406:
	addq	%r12, %rdx
	je	.L409
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
.L399:
	cmpq	%r14, %rdi
	je	.L400
	movq	%r12, %rax
	movq	%rdi, %rdx
	.p2align 4,,10
	.p2align 3
.L402:
	testq	%rax, %rax
	je	.L401
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
.L401:
	addq	$24, %rdx
	addq	$24, %rax
	cmpq	%r14, %rdx
	jne	.L402
	leaq	24(%rdi), %rax
	movq	0(%rbp), %rbx
	subq	%rax, %r14
	shrq	$3, %r14
	leaq	48(%r12,%r14,8), %r15
	movq	8(%rbp), %r14
	cmpq	%rbx, %r14
	je	.L400
	.p2align 4,,10
	.p2align 3
.L404:
	movq	(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L403
	call	_ZdlPv
.L403:
	addq	$24, %rbx
	cmpq	%r14, %rbx
	jne	.L404
	movq	0(%rbp), %r14
.L400:
	testq	%r14, %r14
	je	.L405
	movq	%r14, %rdi
	call	_ZdlPv
.L405:
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
.L407:
	.cfi_restore_state
	movl	$24, %r13d
	jmp	.L397
	.p2align 4,,10
	.p2align 3
.L409:
	movq	%rax, %rdi
	jmp	.L399
.L424:
	movabsq	$768614336404564650, %rdi
	cmpq	%rdi, %rsi
	ja	.L408
	testq	%rsi, %rsi
	jne	.L425
	movl	$24, %r15d
	xorl	%r13d, %r13d
	xorl	%r12d, %r12d
	jmp	.L406
.L425:
	leaq	(%rsi,%rcx,4), %r13
	salq	$3, %r13
	jmp	.L397
	.cfi_endproc
.LFE9351:
	.size	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_, .-_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,comdat
.LCOLDE32:
	.section	.text._ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_,comdat
.LHOTE32:
	.weak	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIIS3_EEEvDpOT_
	.set	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIIS3_EEEvDpOT_,_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_
	.section	.text.unlikely
.LCOLDB33:
	.text
.LHOTB33:
	.p2align 4,,15
	.globl	_Z19setBiconnectedGraphii
	.type	_Z19setBiconnectedGraphii, @function
_Z19setBiconnectedGraphii:
.LFB8677:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8677
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movabsq	$-6148914691236517205, %rdx
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movl	%esi, %ebp
	movl	%edi, %ebx
	subq	$32, %rsp
	.cfi_def_cfa_offset 64
	movq	%fs:40, %rax
	movq	%rax, 24(%rsp)
	xorl	%eax, %eax
	movq	TComponent+8(%rip), %rax
	movq	$0, (%rsp)
	movq	$0, 8(%rsp)
	movq	$0, 16(%rsp)
	movq	%rax, %r12
	subq	TComponent(%rip), %r12
	sarq	$3, %r12
	imulq	%rdx, %r12
	cmpq	TComponent+16(%rip), %rax
	je	.L427
	testq	%rax, %rax
	je	.L428
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
	movq	(%rsp), %rdx
	movq	%rdx, (%rax)
	movq	8(%rsp), %rdx
	movq	%rdx, 8(%rax)
	movq	16(%rsp), %rdx
	movq	%rdx, 16(%rax)
	movq	TComponent+8(%rip), %rax
.L428:
	addq	$24, %rax
	movq	%rax, TComponent+8(%rip)
.L429:
	movslq	%r12d, %rax
	leaq	(%rax,%rax,2), %r12
	salq	$3, %r12
	jmp	.L437
	.p2align 4,,10
	.p2align 3
.L430:
	cmpl	-8(%rdi), %ebx
	je	.L473
.L443:
	movq	-8(%rdi), %rax
	subq	$8, %rdi
	movq	%rdi, edgeStack+48(%rip)
	movq	%rax, (%rsp)
.L446:
	movq	%r12, %rdi
	addq	TComponent(%rip), %rdi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L434
	testq	%rax, %rax
	je	.L435
	movq	(%rsp), %rdx
	movq	%rdx, (%rax)
.L435:
	addq	$8, %rax
	movq	%rax, 8(%rdi)
.L437:
	movq	edgeStack+48(%rip), %rdi
	movq	edgeStack+56(%rip), %rax
	movq	edgeStack+72(%rip), %rdx
	cmpq	%rax, %rdi
	jne	.L430
	movq	-8(%rdx), %rcx
	cmpl	504(%rcx), %ebx
	leaq	512(%rcx), %rsi
	jne	.L431
	cmpl	%ebp, -4(%rsi)
	je	.L474
.L467:
	cmpq	%rax, %rdi
	jne	.L443
	movq	-8(%rdx), %rcx
.L431:
	movq	504(%rcx), %rax
	movq	%rax, (%rsp)
	call	_ZdlPv
	movq	edgeStack+72(%rip), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, edgeStack+72(%rip)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, edgeStack+56(%rip)
	addq	$504, %rax
	movq	%rax, edgeStack+48(%rip)
	movq	%rdx, edgeStack+64(%rip)
	jmp	.L446
	.p2align 4,,10
	.p2align 3
.L473:
	movq	%rdi, %rsi
	cmpl	%ebp, -4(%rsi)
	jne	.L467
.L474:
	cmpq	%rax, %rdi
	je	.L475
	movq	-8(%rdi), %rax
	subq	$8, %rdi
	movq	%rdi, edgeStack+48(%rip)
	movq	%rax, (%rsp)
.L447:
	movq	%r12, %rdi
	addq	TComponent(%rip), %rdi
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L438
	testq	%rax, %rax
	je	.L439
	movq	(%rsp), %rdx
	movq	%rdx, (%rax)
.L439:
	addq	$8, %rax
	movq	%rax, 8(%rdi)
.L426:
	movq	24(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L476
	addq	$32, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L434:
	.cfi_restore_state
	movq	%rsp, %rsi
.LEHB18:
	call	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
.LEHE18:
	jmp	.L437
	.p2align 4,,10
	.p2align 3
.L475:
	movq	-8(%rdx), %rax
	movq	504(%rax), %rax
	movq	%rax, (%rsp)
	call	_ZdlPv
	movq	edgeStack+72(%rip), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, edgeStack+72(%rip)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, edgeStack+56(%rip)
	addq	$504, %rax
	movq	%rax, edgeStack+48(%rip)
	movq	%rdx, edgeStack+64(%rip)
	jmp	.L447
.L427:
	movq	%rsp, %rsi
	movl	$TComponent, %edi
.LEHB19:
	call	_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EE19_M_emplace_back_auxIJS3_EEEvDpOT_
.LEHE19:
	movq	(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L429
	call	_ZdlPv
	jmp	.L429
.L438:
	movq	%rsp, %rsi
.LEHB20:
	call	_ZNSt6vectorISt4pairIiiESaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	jmp	.L426
.L451:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L442
	call	_ZdlPv
.L442:
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE20:
.L476:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8677:
	.section	.gcc_except_table
.LLSDA8677:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8677-.LLSDACSB8677
.LLSDACSB8677:
	.uleb128 .LEHB18-.LFB8677
	.uleb128 .LEHE18-.LEHB18
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB19-.LFB8677
	.uleb128 .LEHE19-.LEHB19
	.uleb128 .L451-.LFB8677
	.uleb128 0
	.uleb128 .LEHB20-.LFB8677
	.uleb128 .LEHE20-.LEHB20
	.uleb128 0
	.uleb128 0
.LLSDACSE8677:
	.text
	.size	_Z19setBiconnectedGraphii, .-_Z19setBiconnectedGraphii
	.section	.text.unlikely
.LCOLDE33:
	.text
.LHOTE33:
	.section	.text.unlikely
.LCOLDB34:
	.text
.LHOTB34:
	.p2align 4,,15
	.globl	_Z3dfsi
	.type	_Z3dfsi, @function
_Z3dfsi:
.LFB8671:
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
	subq	$56, %rsp
	.cfi_def_cfa_offset 112
	movq	%fs:40, %rax
	movq	%rax, 40(%rsp)
	xorl	%eax, %eax
	movq	fdata+16(%rip), %rax
	movl	%edi, 12(%rsp)
	testq	%rax, %rax
	je	.L624
	movq	%rax, %rdx
	movl	$fdata+8, %esi
	jmp	.L479
	.p2align 4,,10
	.p2align 3
.L748:
	movq	%rdx, %rsi
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L480
.L479:
	cmpl	32(%rdx), %edi
	jle	.L748
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L479
.L480:
	cmpq	$fdata+8, %rsi
	je	.L478
	cmpl	32(%rsi), %edi
	jge	.L749
.L478:
	leaq	28(%rsp), %rbp
	leaq	32(%rsp), %rbx
	leaq	12(%rsp), %r12
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%rbp, %r8
	movq	%rbx, %rcx
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movb	$1, 52(%rax)
	movl	12(%rsp), %edi
	testq	%rdx, %rdx
	je	.L750
.L599:
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L484
	.p2align 4,,10
	.p2align 3
.L751:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L485
.L484:
	cmpl	%edi, 32(%rax)
	jge	.L751
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L484
.L485:
	cmpq	$fdata+8, %rsi
	je	.L728
	cmpl	%edi, 32(%rsi)
	jle	.L707
.L728:
	leaq	32(%rsp), %rbx
	leaq	12(%rsp), %r12
	leaq	28(%rsp), %rbp
.L488:
	movq	%rbx, %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%rbp, %r8
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movl	_ZZ3dfsiE10stackOrder(%rip), %ecx
	movq	fdata+16(%rip), %rdx
	movl	12(%rsp), %edi
	leal	1(%rcx), %esi
	testq	%rdx, %rdx
	movl	%ecx, 48(%rax)
	movl	%esi, _ZZ3dfsiE10stackOrder(%rip)
	je	.L752
.L600:
	movl	%edi, %r8d
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L490
	.p2align 4,,10
	.p2align 3
.L753:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L491
.L490:
	cmpl	%edi, 32(%rax)
	jge	.L753
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L490
.L491:
	cmpq	$fdata+8, %rsi
	je	.L729
	cmpl	%edi, 32(%rsi)
	jle	.L709
.L729:
	leaq	32(%rsp), %rbx
	leaq	12(%rsp), %r12
	leaq	28(%rsp), %rbp
.L494:
	movq	%rbp, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbx, %rcx
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	12(%rsp), %r8d
	testq	%rdx, %rdx
	movl	%r8d, 44(%rax)
	je	.L754
.L601:
	movq	%rdx, %rcx
	movl	$fdata+8, %eax
	jmp	.L497
	.p2align 4,,10
	.p2align 3
.L756:
	movq	%rcx, %rax
	movq	16(%rcx), %rcx
	testq	%rcx, %rcx
	je	.L755
.L497:
	cmpl	%r8d, 32(%rcx)
	jge	.L756
	movq	24(%rcx), %rcx
	testq	%rcx, %rcx
	jne	.L497
.L755:
	cmpq	$fdata+8, %rax
	je	.L730
	cmpl	%r8d, 32(%rax)
	jg	.L730
.L602:
	testq	%rdx, %rdx
	movq	56(%rax), %rbx
	leaq	12(%rsp), %r12
	leaq	28(%rsp), %rbp
	leaq	24(%rsp), %r13
	je	.L625
	.p2align 4,,10
	.p2align 3
.L768:
	movl	12(%rsp), %ecx
	movl	$fdata+8, %eax
	jmp	.L502
	.p2align 4,,10
	.p2align 3
.L757:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L503
.L502:
	cmpl	%ecx, 32(%rdx)
	jge	.L757
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L502
.L503:
	cmpq	$fdata+8, %rax
	je	.L501
	cmpl	%ecx, 32(%rax)
	jle	.L603
.L501:
	leaq	32(%rsp), %rcx
	movq	%rbp, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
.L603:
	cmpq	64(%rax), %rbx
	jnb	.L477
	movq	fdata+16(%rip), %rdx
	movl	(%rbx), %ecx
	movl	$fdata+8, %esi
	testq	%rdx, %rdx
	movl	%ecx, 24(%rsp)
	movq	%rdx, %rax
	jne	.L510
	jmp	.L507
	.p2align 4,,10
	.p2align 3
.L758:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L509
.L510:
	cmpl	32(%rax), %ecx
	jle	.L758
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L510
.L509:
	cmpq	$fdata+8, %rsi
	je	.L507
	cmpl	32(%rsi), %ecx
	jl	.L507
	cmpb	$0, 52(%rsi)
	je	.L605
	movq	%rdx, %rdi
.L621:
	movl	12(%rsp), %ecx
	movq	%rdi, %rax
	movl	$fdata+8, %esi
	jmp	.L555
	.p2align 4,,10
	.p2align 3
.L759:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L556
.L555:
	cmpl	%ecx, 32(%rax)
	jge	.L759
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L555
.L556:
	cmpq	$fdata+8, %rsi
	je	.L554
	cmpl	%ecx, 32(%rsi)
	jg	.L554
	movl	24(%rsp), %ecx
	cmpl	40(%rsi), %ecx
	movq	%rdi, %rdx
	je	.L553
.L561:
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L563
	.p2align 4,,10
	.p2align 3
.L761:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L760
.L563:
	cmpl	%ecx, 32(%rax)
	jge	.L761
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L563
.L760:
	cmpq	$fdata+8, %rsi
	je	.L560
	cmpl	%ecx, 32(%rsi)
	jg	.L560
	movl	48(%rsi), %r14d
.L614:
	movl	12(%rsp), %ecx
	movl	$fdata+8, %eax
	jmp	.L567
	.p2align 4,,10
	.p2align 3
.L762:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L568
.L567:
	cmpl	%ecx, 32(%rdx)
	jge	.L762
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L567
.L568:
	cmpq	$fdata+8, %rax
	je	.L571
	cmpl	%ecx, 32(%rax)
	jle	.L615
.L571:
	leaq	32(%rsp), %rcx
	movq	%rbp, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
.L615:
	cmpl	48(%rax), %r14d
	movq	fdata+16(%rip), %rdx
	jge	.L553
	movl	12(%rsp), %eax
	leaq	32(%rsp), %rsi
	movl	$edgeStack, %edi
	movl	%eax, 32(%rsp)
	movl	24(%rsp), %eax
	movl	%eax, 36(%rsp)
	call	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	movq	fdata+16(%rip), %rax
	testq	%rax, %rax
	je	.L640
	movl	12(%rsp), %ecx
	movq	%rax, %rdx
	movl	$fdata+8, %esi
	jmp	.L616
	.p2align 4,,10
	.p2align 3
.L763:
	movq	%rdx, %rsi
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L574
.L616:
	cmpl	32(%rdx), %ecx
	jle	.L763
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L616
.L574:
	cmpq	$fdata+8, %rsi
	je	.L577
	cmpl	32(%rsi), %ecx
	jl	.L577
	movl	44(%rsi), %ecx
	movq	%rax, %rdx
	movl	%ecx, 28(%rsp)
.L617:
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L580
	.p2align 4,,10
	.p2align 3
.L765:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L764
.L580:
	cmpl	32(%rax), %ecx
	jle	.L765
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L580
.L764:
	cmpq	$fdata+8, %rsi
	je	.L583
	cmpl	32(%rsi), %ecx
	jl	.L583
	movl	48(%rsi), %r14d
.L618:
	movl	24(%rsp), %ecx
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L585
	.p2align 4,,10
	.p2align 3
.L766:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L586
.L585:
	cmpl	32(%rax), %ecx
	jle	.L766
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L585
.L586:
	cmpq	$fdata+8, %rsi
	je	.L734
	cmpl	32(%rsi), %ecx
	jl	.L734
	movl	48(%rsi), %r9d
.L619:
	movl	12(%rsp), %edi
	movq	%rdx, %rcx
	movl	$fdata+8, %eax
	jmp	.L591
	.p2align 4,,10
	.p2align 3
.L767:
	movq	%rcx, %rax
	movq	16(%rcx), %rcx
	testq	%rcx, %rcx
	je	.L592
.L591:
	cmpl	%edi, 32(%rcx)
	jge	.L767
	movq	24(%rcx), %rcx
	testq	%rcx, %rcx
	jne	.L591
.L592:
	cmpq	$fdata+8, %rax
	je	.L735
	cmpl	%edi, 32(%rax)
	jle	.L620
.L735:
	leaq	23(%rsp), %r15
.L595:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%r15, %r8
	movq	%rax, %rsi
	movl	$fdata, %edi
	movl	%r9d, 8(%rsp)
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	8(%rsp), %r9d
.L620:
	cmpl	%r9d, %r14d
	jge	.L596
	movl	28(%rsp), %ecx
.L597:
	movl	%ecx, 44(%rax)
.L553:
	addq	$4, %rbx
.L779:
	testq	%rdx, %rdx
	jne	.L768
.L625:
	movl	$fdata+8, %eax
	jmp	.L501
.L730:
	leaq	32(%rsp), %rbx
	leaq	12(%rsp), %r12
	leaq	28(%rsp), %rbp
.L500:
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbp, %r8
	movq	%rbx, %rcx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	jmp	.L602
	.p2align 4,,10
	.p2align 3
.L507:
	leaq	32(%rsp), %rcx
	movq	%rbp, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	cmpb	$0, 52(%rax)
	je	.L605
	movq	fdata+16(%rip), %rdi
	testq	%rdi, %rdi
	jne	.L621
	movl	$fdata+8, %esi
	.p2align 4,,10
	.p2align 3
.L554:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbp, %r8
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movl	24(%rsp), %ecx
	cmpl	%ecx, 40(%rax)
	movq	fdata+16(%rip), %rdx
	je	.L553
	testq	%rdx, %rdx
	jne	.L561
	movl	$fdata+8, %esi
	.p2align 4,,10
	.p2align 3
.L560:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbp, %r8
	movl	$fdata, %edi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	48(%rax), %r14d
	testq	%rdx, %rdx
	jne	.L614
	movl	$fdata+8, %eax
	jmp	.L571
	.p2align 4,,10
	.p2align 3
.L605:
	movl	12(%rsp), %eax
	leaq	32(%rsp), %rsi
	movl	$edgeStack, %edi
	movl	%eax, 32(%rsp)
	movl	24(%rsp), %eax
	movl	%eax, 36(%rsp)
	call	_ZNSt5dequeISt4pairIiiESaIS1_EE12emplace_backIJS1_EEEvDpOT_
	movq	fdata+16(%rip), %rdx
	testq	%rdx, %rdx
	je	.L627
	movl	24(%rsp), %edi
	movl	$fdata+8, %eax
	jmp	.L515
	.p2align 4,,10
	.p2align 3
.L769:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L516
.L515:
	cmpl	%edi, 32(%rdx)
	jge	.L769
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L515
.L516:
	cmpq	$fdata+8, %rax
	je	.L514
	cmpl	%edi, 32(%rax)
	jle	.L606
.L514:
	leaq	32(%rsp), %rcx
	movl	$fdata, %edi
	movq	%rbp, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movl	24(%rsp), %edi
.L606:
	movl	12(%rsp), %edx
	movl	%edx, 40(%rax)
	call	_Z3dfsi
	movq	fdata+16(%rip), %rdx
	testq	%rdx, %rdx
	je	.L628
	movl	24(%rsp), %ecx
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L520
	.p2align 4,,10
	.p2align 3
.L770:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L521
.L520:
	cmpl	%ecx, 32(%rax)
	jge	.L770
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L520
.L521:
	cmpq	$fdata+8, %rsi
	je	.L519
	cmpl	%ecx, 32(%rsi)
	jg	.L519
	movl	44(%rsi), %ecx
	movl	%ecx, 28(%rsp)
.L607:
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L526
	.p2align 4,,10
	.p2align 3
.L772:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L771
.L526:
	cmpl	32(%rax), %ecx
	jle	.L772
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L526
.L771:
	cmpq	$fdata+8, %rsi
	je	.L529
	cmpl	32(%rsi), %ecx
	jl	.L529
	movl	48(%rsi), %r14d
.L608:
	movl	12(%rsp), %ecx
	movl	$fdata+8, %eax
	jmp	.L531
	.p2align 4,,10
	.p2align 3
.L773:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L532
.L531:
	cmpl	32(%rdx), %ecx
	jle	.L773
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L531
.L532:
	cmpq	$fdata+8, %rax
	je	.L731
	cmpl	32(%rax), %ecx
	jge	.L609
.L731:
	leaq	23(%rsp), %r15
.L535:
	leaq	32(%rsp), %rcx
	movq	%r15, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
.L609:
	cmpl	%r14d, 48(%rax)
	jle	.L774
	movq	fdata+16(%rip), %rdx
	testq	%rdx, %rdx
	je	.L629
.L780:
	movl	12(%rsp), %ecx
	movq	%rdx, %rax
	movl	$fdata+8, %r14d
	jmp	.L538
	.p2align 4,,10
	.p2align 3
.L775:
	movq	%rax, %r14
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L539
.L538:
	cmpl	%ecx, 32(%rax)
	jge	.L775
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L538
.L539:
	cmpq	$fdata+8, %r14
	je	.L537
	cmpl	%ecx, 32(%r14)
	jle	.L610
.L537:
	leaq	23(%rsp), %r15
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%r14, %rsi
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	movq	%r15, %r8
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movq	%rax, %r14
	testq	%rdx, %rdx
	je	.L776
.L610:
	movl	24(%rsp), %ecx
	movq	%rdx, %rax
	movl	$fdata+8, %esi
	jmp	.L542
	.p2align 4,,10
	.p2align 3
.L777:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L543
.L542:
	cmpl	32(%rax), %ecx
	jle	.L777
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L542
.L543:
	cmpq	$fdata+8, %rsi
	je	.L732
	cmpl	32(%rsi), %ecx
	jl	.L732
	movl	44(%rsi), %r9d
.L611:
	movl	12(%rsp), %ecx
	movl	$fdata+8, %eax
	jmp	.L548
	.p2align 4,,10
	.p2align 3
.L778:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L549
.L548:
	cmpl	32(%rdx), %ecx
	jle	.L778
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L548
.L549:
	cmpq	$fdata+8, %rax
	je	.L733
	cmpl	32(%rax), %ecx
	jge	.L612
.L733:
	leaq	23(%rsp), %r15
.L552:
	leaq	32(%rsp), %rcx
	movq	%r15, %r8
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movl	$fdata, %edi
	movl	%r9d, 8(%rsp)
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movl	8(%rsp), %r9d
.L612:
	movl	44(%rax), %edi
	movl	%r9d, %esi
	addq	$4, %rbx
	call	_Z10minBystackii
	movq	fdata+16(%rip), %rdx
	movl	%eax, 44(%r14)
	jmp	.L779
.L628:
	movl	$fdata+8, %esi
	.p2align 4,,10
	.p2align 3
.L519:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbp, %r8
	movl	$fdata, %edi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	44(%rax), %ecx
	testq	%rdx, %rdx
	movl	%ecx, 28(%rsp)
	jne	.L607
	movl	$fdata+8, %esi
	.p2align 4,,10
	.p2align 3
.L529:
	leaq	23(%rsp), %r15
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%rbp, 32(%rsp)
	movq	%r15, %r8
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	48(%rax), %r14d
	testq	%rdx, %rdx
	jne	.L608
	movl	$fdata+8, %eax
	jmp	.L535
	.p2align 4,,10
	.p2align 3
.L732:
	leaq	23(%rsp), %r15
.L546:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%r15, %r8
	movl	$fdata, %edi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	44(%rax), %r9d
	testq	%rdx, %rdx
	jne	.L611
	movl	$fdata+8, %eax
	jmp	.L552
	.p2align 4,,10
	.p2align 3
.L774:
	movl	24(%rsp), %esi
	movl	12(%rsp), %edi
	call	_Z19setBiconnectedGraphii
	movq	fdata+16(%rip), %rdx
	testq	%rdx, %rdx
	jne	.L780
.L629:
	movl	$fdata+8, %r14d
	jmp	.L537
.L477:
	movq	40(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L781
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
.L640:
	.cfi_restore_state
	movl	$fdata+8, %esi
.L577:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbp, %r8
	movl	$fdata, %edi
	movq	%r12, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	44(%rax), %ecx
	testq	%rdx, %rdx
	movl	%ecx, 28(%rsp)
	jne	.L617
	movl	$fdata+8, %esi
.L583:
	leaq	23(%rsp), %r15
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movl	$fdata, %edi
	movq	%rbp, 32(%rsp)
	movq	%r15, %r8
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	48(%rax), %r14d
	testq	%rdx, %rdx
	jne	.L618
	movl	$fdata+8, %esi
	jmp	.L589
.L596:
	movl	24(%rsp), %ecx
	jmp	.L597
.L734:
	leaq	23(%rsp), %r15
.L589:
	leaq	32(%rsp), %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%r15, %r8
	movl	$fdata, %edi
	movq	%r13, 32(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESE_IJEEEEESt17_Rb_tree_iteratorIS3_ESt23_Rb_tree_const_iteratorIS3_EDpOT_
	movq	fdata+16(%rip), %rdx
	movl	48(%rax), %r9d
	testq	%rdx, %rdx
	jne	.L619
	movl	$fdata+8, %eax
	jmp	.L595
.L709:
	movl	%edi, 44(%rsi)
	jmp	.L601
.L707:
	movl	_ZZ3dfsiE10stackOrder(%rip), %eax
	leal	1(%rax), %ecx
	movl	%eax, 48(%rsi)
	movl	%ecx, _ZZ3dfsiE10stackOrder(%rip)
	jmp	.L600
.L749:
	movb	$1, 52(%rsi)
	movq	%rax, %rdx
	jmp	.L599
.L776:
	movl	$fdata+8, %esi
	jmp	.L546
.L627:
	movl	$fdata+8, %eax
	jmp	.L514
.L752:
	movl	$fdata+8, %esi
	jmp	.L494
.L754:
	movl	$fdata+8, %eax
	jmp	.L500
.L750:
	movl	$fdata+8, %esi
	jmp	.L488
.L624:
	movl	$fdata+8, %esi
	jmp	.L478
.L781:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8671:
	.size	_Z3dfsi, .-_Z3dfsi
	.section	.text.unlikely
.LCOLDE34:
	.text
.LHOTE34:
	.section	.text.unlikely
.LCOLDB35:
	.text
.LHOTB35:
	.p2align 4,,15
	.globl	_Z16findBicomponentsv
	.type	_Z16findBicomponentsv, @function
_Z16findBicomponentsv:
.LFB8670:
	.cfi_startproc
	movq	fdata+24(%rip), %rax
	cmpq	$fdata+8, %rax
	je	.L791
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	jmp	.L787
	.p2align 4,,10
	.p2align 3
.L784:
	movq	%rax, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpq	$fdata+8, %rax
	je	.L792
.L787:
	cmpb	$0, 52(%rax)
	jne	.L784
	movl	32(%rax), %edi
	movq	%rax, 8(%rsp)
	call	_Z3dfsi
	movq	8(%rsp), %rax
	movq	%rax, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpq	$fdata+8, %rax
	jne	.L787
.L792:
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
.L791:
	rep ret
	.cfi_endproc
.LFE8670:
	.size	_Z16findBicomponentsv, .-_Z16findBicomponentsv
	.section	.text.unlikely
.LCOLDE35:
	.text
.LHOTE35:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,comdat
	.align 2
.LCOLDB36:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,comdat
.LHOTB36:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_
	.type	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_, @function
_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_:
.LFB9381:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	leaq	8(%rdi), %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	16(%rdi), %rdx
	testq	%rdx, %rdx
	je	.L795
	movl	(%rsi), %r8d
	jmp	.L796
	.p2align 4,,10
	.p2align 3
.L806:
	movq	16(%rdx), %rax
	testq	%rax, %rax
	je	.L797
.L807:
	movq	%rax, %rdx
.L796:
	movl	32(%rdx), %ecx
	cmpl	%r8d, %ecx
	jg	.L806
	movq	24(%rdx), %rax
	testq	%rax, %rax
	jne	.L807
.L797:
	cmpl	%r8d, %ecx
	movq	%rdx, %rbx
	movq	%rdx, %rax
	jg	.L795
.L800:
	xorl	%edx, %edx
	cmpl	%ecx, %r8d
	cmovg	%rdx, %rax
	cmovg	%rbx, %rdx
.L802:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L795:
	.cfi_restore_state
	xorl	%eax, %eax
	cmpq	24(%rdi), %rbx
	movq	%rbx, %rdx
	je	.L802
	movq	%rsi, %rbp
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movl	0(%rbp), %r8d
	movl	32(%rax), %ecx
	jmp	.L800
	.cfi_endproc
.LFE9381:
	.size	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_, .-_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,comdat
.LCOLDE36:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_,comdat
.LHOTE36:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,comdat
	.align 2
.LCOLDB37:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,comdat
.LHOTB37:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_
	.type	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_, @function
_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_:
.LFB9395:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	leaq	8(%rdi), %rax
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbp
	movq	%rdx, %r13
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	cmpq	%rax, %rsi
	je	.L821
	movl	(%rdx), %r12d
	cmpl	32(%rsi), %r12d
	movq	%rsi, %rbx
	jge	.L812
	movq	24(%rdi), %rax
	cmpq	%rsi, %rax
	movq	%rax, %rdx
	je	.L819
	movq	%rsi, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	cmpl	32(%rax), %r12d
	movq	%rax, %rdx
	jle	.L810
	cmpq	$0, 24(%rax)
	movl	$0, %ecx
	movq	%rcx, %rax
	cmovne	%rbx, %rax
	cmovne	%rbx, %rdx
.L819:
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
.L812:
	.cfi_restore_state
	jle	.L816
	movq	32(%rdi), %rdx
	xorl	%eax, %eax
	cmpq	%rsi, %rdx
	je	.L819
	movq	%rsi, %rdi
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpl	32(%rax), %r12d
	movq	%rax, %rdx
	jge	.L810
	cmpq	$0, 24(%rbx)
	movl	$0, %ecx
	movq	%rcx, %rax
	cmovne	%rdx, %rax
	cmove	%rbx, %rdx
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
.L821:
	.cfi_restore_state
	cmpq	$0, 40(%rdi)
	je	.L810
	movq	32(%rdi), %rbx
	movl	(%rdx), %eax
	cmpl	%eax, 32(%rbx)
	jl	.L811
.L810:
	movq	%r13, %rsi
	movq	%rbp, %rdi
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_
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
.L816:
	.cfi_restore_state
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%rsi, %rax
	xorl	%edx, %edx
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
.L811:
	.cfi_restore_state
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	movq	%rbx, %rdx
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE9395:
	.size	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_, .-_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,comdat
.LCOLDE37:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_,comdat
.LHOTE37:
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,comdat
	.align 2
.LCOLDB38:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,comdat
.LHOTB38:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	.type	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_, @function
_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_:
.LFB9175:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movq	%rcx, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	movq	%rdi, %rbp
	movl	$64, %edi
	movq	%rsi, %r12
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	call	_Znwm
	movq	%rax, %rbx
	movq	0(%r13), %rax
	movq	%r12, %rsi
	leaq	32(%rbx), %rdx
	movq	%rbp, %rdi
	movl	(%rax), %eax
	movq	$0, 40(%rbx)
	movq	$0, 48(%rbx)
	movq	$0, 56(%rbx)
	movl	%eax, 32(%rbx)
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE29_M_get_insert_hint_unique_posESt23_Rb_tree_const_iteratorIS5_ERS1_
	testq	%rdx, %rdx
	movq	%rax, %r12
	je	.L823
	testq	%rax, %rax
	leaq	8(%rbp), %rcx
	je	.L824
.L826:
	movl	$1, %edi
.L825:
	movq	%rbx, %rsi
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 40(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%rbx, %rax
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
.L823:
	.cfi_restore_state
	movq	40(%rbx), %rdi
	testq	%rdi, %rdi
	je	.L828
	call	_ZdlPv
.L828:
	movq	%rbx, %rdi
	call	_ZdlPv
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%r12, %rax
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
.L824:
	.cfi_restore_state
	cmpq	%rcx, %rdx
	je	.L826
	xorl	%edi, %edi
	movl	32(%rdx), %eax
	cmpl	%eax, 32(%rbx)
	setl	%dil
	jmp	.L825
	.cfi_endproc
.LFE9175:
	.size	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_, .-_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,comdat
.LCOLDE38:
	.section	.text._ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,"axG",@progbits,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,comdat
.LHOTE38:
	.weak	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIIRKSt21piecewise_construct_tSt5tupleIIRS1_EESG_IIEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	.set	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIIRKSt21piecewise_construct_tSt5tupleIIRS1_EESG_IIEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_,_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDB39:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTB39:
	.p2align 4,,15
	.weak	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.type	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, @function
_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_:
.LFB9508:
	.cfi_startproc
	cmpq	%rdi, %rsi
	je	.L850
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
	je	.L833
	movq	%rsi, %r14
	movq	%rdi, %r13
	movl	$4, %r12d
	.p2align 4,,10
	.p2align 3
.L841:
	movl	0(%rbp), %ebx
	cmpl	0(%r13), %ebx
	jl	.L852
	movl	-4(%rbp), %edx
	leaq	-4(%rbp), %rax
	cmpl	%edx, %ebx
	jl	.L840
	jmp	.L853
	.p2align 4,,10
	.p2align 3
.L843:
	movq	%rcx, %rax
.L840:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %ebx
	jl	.L843
.L839:
	movl	%ebx, (%rax)
.L838:
	addq	$4, %rbp
	cmpq	%rbp, %r14
	jne	.L841
.L833:
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
.L850:
	rep ret
	.p2align 4,,10
	.p2align 3
.L852:
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
	je	.L837
	movq	%r12, %rdi
	movq	%r13, %rsi
	subq	%rdx, %rdi
	addq	%rbp, %rdi
	call	memmove
.L837:
	movl	%ebx, 0(%r13)
	jmp	.L838
.L853:
	movq	%rbp, %rax
	jmp	.L839
	.cfi_endproc
.LFE9508:
	.size	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, .-_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDE39:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTE39:
	.section	.text.unlikely
.LCOLDB40:
	.text
.LHOTB40:
	.p2align 4,,15
	.type	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139, @function
_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139:
.LFB10036:
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
	cmpq	$67, %rax
	jle	.L855
	subq	$8, %rsp
	.cfi_def_cfa_offset 40
	leaq	64(%rdi), %rbx
	pushq	$0
	.cfi_def_cfa_offset 48
	movq	%rbx, %rsi
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	cmpq	%rbx, %rbp
	popq	%rcx
	.cfi_def_cfa_offset 40
	popq	%rsi
	.cfi_def_cfa_offset 32
	movq	%rbx, %rsi
	je	.L854
	.p2align 4,,10
	.p2align 3
.L864:
	movl	(%rsi), %edi
	movl	-4(%rsi), %edx
	leaq	-4(%rsi), %rax
	cmpl	%edx, %edi
	jl	.L859
	jmp	.L868
	.p2align 4,,10
	.p2align 3
.L863:
	movq	%rcx, %rax
.L859:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %edi
	jl	.L863
	addq	$4, %rsi
	movl	%edi, (%rax)
	cmpq	%rsi, %rbp
	jne	.L864
.L854:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L855:
	.cfi_restore_state
	subq	$8, %rsp
	.cfi_def_cfa_offset 40
	pushq	$0
	.cfi_def_cfa_offset 48
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
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
.L868:
	.cfi_restore_state
	movq	%rsi, %rax
	addq	$4, %rsi
	cmpq	%rsi, %rbp
	movl	%edi, (%rax)
	jne	.L864
	jmp	.L854
	.cfi_endproc
.LFE10036:
	.size	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139, .-_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139
	.section	.text.unlikely
.LCOLDE40:
	.text
.LHOTE40:
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDB41:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTB41:
	.p2align 4,,15
	.weak	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.type	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, @function
_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_:
.LFB9808:
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
	jge	.L870
	movq	%rsi, %r10
	jmp	.L872
	.p2align 4,,10
	.p2align 3
.L880:
	movq	%rax, %r10
.L872:
	leaq	1(%r10), %r8
	leaq	(%r8,%r8), %rax
	leaq	(%rdi,%r8,8), %r8
	leaq	-1(%rax), %r11
	movl	(%r8), %r9d
	leaq	(%rdi,%r11,4), %rbp
	movl	0(%rbp), %ebx
	cmpl	%r9d, %ebx
	jle	.L871
	movq	%rbp, %r8
	movl	%ebx, %r9d
	movq	%r11, %rax
.L871:
	cmpq	%r12, %rax
	movl	%r9d, (%rdi,%r10,4)
	jl	.L880
	testb	$1, %dl
	jne	.L873
.L879:
	subq	$2, %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%r9, %rdx
	sarq	%rdx
	cmpq	%rax, %rdx
	je	.L884
.L873:
	cmpq	%rsi, %rax
	jle	.L874
	leaq	-1(%rax), %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%rdx, %r9
	sarq	%r9
	movl	(%rdi,%r9,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L874
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	movl	%r10d, (%rdi,%rax,4)
	jge	.L874
.L877:
	leaq	-1(%r9), %rax
	movq	%rax, %rdx
	shrq	$63, %rdx
	addq	%rax, %rdx
	movq	%r9, %rax
	sarq	%rdx
	movl	(%rdi,%rdx,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L874
	movq	%rdx, %r9
	movl	%r10d, (%rdi,%rax,4)
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	jl	.L877
.L874:
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
.L884:
	.cfi_restore_state
	leaq	1(%rax,%rax), %rax
	leaq	(%rdi,%rax,4), %rdx
	movl	(%rdx), %r9d
	movl	%r9d, (%r8)
	movq	%rdx, %r8
	jmp	.L873
.L870:
	testb	$1, %dl
	leaq	(%rdi,%rsi,4), %r8
	movq	%rsi, %rax
	je	.L879
	jmp	.L874
	.cfi_endproc
.LFE9808:
	.size	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, .-_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDE41:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTE41:
	.section	.text.unlikely
.LCOLDB42:
	.text
.LHOTB42:
	.p2align 4,,15
	.type	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147, @function
_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147:
.LFB10044:
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
	jle	.L885
	testq	%rdx, %rdx
	movq	%rdi, %r12
	movq	%rdx, %r13
	je	.L887
	leaq	8(%rdi), %rbx
	movq	%rsi, %rbp
.L888:
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
	jge	.L893
	cmpl	%ecx, %eax
	jl	.L899
	cmpl	%ecx, %edi
	jge	.L911
.L912:
	movl	(%r12), %edx
	movl	%ecx, (%r12)
	movl	%edx, -4(%rsi)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
.L895:
	movq	%rbx, %r8
	movq	%rsi, %rcx
	.p2align 4,,10
	.p2align 3
.L897:
	leaq	-4(%r8), %rbp
	cmpl	%edi, %r9d
	movq	%rbp, %r14
	jl	.L900
	cmpl	%edi, %edx
	leaq	-4(%rcx), %rax
	jle	.L907
	leaq	-8(%rcx), %rax
	.p2align 4,,10
	.p2align 3
.L902:
	movq	%rax, %rcx
	subq	$4, %rax
	movl	4(%rax), %edx
	cmpl	%edi, %edx
	jg	.L902
	cmpq	%rcx, %rbp
	jnb	.L913
.L903:
	movl	%edx, -4(%r8)
	movl	%r9d, (%rcx)
	movl	-4(%rcx), %edx
	movl	(%r12), %edi
.L900:
	movl	(%r8), %r9d
	addq	$4, %r8
	jmp	.L897
.L907:
	movq	%rax, %rcx
	cmpq	%rcx, %rbp
	jb	.L903
.L913:
	movq	%r13, %rdx
	movq	%rbp, %rdi
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147
	movq	%rbp, %rax
	subq	%r12, %rax
	cmpq	$67, %rax
	jle	.L885
	testq	%r13, %r13
	je	.L887
	movq	%rbp, %rsi
	jmp	.L888
.L893:
	cmpl	%ecx, %edi
	jl	.L911
	cmpl	%ecx, %eax
	jl	.L912
.L899:
	movl	(%r12), %ecx
	movl	%eax, (%r12)
	movl	%ecx, (%rdx)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
	movl	-4(%rsi), %edx
	jmp	.L895
.L911:
	movl	(%r12), %r9d
	movl	%edi, (%r12)
	movl	%r9d, 4(%r12)
	movl	-4(%rsi), %edx
	jmp	.L895
.L887:
	sarq	$2, %rax
	leaq	-2(%rax), %rbp
	movq	%rax, %rbx
	sarq	%rbp
	jmp	.L890
.L914:
	subq	$1, %rbp
.L890:
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
	jne	.L914
	subq	$4, %r14
.L891:
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
	jg	.L891
.L885:
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
.LFE10044:
	.size	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147, .-_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147
	.section	.text.unlikely
.LCOLDE42:
	.text
.LHOTE42:
	.section	.text.unlikely
.LCOLDB43:
	.text
.LHOTB43:
	.p2align 4,,15
	.globl	_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE
	.type	_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE, @function
_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE:
.LFB8681:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8681
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movq	%rdi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	movq	$0, (%rdi)
	movq	$0, 8(%rdi)
	movq	$0, 16(%rdi)
	movq	(%rsi), %rbp
	movq	8(%rsi), %r13
	cmpq	%r13, %rbp
	je	.L915
	xorl	%eax, %eax
	xorl	%ebx, %ebx
	jmp	.L924
	.p2align 4,,10
	.p2align 3
.L946:
	testq	%rbx, %rbx
	movl	0(%rbp), %edx
	je	.L918
	movl	%edx, (%rbx)
.L918:
	addq	$4, %rbx
	cmpq	%rbx, %rax
	movq	%rbx, 8(%r12)
	je	.L920
.L947:
	testq	%rbx, %rbx
	movl	4(%rbp), %eax
	je	.L921
	movl	%eax, (%rbx)
.L921:
	addq	$8, %rbp
	addq	$4, %rbx
	cmpq	%rbp, %r13
	movq	%rbx, 8(%r12)
	je	.L923
.L948:
	movq	16(%r12), %rax
.L924:
	cmpq	%rbx, %rax
	jne	.L946
	movq	%rbp, %rsi
	movq	%r12, %rdi
.LEHB21:
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	movq	8(%r12), %rbx
	movq	16(%r12), %rax
	cmpq	%rbx, %rax
	jne	.L947
	.p2align 4,,10
	.p2align 3
.L920:
	leaq	4(%rbp), %rsi
	movq	%r12, %rdi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
.LEHE21:
	addq	$8, %rbp
	movq	8(%r12), %rbx
	cmpq	%rbp, %r13
	jne	.L948
	.p2align 4,,10
	.p2align 3
.L923:
	movq	(%r12), %rbp
	cmpq	%rbp, %rbx
	je	.L915
	movq	%rbx, %rax
	movl	$63, %edx
	movq	%rbx, %rsi
	subq	%rbp, %rax
	movq	%rbp, %rdi
	sarq	$2, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147
	movq	%rbp, %rdi
	movq	%rbx, %rsi
	call	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139
	movq	8(%r12), %rdi
	movq	(%r12), %rdx
	cmpq	%rdx, %rdi
	jne	.L927
	jmp	.L915
	.p2align 4,,10
	.p2align 3
.L950:
	movl	4(%rdx), %esi
	cmpl	%esi, -4(%rax)
	je	.L949
	movq	%rax, %rdx
.L927:
	leaq	4(%rdx), %rax
	cmpq	%rax, %rdi
	movq	%rax, %rcx
	jne	.L950
.L915:
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%r12, %rax
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
.L949:
	.cfi_restore_state
	cmpq	%rdx, %rdi
	je	.L915
	.p2align 4,,10
	.p2align 3
.L928:
	addq	$4, %rcx
	cmpq	%rcx, %rdi
	je	.L930
.L951:
	movl	(%rcx), %esi
	cmpl	%esi, (%rdx)
	je	.L928
	addq	$4, %rcx
	movl	%esi, 4(%rdx)
	movq	%rax, %rdx
	addq	$4, %rax
	cmpq	%rcx, %rdi
	jne	.L951
.L930:
	cmpq	%rax, %rdi
	je	.L915
	movq	%rax, 8(%r12)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 40
	movq	%r12, %rax
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
.L935:
	.cfi_restore_state
	movq	(%r12), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L933
	call	_ZdlPv
.L933:
	movq	%rbx, %rdi
.LEHB22:
	call	_Unwind_Resume
.LEHE22:
	.cfi_endproc
.LFE8681:
	.section	.gcc_except_table
.LLSDA8681:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8681-.LLSDACSB8681
.LLSDACSB8681:
	.uleb128 .LEHB21-.LFB8681
	.uleb128 .LEHE21-.LEHB21
	.uleb128 .L935-.LFB8681
	.uleb128 0
	.uleb128 .LEHB22-.LFB8681
	.uleb128 .LEHE22-.LEHB22
	.uleb128 0
	.uleb128 0
.LLSDACSE8681:
	.text
	.size	_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE, .-_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE
	.section	.text.unlikely
.LCOLDE43:
	.text
.LHOTE43:
	.section	.text.unlikely
.LCOLDB44:
	.text
.LHOTB44:
	.p2align 4,,15
	.globl	_Z16findThebestGraphv
	.type	_Z16findThebestGraphv, @function
_Z16findThebestGraphv:
.LFB8682:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8682
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
	subq	$216, %rsp
	.cfi_def_cfa_offset 272
	movq	TComponent(%rip), %rbx
	movq	TComponent+8(%rip), %r12
	movq	%fs:40, %rax
	movq	%rax, 200(%rsp)
	xorl	%eax, %eax
	leaq	152(%rsp), %rax
	movq	%rdi, 8(%rsp)
	movl	$0, 152(%rsp)
	cmpq	%r12, %rbx
	movq	$0, 160(%rsp)
	movq	$0, 184(%rsp)
	movq	%rax, 168(%rsp)
	movq	%rax, 176(%rsp)
	movl	$0, 24(%rsp)
	je	.L1018
	leaq	80(%rsp), %rbp
	leaq	28(%rsp), %r13
	.p2align 4,,10
	.p2align 3
.L993:
	movq	%rbx, %rsi
	movq	%rbp, %rdi
.LEHB23:
	call	_Z8rearrageRSt6vectorISt4pairIiiESaIS1_EE
.LEHE23:
	movq	80(%rsp), %rdi
	movq	88(%rsp), %r14
	movq	160(%rsp), %rdx
	subq	%rdi, %r14
	movq	%r14, %r8
	sarq	$2, %r8
	testq	%rdx, %rdx
	movq	%r8, %r9
	movl	%r8d, %ecx
	movl	%r8d, 28(%rsp)
	je	.L954
	movq	%rdx, %rax
	leaq	152(%rsp), %rsi
	jmp	.L957
	.p2align 4,,10
	.p2align 3
.L1066:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L956
.L957:
	cmpl	32(%rax), %ecx
	jle	.L1066
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L957
.L956:
	leaq	152(%rsp), %rax
	cmpq	%rax, %rsi
	je	.L954
	cmpl	32(%rsi), %ecx
	jge	.L970
.L954:
	movl	%ecx, 112(%rsp)
	xorl	%ecx, %ecx
	testq	%r8, %r8
	movq	$0, 120(%rsp)
	movq	$0, 128(%rsp)
	movq	%r14, %r15
	movq	$0, 136(%rsp)
	je	.L962
	movabsq	$4611686018427387903, %rax
	cmpq	%rax, %r8
	ja	.L1067
	movq	%r14, %rdi
.LEHB24:
	call	_Znwm
.LEHE24:
	movq	%rax, %rcx
	movq	80(%rsp), %rdi
	movq	88(%rsp), %rax
	subq	%rdi, %rax
	movq	%rax, %r9
	movq	%rax, %r15
	sarq	$2, %r9
.L962:
	addq	%rcx, %r14
	testq	%r9, %r9
	movq	%rcx, 120(%rsp)
	movq	%rcx, 128(%rsp)
	movq	%r14, 136(%rsp)
	je	.L964
	movq	%rdi, %rsi
	movq	%r15, %rdx
	movq	%rcx, %rdi
	call	memmove
	movq	%rax, %rcx
.L964:
	leaq	(%rcx,%r15), %rax
	leaq	112(%rsp), %rsi
	leaq	144(%rsp), %rdi
	movq	%rax, 128(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE24_M_get_insert_unique_posERS1_
	testq	%rdx, %rdx
	movq	%rdx, %r14
	je	.L965
	testq	%rax, %rax
	jne	.L1019
	leaq	152(%rsp), %rax
	cmpq	%rax, %rdx
	je	.L1019
	movl	32(%rdx), %eax
	cmpl	%eax, 112(%rsp)
	setl	%al
	movl	%eax, %r15d
.L966:
	movl	$64, %edi
.LEHB25:
	call	_Znwm
.LEHE25:
	movl	112(%rsp), %edx
	leaq	152(%rsp), %rcx
	movzbl	%r15b, %edi
	movq	%rax, %rsi
	movl	%edx, 32(%rax)
	movq	120(%rsp), %rdx
	movq	$0, 120(%rsp)
	movq	%rdx, 40(%rax)
	movq	128(%rsp), %rdx
	movq	$0, 128(%rsp)
	movq	%rdx, 48(%rax)
	movq	136(%rsp), %rdx
	movq	$0, 136(%rsp)
	movq	%rdx, 56(%rax)
	movq	%r14, %rdx
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 184(%rsp)
.L965:
	movq	120(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1063
	call	_ZdlPv
.L1063:
	movq	80(%rsp), %rdi
.L968:
	movl	28(%rsp), %eax
	cmpl	%eax, 24(%rsp)
	jge	.L991
.L1015:
	movl	%eax, 24(%rsp)
.L991:
	testq	%rdi, %rdi
	je	.L992
.L1016:
	call	_ZdlPv
.L992:
	addq	$24, %rbx
	cmpq	%rbx, %r12
	jne	.L993
	movq	160(%rsp), %rax
	testq	%rax, %rax
	je	.L1024
	movl	24(%rsp), %edx
	leaq	152(%rsp), %rbx
	jmp	.L994
	.p2align 4,,10
	.p2align 3
.L1068:
	movq	%rax, %rbx
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L995
.L994:
	cmpl	%edx, 32(%rax)
	jge	.L1068
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L994
.L995:
	leaq	152(%rsp), %rax
	cmpq	%rax, %rbx
	je	.L953
	cmpl	%edx, 32(%rbx)
	jg	.L953
.L998:
	movq	48(%rbx), %rbp
	subq	40(%rbx), %rbp
	xorl	%ecx, %ecx
	movq	8(%rsp), %rdi
	movq	%rbp, %rax
	movq	$0, (%rdi)
	movq	$0, 8(%rdi)
	sarq	$2, %rax
	movq	$0, 16(%rdi)
	testq	%rax, %rax
	je	.L1000
	movabsq	$4611686018427387903, %rdx
	cmpq	%rdx, %rax
	ja	.L1069
	movq	%rbp, %rdi
.LEHB26:
	call	_Znwm
.LEHE26:
	movq	%rax, %rcx
.L1000:
	movq	8(%rsp), %rax
	addq	%rcx, %rbp
	movq	%rcx, (%rax)
	movq	%rcx, 8(%rax)
	movq	%rbp, 16(%rax)
	movq	40(%rbx), %rsi
	movq	48(%rbx), %rax
	subq	%rsi, %rax
	movq	%rax, %rbx
	sarq	$2, %rax
	testq	%rax, %rax
	je	.L1003
	movq	%rcx, %rdi
	movq	%rbx, %rdx
	call	memmove
	movq	%rax, %rcx
.L1003:
	movq	8(%rsp), %r15
	movq	160(%rsp), %rsi
	addq	%rcx, %rbx
	leaq	144(%rsp), %rdi
	movq	%rbx, 8(%r15)
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E
	movq	200(%rsp), %rbx
	xorq	%fs:40, %rbx
	movq	%r15, %rax
	jne	.L1070
	addq	$216, %rsp
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
.L1071:
	.cfi_restore_state
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L969
.L970:
	cmpl	32(%rdx), %ecx
	jle	.L1071
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L970
.L969:
	leaq	152(%rsp), %rdx
	cmpq	%rdx, %rax
	je	.L973
	cmpl	32(%rax), %ecx
	jge	.L974
.L973:
	leaq	21(%rsp), %r8
	leaq	32(%rsp), %rcx
	leaq	144(%rsp), %rdi
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movq	%r13, 32(%rsp)
.LEHB27:
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	movq	80(%rsp), %rdi
.L974:
	movq	40(%rax), %r8
	movq	48(%rax), %rcx
	subq	%r8, %rcx
	sarq	$2, %rcx
	testq	%rcx, %rcx
	je	.L968
	movl	(%r8), %eax
	cmpl	%eax, (%rdi)
	jl	.L975
	movl	$0, %edx
	je	.L1048
	jmp	.L977
	.p2align 4,,10
	.p2align 3
.L979:
	movl	(%rdi,%rax,4), %esi
	cmpl	%esi, (%r8,%rax,4)
	jg	.L975
	jne	.L977
.L1048:
	leal	1(%rdx), %eax
	cmpq	%rcx, %rax
	movq	%rax, %rdx
	jb	.L979
.L977:
	movl	28(%rsp), %eax
	cmpl	%eax, 24(%rsp)
	jl	.L1015
	jmp	.L1016
	.p2align 4,,10
	.p2align 3
.L975:
	movq	160(%rsp), %rdx
	testq	%rdx, %rdx
	je	.L1026
	movl	28(%rsp), %ecx
	movq	%rdx, %rax
	leaq	152(%rsp), %rsi
	jmp	.L1010
	.p2align 4,,10
	.p2align 3
.L1072:
	movq	%rax, %rsi
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L980
.L1010:
	cmpl	%ecx, 32(%rax)
	jge	.L1072
	movq	24(%rax), %rax
	testq	%rax, %rax
	jne	.L1010
.L980:
	leaq	152(%rsp), %rax
	cmpq	%rax, %rsi
	je	.L983
	cmpl	%ecx, 32(%rsi)
	jg	.L983
	movq	40(%rsi), %rax
	movq	%rax, 48(%rsi)
.L1014:
	leaq	152(%rsp), %rax
	jmp	.L986
	.p2align 4,,10
	.p2align 3
.L1073:
	movq	%rdx, %rax
	movq	16(%rdx), %rdx
	testq	%rdx, %rdx
	je	.L987
.L986:
	cmpl	%ecx, 32(%rdx)
	jge	.L1073
	movq	24(%rdx), %rdx
	testq	%rdx, %rdx
	jne	.L986
.L987:
	leaq	152(%rsp), %rdx
	cmpq	%rdx, %rax
	je	.L985
	cmpl	%ecx, 32(%rax)
	jle	.L990
.L985:
	leaq	23(%rsp), %r8
	leaq	64(%rsp), %rcx
	leaq	144(%rsp), %rdi
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rax, %rsi
	movq	%r13, 64(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
.L990:
	leaq	40(%rax), %rdi
	movq	%rbp, %rsi
	call	_ZNSt6vectorIiSaIiEEaSERKS1_
	jmp	.L1063
.L1026:
	leaq	144(%rsp), %rax
	leaq	8(%rax), %rsi
	.p2align 4,,10
	.p2align 3
.L983:
	leaq	22(%rsp), %r8
	leaq	48(%rsp), %rcx
	leaq	144(%rsp), %rdi
	movl	$_ZStL19piecewise_construct, %edx
	movq	%r13, 48(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
.LEHE27:
	movq	160(%rsp), %rdx
	movq	40(%rax), %rcx
	testq	%rdx, %rdx
	movq	%rcx, 48(%rax)
	movl	28(%rsp), %ecx
	jne	.L1014
	leaq	152(%rsp), %rax
	jmp	.L985
.L1024:
	leaq	152(%rsp), %rbx
.L953:
	leaq	24(%rsp), %rax
	leaq	28(%rsp), %r8
	leaq	144(%rsp), %rdi
	movq	%rbp, %rcx
	movl	$_ZStL19piecewise_construct, %edx
	movq	%rbx, %rsi
	movq	%rax, 80(%rsp)
.LEHB28:
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESG_IJEEEEESt17_Rb_tree_iteratorIS5_ESt23_Rb_tree_const_iteratorIS5_EDpOT_
	movq	%rax, %rbx
	jmp	.L998
.L1019:
	movl	$1, %r15d
	jmp	.L966
.L1069:
	call	_ZSt17__throw_bad_allocv
.LEHE28:
.L1070:
	call	__stack_chk_fail
.L1028:
	movq	120(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L1006
	call	_ZdlPv
.L1006:
	movq	80(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1008
	call	_ZdlPv
.L1008:
	movq	160(%rsp), %rsi
	leaq	144(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiSt4pairIKiSt6vectorIiSaIiEEESt10_Select1stIS5_ESt4lessIiESaIS5_EE8_M_eraseEPSt13_Rb_tree_nodeIS5_E
	movq	%rbx, %rdi
.LEHB29:
	call	_Unwind_Resume
.LEHE29:
.L1018:
	movq	%rax, %rbx
	leaq	80(%rsp), %rbp
	jmp	.L953
.L1029:
	movq	%rax, %rbx
	jmp	.L1008
.L1067:
.LEHB30:
	call	_ZSt17__throw_bad_allocv
.LEHE30:
.L1027:
	movq	%rax, %rbx
	jmp	.L1006
	.cfi_endproc
.LFE8682:
	.section	.gcc_except_table
.LLSDA8682:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8682-.LLSDACSB8682
.LLSDACSB8682:
	.uleb128 .LEHB23-.LFB8682
	.uleb128 .LEHE23-.LEHB23
	.uleb128 .L1029-.LFB8682
	.uleb128 0
	.uleb128 .LEHB24-.LFB8682
	.uleb128 .LEHE24-.LEHB24
	.uleb128 .L1027-.LFB8682
	.uleb128 0
	.uleb128 .LEHB25-.LFB8682
	.uleb128 .LEHE25-.LEHB25
	.uleb128 .L1028-.LFB8682
	.uleb128 0
	.uleb128 .LEHB26-.LFB8682
	.uleb128 .LEHE26-.LEHB26
	.uleb128 .L1029-.LFB8682
	.uleb128 0
	.uleb128 .LEHB27-.LFB8682
	.uleb128 .LEHE27-.LEHB27
	.uleb128 .L1027-.LFB8682
	.uleb128 0
	.uleb128 .LEHB28-.LFB8682
	.uleb128 .LEHE28-.LEHB28
	.uleb128 .L1029-.LFB8682
	.uleb128 0
	.uleb128 .LEHB29-.LFB8682
	.uleb128 .LEHE29-.LEHB29
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB30-.LFB8682
	.uleb128 .LEHE30-.LEHB30
	.uleb128 .L1027-.LFB8682
	.uleb128 0
.LLSDACSE8682:
	.text
	.size	_Z16findThebestGraphv, .-_Z16findThebestGraphv
	.section	.text.unlikely
.LCOLDE44:
	.text
.LHOTE44:
	.section	.rodata.str1.1
.LC45:
	.string	"food.inp"
	.section	.text.unlikely
.LCOLDB46:
	.text
.LHOTB46:
	.p2align 4,,15
	.globl	_Z9file_readv
	.type	_Z9file_readv, @function
_Z9file_readv:
.LFB8648:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8648
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
	subq	$648, %rsp
	.cfi_def_cfa_offset 688
	leaq	368(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 632(%rsp)
	xorl	%eax, %eax
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rbx
	movb	$0, 592(%rsp)
	leaq	112(%rsp), %rdi
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbp
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 368(%rsp)
	xorl	%esi, %esi
	movq	$0, 584(%rsp)
	movb	$0, 593(%rsp)
	movq	-24(%rbx), %rax
	movq	$0, 600(%rsp)
	movq	$0, 608(%rsp)
	movq	$0, 616(%rsp)
	movq	$0, 624(%rsp)
	movq	%rbx, 112(%rsp)
	movq	%rbp, 112(%rsp,%rax)
	movq	$0, 120(%rsp)
	addq	-24(%rbx), %rdi
.LEHB31:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE31:
	leaq	112(%rsp), %rax
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 112(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 368(%rsp)
	leaq	16(%rax), %rdi
.LEHB32:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE32:
	leaq	112(%rsp), %rax
	leaq	128(%rsp), %rsi
	leaq	256(%rax), %rdi
.LEHB33:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	112(%rsp), %rax
	movl	$8, %edx
	movl	$.LC45, %esi
	leaq	16(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	112(%rsp), %rdi
	movq	112(%rsp), %rax
	je	.L1140
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE33:
.L1076:
	leaq	8(%rsp), %rsi
	leaq	112(%rsp), %rdi
.LEHB34:
	call	_ZNSirsERi
.LEHE34:
	.p2align 4,,10
	.p2align 3
.L1138:
	movl	8(%rsp), %eax
	leal	-1(%rax), %edx
	testl	%eax, %eax
	movl	%edx, 8(%rsp)
	jle	.L1080
.L1143:
	leaq	4(%rsp), %rsi
	leaq	112(%rsp), %rdi
	movq	$0, 32(%rsp)
	movq	$0, 40(%rsp)
	movq	$0, 48(%rsp)
	movl	$-1, 16(%rsp)
	movl	$-1, 20(%rsp)
	movl	$0, 24(%rsp)
	movb	$0, 28(%rsp)
.LEHB35:
	call	_ZNSirsERi
	jmp	.L1081
	.p2align 4,,10
	.p2align 3
.L1141:
	testq	%rax, %rax
	je	.L1084
	movl	%edx, (%rax)
.L1084:
	addq	$4, %rax
	movq	%rax, 40(%rsp)
.L1081:
	leaq	12(%rsp), %rsi
	leaq	112(%rsp), %rdi
	call	_ZNSirsERi
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L1082
	movl	12(%rsp), %edx
	testl	%edx, %edx
	je	.L1082
	movq	40(%rsp), %rax
	cmpq	48(%rsp), %rax
	jne	.L1141
	leaq	12(%rsp), %rsi
	leaq	32(%rsp), %rdi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJRKiEEEvDpOT_
	jmp	.L1081
	.p2align 4,,10
	.p2align 3
.L1082:
	movq	40(%rsp), %r12
	movq	32(%rsp), %r13
	cmpq	%r13, %r12
	je	.L1103
	movq	%r12, %rax
	movl	$63, %edx
	movq	%r12, %rsi
	subq	%r13, %rax
	movq	%r13, %rdi
	sarq	$2, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.147
	movq	%r12, %rsi
	movq	%r13, %rdi
	call	_ZSt22__final_insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_.isra.139
	movq	40(%rsp), %rax
	movq	32(%rsp), %rsi
.L1086:
	movl	4(%rsp), %edx
	subq	%rsi, %rax
	xorl	%ecx, %ecx
	movq	%rax, %r13
	sarq	$2, %rax
	movq	$0, 88(%rsp)
	testq	%rax, %rax
	movq	%rax, %rdi
	movq	$0, 96(%rsp)
	movl	%edx, 64(%rsp)
	movl	16(%rsp), %edx
	movq	%r13, %r12
	movq	$0, 104(%rsp)
	movl	%edx, 72(%rsp)
	movl	20(%rsp), %edx
	movl	%edx, 76(%rsp)
	movl	24(%rsp), %edx
	movl	%edx, 80(%rsp)
	movzbl	28(%rsp), %edx
	movb	%dl, 84(%rsp)
	je	.L1088
	movabsq	$4611686018427387903, %rdx
	cmpq	%rdx, %rax
	ja	.L1142
	movq	%r13, %rdi
	call	_Znwm
.LEHE35:
	movq	32(%rsp), %rsi
	movq	40(%rsp), %rdx
	movq	%rax, %rcx
	subq	%rsi, %rdx
	movq	%rdx, %rdi
	movq	%rdx, %r12
	sarq	$2, %rdi
.L1088:
	leaq	(%rcx,%r13), %rax
	testq	%rdi, %rdi
	movq	%rcx, 88(%rsp)
	movq	%rcx, 96(%rsp)
	movq	%rax, 104(%rsp)
	je	.L1090
	movq	%rcx, %rdi
	movq	%r12, %rdx
	call	memmove
	movq	%rax, %rcx
.L1090:
	leaq	(%rcx,%r12), %rdx
	leaq	64(%rsp), %rsi
	movl	$fdata, %edi
	movq	%rdx, 96(%rsp)
	call	_ZNSt8_Rb_treeIiSt4pairIKi5fnodeESt10_Select1stIS3_ESt4lessIiESaIS3_EE24_M_get_insert_unique_posERS1_
	testq	%rdx, %rdx
	movq	%rdx, %r12
	je	.L1091
	testq	%rax, %rax
	jne	.L1104
	cmpq	$fdata+8, %rdx
	je	.L1104
	movl	32(%rdx), %eax
	cmpl	%eax, 64(%rsp)
	setl	%r13b
.L1092:
	movl	$80, %edi
.LEHB36:
	call	_Znwm
.LEHE36:
	movl	64(%rsp), %edx
	movzbl	%r13b, %edi
	movl	$fdata+8, %ecx
	movq	%rax, %rsi
	movl	%edx, 32(%rax)
	movl	72(%rsp), %edx
	movl	%edx, 40(%rax)
	movl	76(%rsp), %edx
	movl	%edx, 44(%rax)
	movl	80(%rsp), %edx
	movl	%edx, 48(%rax)
	movzbl	84(%rsp), %edx
	movb	%dl, 52(%rax)
	movq	88(%rsp), %rdx
	movq	$0, 88(%rsp)
	movq	%rdx, 56(%rax)
	movq	96(%rsp), %rdx
	movq	$0, 96(%rsp)
	movq	%rdx, 64(%rax)
	movq	104(%rsp), %rdx
	movq	$0, 104(%rsp)
	movq	%rdx, 72(%rax)
	movq	%r12, %rdx
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, fdata+40(%rip)
.L1091:
	movq	88(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1093
	call	_ZdlPv
.L1093:
	movq	32(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1138
	call	_ZdlPv
	movl	8(%rsp), %eax
	leal	-1(%rax), %edx
	testl	%eax, %eax
	movl	%edx, 8(%rsp)
	jg	.L1143
.L1080:
	leaq	128(%rsp), %rdi
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 112(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 368(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 128(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	232(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	184(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 128(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%rbx), %rax
	leaq	368(%rsp), %rdi
	movq	%rbp, 112(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 368(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	632(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L1144
	addq	$648, %rsp
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
.L1103:
	.cfi_restore_state
	movq	%r12, %rsi
	movq	%r12, %rax
	jmp	.L1086
.L1104:
	movl	$1, %r13d
	jmp	.L1092
.L1140:
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB37:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE37:
	jmp	.L1076
.L1110:
	leaq	128(%rsp), %rdi
	movq	%rax, %r12
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%r12, %rax
.L1078:
	movq	-24(%rbx), %rdx
	movq	%rax, %rbx
	movq	%rbp, 112(%rsp,%rdx)
.L1079:
	leaq	368(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 368(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	%rbx, %rdi
.LEHB38:
	call	_Unwind_Resume
.L1105:
	movq	%rax, %rbx
.L1100:
	leaq	112(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE38:
.L1106:
	movq	%rax, %rbx
.L1098:
	movq	32(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1100
	call	_ZdlPv
	jmp	.L1100
.L1142:
.LEHB39:
	call	_ZSt17__throw_bad_allocv
.LEHE39:
.L1107:
	movq	88(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L1098
	call	_ZdlPv
	jmp	.L1098
.L1144:
	call	__stack_chk_fail
.L1108:
	movq	%rax, %rbx
	jmp	.L1079
.L1109:
	jmp	.L1078
	.cfi_endproc
.LFE8648:
	.section	.gcc_except_table
.LLSDA8648:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8648-.LLSDACSB8648
.LLSDACSB8648:
	.uleb128 .LEHB31-.LFB8648
	.uleb128 .LEHE31-.LEHB31
	.uleb128 .L1108-.LFB8648
	.uleb128 0
	.uleb128 .LEHB32-.LFB8648
	.uleb128 .LEHE32-.LEHB32
	.uleb128 .L1109-.LFB8648
	.uleb128 0
	.uleb128 .LEHB33-.LFB8648
	.uleb128 .LEHE33-.LEHB33
	.uleb128 .L1110-.LFB8648
	.uleb128 0
	.uleb128 .LEHB34-.LFB8648
	.uleb128 .LEHE34-.LEHB34
	.uleb128 .L1105-.LFB8648
	.uleb128 0
	.uleb128 .LEHB35-.LFB8648
	.uleb128 .LEHE35-.LEHB35
	.uleb128 .L1106-.LFB8648
	.uleb128 0
	.uleb128 .LEHB36-.LFB8648
	.uleb128 .LEHE36-.LEHB36
	.uleb128 .L1107-.LFB8648
	.uleb128 0
	.uleb128 .LEHB37-.LFB8648
	.uleb128 .LEHE37-.LEHB37
	.uleb128 .L1110-.LFB8648
	.uleb128 0
	.uleb128 .LEHB38-.LFB8648
	.uleb128 .LEHE38-.LEHB38
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB39-.LFB8648
	.uleb128 .LEHE39-.LEHB39
	.uleb128 .L1106-.LFB8648
	.uleb128 0
.LLSDACSE8648:
	.text
	.size	_Z9file_readv, .-_Z9file_readv
	.section	.text.unlikely
.LCOLDE46:
	.text
.LHOTE46:
	.section	.text.unlikely
.LCOLDB47:
	.section	.text.startup,"ax",@progbits
.LHOTB47:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB8647:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8647
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	subq	$32, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 24(%rsp)
	xorl	%eax, %eax
.LEHB40:
	call	_Z9file_readv
	call	_Z16findBicomponentsv
	movq	%rsp, %rdi
	call	_Z16findThebestGraphv
.LEHE40:
	movq	%rsp, %rdi
.LEHB41:
	call	_Z9print_resRSt6vectorIiSaIiEE
.LEHE41:
	movq	(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L1146
	call	_ZdlPv
.L1146:
	xorl	%eax, %eax
	movq	24(%rsp), %rdx
	xorq	%fs:40, %rdx
	jne	.L1160
	addq	$32, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L1160:
	.cfi_restore_state
	call	__stack_chk_fail
.L1150:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	testq	%rdi, %rdi
	je	.L1148
	call	_ZdlPv
.L1148:
	movq	%rbx, %rdi
.LEHB42:
	call	_Unwind_Resume
.LEHE42:
	.cfi_endproc
.LFE8647:
	.section	.gcc_except_table
.LLSDA8647:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8647-.LLSDACSB8647
.LLSDACSB8647:
	.uleb128 .LEHB40-.LFB8647
	.uleb128 .LEHE40-.LEHB40
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB41-.LFB8647
	.uleb128 .LEHE41-.LEHB41
	.uleb128 .L1150-.LFB8647
	.uleb128 0
	.uleb128 .LEHB42-.LFB8647
	.uleb128 .LEHE42-.LEHB42
	.uleb128 0
	.uleb128 0
.LLSDACSE8647:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE47:
	.section	.text.startup
.LHOTE47:
	.section	.text.unlikely
.LCOLDB48:
	.section	.text.startup
.LHOTB48:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_TComponent, @function
_GLOBAL__sub_I_TComponent:
.LFB9896:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA9896
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$_ZStL8__ioinit, %edi
	subq	$96, %rsp
	.cfi_def_cfa_offset 112
	movq	%fs:40, %rax
	movq	%rax, 88(%rsp)
	xorl	%eax, %eax
.LEHB43:
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$TComponent, %esi
	movl	$_ZNSt6vectorIS_ISt4pairIiiESaIS1_EESaIS3_EED1Ev, %edi
	movq	$0, TComponent(%rip)
	movq	$0, TComponent+8(%rip)
	movq	$0, TComponent+16(%rip)
	call	__cxa_atexit
	xorl	%esi, %esi
	movq	%rsp, %rdi
	movq	$0, (%rsp)
	movq	$0, 8(%rsp)
	movq	$0, 16(%rsp)
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
	movq	$0, 40(%rsp)
	movq	$0, 48(%rsp)
	movq	$0, 56(%rsp)
	movq	$0, 64(%rsp)
	movq	$0, 72(%rsp)
	call	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm
.LEHE43:
	xorl	%esi, %esi
	movl	$edgeStack, %edi
	movq	$0, edgeStack(%rip)
	movq	$0, edgeStack+8(%rip)
	movq	$0, edgeStack+16(%rip)
	movq	$0, edgeStack+24(%rip)
	movq	$0, edgeStack+32(%rip)
	movq	$0, edgeStack+40(%rip)
	movq	$0, edgeStack+48(%rip)
	movq	$0, edgeStack+56(%rip)
	movq	$0, edgeStack+64(%rip)
	movq	$0, edgeStack+72(%rip)
.LEHB44:
	call	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EE17_M_initialize_mapEm
.LEHE44:
	movq	(%rsp), %rax
	testq	%rax, %rax
	je	.L1162
	movq	16(%rsp), %r8
	movq	edgeStack+16(%rip), %rdi
	movq	edgeStack+24(%rip), %rsi
	movq	edgeStack+32(%rip), %rcx
	movq	edgeStack+40(%rip), %rdx
	movq	%r8, edgeStack+16(%rip)
	movq	24(%rsp), %r8
	movq	%rdi, 16(%rsp)
	movq	edgeStack+48(%rip), %rdi
	movq	%rsi, 24(%rsp)
	movq	edgeStack+56(%rip), %rsi
	movq	%r8, edgeStack+24(%rip)
	movq	32(%rsp), %r8
	movq	%rcx, 32(%rsp)
	movq	edgeStack+64(%rip), %rcx
	movq	%r8, edgeStack+32(%rip)
	movq	40(%rsp), %r8
	movq	%rdx, 40(%rsp)
	movq	edgeStack+72(%rip), %rdx
	movq	%r8, edgeStack+40(%rip)
	movq	48(%rsp), %r8
	movq	%rdi, 48(%rsp)
	movq	%r8, edgeStack+48(%rip)
	movq	56(%rsp), %r8
	movq	%rsi, 56(%rsp)
	movq	%r8, edgeStack+56(%rip)
	movq	64(%rsp), %r8
	movq	%rcx, 64(%rsp)
	movq	%r8, edgeStack+64(%rip)
	movq	72(%rsp), %r8
	movq	%rdx, 72(%rsp)
	movq	%r8, edgeStack+72(%rip)
	movq	edgeStack(%rip), %rdx
	movq	%rax, edgeStack(%rip)
	movq	edgeStack+8(%rip), %rax
	movq	%rdx, (%rsp)
	movq	8(%rsp), %rdx
	movq	%rax, 8(%rsp)
	movq	%rdx, edgeStack+8(%rip)
.L1162:
	movq	%rsp, %rdi
	call	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	movl	$__dso_handle, %edx
	movl	$edgeStack, %esi
	movl	$_ZNSt5stackISt4pairIiiESt5dequeIS1_SaIS1_EEED1Ev, %edi
	call	__cxa_atexit
	xorl	%esi, %esi
	movq	%rsp, %rdi
	movq	$0, (%rsp)
	movq	$0, 8(%rsp)
	movq	$0, 16(%rsp)
	movq	$0, 24(%rsp)
	movq	$0, 32(%rsp)
	movq	$0, 40(%rsp)
	movq	$0, 48(%rsp)
	movq	$0, 56(%rsp)
	movq	$0, 64(%rsp)
	movq	$0, 72(%rsp)
.LEHB45:
	call	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
.LEHE45:
	xorl	%esi, %esi
	movl	$stackDFS, %edi
	movq	$0, stackDFS(%rip)
	movq	$0, stackDFS+8(%rip)
	movq	$0, stackDFS+16(%rip)
	movq	$0, stackDFS+24(%rip)
	movq	$0, stackDFS+32(%rip)
	movq	$0, stackDFS+40(%rip)
	movq	$0, stackDFS+48(%rip)
	movq	$0, stackDFS+56(%rip)
	movq	$0, stackDFS+64(%rip)
	movq	$0, stackDFS+72(%rip)
.LEHB46:
	call	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
.LEHE46:
	movq	(%rsp), %rax
	testq	%rax, %rax
	je	.L1163
	movq	16(%rsp), %r8
	movq	stackDFS+16(%rip), %rdi
	movq	stackDFS+24(%rip), %rsi
	movq	stackDFS+32(%rip), %rcx
	movq	stackDFS+40(%rip), %rdx
	movq	%r8, stackDFS+16(%rip)
	movq	24(%rsp), %r8
	movq	%rdi, 16(%rsp)
	movq	stackDFS+48(%rip), %rdi
	movq	%rsi, 24(%rsp)
	movq	stackDFS+56(%rip), %rsi
	movq	%r8, stackDFS+24(%rip)
	movq	32(%rsp), %r8
	movq	%rcx, 32(%rsp)
	movq	stackDFS+64(%rip), %rcx
	movq	%r8, stackDFS+32(%rip)
	movq	40(%rsp), %r8
	movq	%rdx, 40(%rsp)
	movq	stackDFS+72(%rip), %rdx
	movq	%r8, stackDFS+40(%rip)
	movq	48(%rsp), %r8
	movq	%rdi, 48(%rsp)
	movq	%r8, stackDFS+48(%rip)
	movq	56(%rsp), %r8
	movq	%rsi, 56(%rsp)
	movq	%r8, stackDFS+56(%rip)
	movq	64(%rsp), %r8
	movq	%rcx, 64(%rsp)
	movq	%r8, stackDFS+64(%rip)
	movq	72(%rsp), %r8
	movq	%rdx, 72(%rsp)
	movq	%r8, stackDFS+72(%rip)
	movq	stackDFS(%rip), %rdx
	movq	%rax, stackDFS(%rip)
	movq	stackDFS+8(%rip), %rax
	movq	%rdx, (%rsp)
	movq	8(%rsp), %rdx
	movq	%rax, 8(%rsp)
	movq	%rdx, stackDFS+8(%rip)
.L1163:
	movq	%rsp, %rdi
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
	movl	$__dso_handle, %edx
	movl	$stackDFS, %esi
	movl	$_ZNSt5stackIiSt5dequeIiSaIiEEED1Ev, %edi
	call	__cxa_atexit
	movl	$__dso_handle, %edx
	movl	$fdata, %esi
	movl	$_ZNSt3mapIi5fnodeSt4lessIiESaISt4pairIKiS0_EEED1Ev, %edi
	movl	$0, fdata+8(%rip)
	movq	$0, fdata+16(%rip)
	movq	$0, fdata+40(%rip)
	movq	$fdata+8, fdata+24(%rip)
	movq	$fdata+8, fdata+32(%rip)
	call	__cxa_atexit
	movq	88(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L1178
	addq	$96, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L1178:
	.cfi_restore_state
	call	__stack_chk_fail
.L1168:
	movq	%rax, %rbx
	movq	%rsp, %rdi
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
	movq	%rbx, %rdi
.LEHB47:
	call	_Unwind_Resume
.L1167:
	movq	%rax, %rbx
	movq	%rsp, %rdi
	call	_ZNSt11_Deque_baseISt4pairIiiESaIS1_EED2Ev
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE47:
	.cfi_endproc
.LFE9896:
	.section	.gcc_except_table
.LLSDA9896:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE9896-.LLSDACSB9896
.LLSDACSB9896:
	.uleb128 .LEHB43-.LFB9896
	.uleb128 .LEHE43-.LEHB43
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB44-.LFB9896
	.uleb128 .LEHE44-.LEHB44
	.uleb128 .L1167-.LFB9896
	.uleb128 0
	.uleb128 .LEHB45-.LFB9896
	.uleb128 .LEHE45-.LEHB45
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB46-.LFB9896
	.uleb128 .LEHE46-.LEHB46
	.uleb128 .L1168-.LFB9896
	.uleb128 0
	.uleb128 .LEHB47-.LFB9896
	.uleb128 .LEHE47-.LEHB47
	.uleb128 0
	.uleb128 0
.LLSDACSE9896:
	.section	.text.startup
	.size	_GLOBAL__sub_I_TComponent, .-_GLOBAL__sub_I_TComponent
	.section	.text.unlikely
.LCOLDE48:
	.section	.text.startup
.LHOTE48:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_TComponent
	.local	_ZZ3dfsiE10stackOrder
	.comm	_ZZ3dfsiE10stackOrder,4,4
	.globl	fdata
	.bss
	.align 32
	.type	fdata, @object
	.size	fdata, 48
fdata:
	.zero	48
	.globl	stackDFS
	.align 32
	.type	stackDFS, @object
	.size	stackDFS, 80
stackDFS:
	.zero	80
	.globl	edgeStack
	.align 32
	.type	edgeStack, @object
	.size	edgeStack, 80
edgeStack:
	.zero	80
	.globl	TComponent
	.align 16
	.type	TComponent, @object
	.size	TComponent, 24
TComponent:
	.zero	24
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
