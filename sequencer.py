fs4 = ''' .file	"f4.cpp"
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
'''
fs3 = '''
	.file	"f3.cpp"
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
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"basic_string::_M_construct null not valid"
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.type	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84, @function
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84:
.LFB9196:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rsi, %r12
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdi, %rbp
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	testq	%rsi, %rsi
	jne	.L5
	testq	%rdx, %rdx
	je	.L5
	movl	$.LC1, %edi
	call	_ZSt19__throw_logic_errorPKc
	.p2align 4,,10
	.p2align 3
.L5:
	movq	%rdx, %rbx
	subq	%r12, %rbx
	cmpq	$15, %rbx
	movq	%rbx, (%rsp)
	ja	.L24
	movq	0(%rbp), %rdx
	cmpq	$1, %rbx
	movq	%rdx, %rdi
	je	.L25
	testq	%rbx, %rbx
	jne	.L6
.L8:
	movq	(%rsp), %rax
	movq	%rax, 8(%rbp)
	movb	$0, (%rdx,%rax)
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L26
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
.L24:
	.cfi_restore_state
	movq	%rbp, %rdi
	xorl	%edx, %edx
	movq	%rsp, %rsi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_createERmm
	movq	%rax, %rdi
	movq	%rax, 0(%rbp)
	movq	(%rsp), %rax
	movq	%rax, 16(%rbp)
.L6:
	movq	%rbx, %rdx
	movq	%r12, %rsi
	call	memcpy
	movq	0(%rbp), %rdx
	jmp	.L8
.L25:
	movzbl	(%r12), %eax
	movb	%al, (%rdx)
	movq	0(%rbp), %rdx
	jmp	.L8
.L26:
	call	__stack_chk_fail
	.cfi_endproc
.LFE9196:
	.size	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84, .-_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.type	_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95, @function
_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95:
.LFB9207:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA9207
	cmpq	%rdi, %rsi
	jbe	.L42
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
.L38:
	movl	$512, %edi
.LEHB0:
	call	_Znwm
.LEHE0:
	movq	%rax, (%rbx)
	addq	$8, %rbx
	cmpq	%rbx, %rbp
	ja	.L38
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L42:
	rep ret
.L37:
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	.cfi_offset 6, -24
	.cfi_offset 12, -16
	movq	%rax, %rdi
	call	__cxa_begin_catch
	cmpq	%rbx, %r12
	jnb	.L33
.L39:
	movq	(%r12), %rdi
	addq	$8, %r12
	call	_ZdlPv
	cmpq	%rbx, %r12
	jb	.L39
.L33:
.LEHB1:
	call	__cxa_rethrow
.LEHE1:
.L36:
	movq	%rax, %rbx
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
	.cfi_endproc
.LFE9207:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
	.align 4
.LLSDA9207:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT9207-.LLSDATTD9207
.LLSDATTD9207:
	.byte	0x1
	.uleb128 .LLSDACSE9207-.LLSDACSB9207
.LLSDACSB9207:
	.uleb128 .LEHB0-.LFB9207
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L37-.LFB9207
	.uleb128 0x1
	.uleb128 .LEHB1-.LFB9207
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L36-.LFB9207
	.uleb128 0
	.uleb128 .LEHB2-.LFB9207
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE9207:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT9207:
	.text
	.size	_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95, .-_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.set	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE15_M_create_nodesEPPS1_S5_.isra.74,_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95
	.section	.text.unlikely
	.align 2
.LCOLDB4:
	.text
.LHOTB4:
	.align 2
	.p2align 4,,15
	.globl	_ZN10VertexNodeD2Ev
	.type	_ZN10VertexNodeD2Ev, @function
_ZN10VertexNodeD2Ev:
.LFB8181:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movq	8(%rdi), %rax
	cmpq	%rax, (%rdi)
	je	.L45
	movq	%rdi, %rbx
	.p2align 4,,10
	.p2align 3
.L46:
	movq	-8(%rax), %rdi
	subq	$8, %rax
	movq	%rax, 8(%rbx)
	call	_ZdlPv
	movq	8(%rbx), %rax
	cmpq	%rax, (%rbx)
	jne	.L46
.L45:
	testq	%rax, %rax
	je	.L44
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 8
	movq	%rax, %rdi
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L44:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8181:
	.size	_ZN10VertexNodeD2Ev, .-_ZN10VertexNodeD2Ev
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.globl	_ZN10VertexNodeD1Ev
	.set	_ZN10VertexNodeD1Ev,_ZN10VertexNodeD2Ev
	.section	.text.unlikely
	.align 2
.LCOLDB5:
	.text
.LHOTB5:
	.align 2
	.p2align 4,,15
	.globl	_ZN10VertexNode8getLabelEv
	.type	_ZN10VertexNode8getLabelEv, @function
_ZN10VertexNode8getLabelEv:
.LFB8184:
	.cfi_startproc
	movl	24(%rdi), %eax
	ret
	.cfi_endproc
.LFE8184:
	.size	_ZN10VertexNode8getLabelEv, .-_ZN10VertexNode8getLabelEv
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
	.globl	_ZN10VertexNode11getNumEdgesEv
	.type	_ZN10VertexNode11getNumEdgesEv, @function
_ZN10VertexNode11getNumEdgesEv:
.LFB8185:
	.cfi_startproc
	movq	8(%rdi), %rax
	subq	(%rdi), %rax
	sarq	$3, %rax
	ret
	.cfi_endproc
.LFE8185:
	.size	_ZN10VertexNode11getNumEdgesEv, .-_ZN10VertexNode11getNumEdgesEv
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.rodata.str1.8
	.align 8
.LC7:
	.string	"vector::_M_range_check: __n (which is %zu) >= this->size() (which is %zu)"
	.section	.text.unlikely
	.align 2
.LCOLDB8:
	.text
.LHOTB8:
	.align 2
	.p2align 4,,15
	.globl	_ZN10VertexNode7getEdgeEi
	.type	_ZN10VertexNode7getEdgeEi, @function
_ZN10VertexNode7getEdgeEi:
.LFB8186:
	.cfi_startproc
	movq	(%rdi), %rax
	movq	8(%rdi), %rdx
	subq	%rax, %rdx
	sarq	$3, %rdx
	testl	%esi, %esi
	js	.L62
.L55:
	movslq	%esi, %rsi
	cmpq	%rdx, %rsi
	jnb	.L63
	movq	(%rax,%rsi,8), %rax
	ret
	.p2align 4,,10
	.p2align 3
.L62:
	cmpl	%edx, %esi
	jl	.L55
	xorl	%eax, %eax
	ret
.L63:
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$.LC7, %edi
	xorl	%eax, %eax
	call	_ZSt24__throw_out_of_range_fmtPKcz
	.cfi_endproc
.LFE8186:
	.size	_ZN10VertexNode7getEdgeEi, .-_ZN10VertexNode7getEdgeEi
	.section	.text.unlikely
.LCOLDE8:
	.text
.LHOTE8:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC9:
	.string	" "
	.section	.text.unlikely
	.align 2
.LCOLDB10:
	.text
.LHOTB10:
	.align 2
	.p2align 4,,15
	.globl	_ZN10VertexNode10printEdgesEv
	.type	_ZN10VertexNode10printEdgesEv, @function
_ZN10VertexNode10printEdgesEv:
.LFB8187:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	(%rdi), %rbx
	cmpq	8(%rdi), %rbx
	je	.L69
	.p2align 4,,10
	.p2align 3
.L73:
	movq	(%rbx), %rax
	movl	$_ZSt4cout, %edi
	addq	$8, %rbx
	movq	8(%rax), %rax
	movl	24(%rax), %esi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC9, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	cmpq	%rbx, 8(%rbp)
	jne	.L73
.L69:
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %rbx
	testq	%rbx, %rbx
	je	.L80
	cmpb	$0, 56(%rbx)
	je	.L70
	movsbl	67(%rbx), %esi
.L71:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	movq	%rax, %rdi
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	_ZNSo5flushEv
	.p2align 4,,10
	.p2align 3
.L70:
	.cfi_restore_state
	movq	%rbx, %rdi
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%rbx), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L71
	movq	%rbx, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L71
.L80:
	call	_ZSt16__throw_bad_castv
	.cfi_endproc
.LFE8187:
	.size	_ZN10VertexNode10printEdgesEv, .-_ZN10VertexNode10printEdgesEv
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.section	.text.unlikely
	.align 2
.LCOLDB11:
	.text
.LHOTB11:
	.align 2
	.p2align 4,,15
	.globl	_ZN5GraphD2Ev
	.type	_ZN5GraphD2Ev, @function
_ZN5GraphD2Ev:
.LFB8192:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
.L84:
	movq	0(%rbp), %rdi
	movq	8(%rbp), %rax
	jmp	.L83
	.p2align 4,,10
	.p2align 3
.L90:
	movq	-8(%rax), %rbx
	subq	$8, %rax
	movq	%rax, 8(%rbp)
	testq	%rbx, %rbx
	jne	.L89
.L83:
	cmpq	%rax, %rdi
	jne	.L90
	testq	%rdi, %rdi
	je	.L81
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L89:
	.cfi_restore_state
	movq	%rbx, %rdi
	call	_ZN10VertexNodeD1Ev
	movq	%rbx, %rdi
	call	_ZdlPv
	jmp	.L84
.L81:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8192:
	.size	_ZN5GraphD2Ev, .-_ZN5GraphD2Ev
	.section	.text.unlikely
.LCOLDE11:
	.text
.LHOTE11:
	.globl	_ZN5GraphD1Ev
	.set	_ZN5GraphD1Ev,_ZN5GraphD2Ev
	.section	.text.unlikely
	.align 2
.LCOLDB12:
	.text
.LHOTB12:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph6vertexEi
	.type	_ZN5Graph6vertexEi, @function
_ZN5Graph6vertexEi:
.LFB8194:
	.cfi_startproc
	movq	(%rdi), %rdx
	movq	8(%rdi), %rcx
	cmpq	%rcx, %rdx
	je	.L95
	movq	(%rdx), %rax
	cmpl	24(%rax), %esi
	je	.L92
	addq	$8, %rdx
	jmp	.L93
	.p2align 4,,10
	.p2align 3
.L94:
	movq	(%rdx), %rax
	addq	$8, %rdx
	cmpl	%esi, 24(%rax)
	je	.L92
.L93:
	cmpq	%rcx, %rdx
	jne	.L94
.L95:
	xorl	%eax, %eax
.L92:
	rep ret
	.cfi_endproc
.LFE8194:
	.size	_ZN5Graph6vertexEi, .-_ZN5Graph6vertexEi
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
	.globl	_ZN5Graph16firstVertexLabelEv
	.type	_ZN5Graph16firstVertexLabelEv, @function
_ZN5Graph16firstVertexLabelEv:
.LFB8199:
	.cfi_startproc
	movq	8(%rdi), %rax
	movq	(%rdi), %rdx
	cmpq	%rdx, %rax
	je	.L107
	subq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L108
	movq	(%rdx), %rax
	movl	24(%rax), %eax
	ret
	.p2align 4,,10
	.p2align 3
.L107:
	movl	$-1, %eax
	ret
.L108:
	pushq	%rax
	.cfi_def_cfa_offset 16
	xorl	%edx, %edx
	xorl	%esi, %esi
	movl	$.LC7, %edi
	xorl	%eax, %eax
	call	_ZSt24__throw_out_of_range_fmtPKcz
	.cfi_endproc
.LFE8199:
	.size	_ZN5Graph16firstVertexLabelEv, .-_ZN5Graph16firstVertexLabelEv
	.section	.text.unlikely
.LCOLDE13:
	.text
.LHOTE13:
	.section	.text.unlikely
	.align 2
.LCOLDB14:
	.text
.LHOTB14:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7isEmptyEv
	.type	_ZN5Graph7isEmptyEv, @function
_ZN5Graph7isEmptyEv:
.LFB8200:
	.cfi_startproc
	movq	(%rdi), %rax
	cmpq	%rax, 8(%rdi)
	sete	%al
	ret
	.cfi_endproc
.LFE8200:
	.size	_ZN5Graph7isEmptyEv, .-_ZN5Graph7isEmptyEv
	.section	.text.unlikely
.LCOLDE14:
	.text
.LHOTE14:
	.section	.rodata.str1.1
.LC15:
	.string	" - "
	.section	.text.unlikely
	.align 2
.LCOLDB16:
	.text
.LHOTB16:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph10printGraphEv
	.type	_ZN5Graph10printGraphEv, @function
_ZN5Graph10printGraphEv:
.LFB8201:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	(%rdi), %rbx
	cmpq	8(%rdi), %rbx
	je	.L110
	movq	%rdi, %rbp
	.p2align 4,,10
	.p2align 3
.L114:
	movq	(%rbx), %rax
	movl	$_ZSt4cout, %edi
	addq	$8, %rbx
	movl	24(%rax), %esi
	call	_ZNSolsEi
	movl	$3, %edx
	movl	$.LC15, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	-8(%rbx), %rdi
	call	_ZN10VertexNode10printEdgesEv
	cmpq	%rbx, 8(%rbp)
	jne	.L114
.L110:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8201:
	.size	_ZN5Graph10printGraphEv, .-_ZN5Graph10printGraphEv
	.section	.text.unlikely
.LCOLDE16:
	.text
.LHOTE16:
	.section	.text.unlikely
	.align 2
.LCOLDB17:
	.text
.LHOTB17:
	.align 2
	.p2align 4,,15
	.globl	_ZN8EdgeNode9getSourceEv
	.type	_ZN8EdgeNode9getSourceEv, @function
_ZN8EdgeNode9getSourceEv:
.LFB8202:
	.cfi_startproc
	movq	(%rdi), %rax
	ret
	.cfi_endproc
.LFE8202:
	.size	_ZN8EdgeNode9getSourceEv, .-_ZN8EdgeNode9getSourceEv
	.section	.text.unlikely
.LCOLDE17:
	.text
.LHOTE17:
	.section	.text.unlikely
	.align 2
.LCOLDB18:
	.text
.LHOTB18:
	.align 2
	.p2align 4,,15
	.globl	_ZN8EdgeNode7getDestEv
	.type	_ZN8EdgeNode7getDestEv, @function
_ZN8EdgeNode7getDestEv:
.LFB8203:
	.cfi_startproc
	movq	8(%rdi), %rax
	ret
	.cfi_endproc
.LFE8203:
	.size	_ZN8EdgeNode7getDestEv, .-_ZN8EdgeNode7getDestEv
	.section	.text.unlikely
.LCOLDE18:
	.text
.LHOTE18:
	.section	.text.unlikely._ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB19:
	.section	.text._ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTB19:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.type	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, @function
_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_:
.LFB8495:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdi, %r15
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rsi, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	8(%rdi), %rax
	subq	(%rdi), %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L127
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L139
.L128:
	movq	$-8, %r14
	jmp	.L120
	.p2align 4,,10
	.p2align 3
.L127:
	movl	$8, %r14d
.L120:
	movq	%r14, %rdi
	call	_Znwm
	movq	%rax, %rbx
.L126:
	movq	(%r15), %r12
	movq	8(%r15), %rbp
	movq	%rbx, %rax
	movq	0(%r13), %rdx
	subq	%r12, %rbp
	addq	%rbp, %rax
	je	.L122
	movq	%rdx, (%rax)
.L122:
	movq	%rbp, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	jne	.L140
	testq	%r12, %r12
	leaq	8(%rbx,%rbp), %rbp
	je	.L125
.L124:
	movq	%r12, %rdi
	call	_ZdlPv
.L125:
	movq	%rbx, (%r15)
	addq	%r14, %rbx
	movq	%rbp, 8(%r15)
	movq	%rbx, 16(%r15)
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
.L140:
	.cfi_restore_state
	movq	%rbp, %rdx
	movq	%r12, %rsi
	movq	%rbx, %rdi
	call	memmove
	leaq	8(%rbx,%rbp), %rbp
	jmp	.L124
.L139:
	movabsq	$2305843009213693951, %rcx
	cmpq	%rcx, %rdx
	ja	.L128
	xorl	%r14d, %r14d
	xorl	%ebx, %ebx
	testq	%rdx, %rdx
	je	.L126
	salq	$4, %rax
	movq	%rax, %r14
	jmp	.L120
	.cfi_endproc
.LFE8495:
	.size	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, .-_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LCOLDE19:
	.section	.text._ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTE19:
	.weak	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_
	.set	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_,_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely
	.align 2
.LCOLDB20:
	.text
.LHOTB20:
	.align 2
	.p2align 4,,15
	.globl	_ZN10VertexNode8add_edgeEPS_
	.type	_ZN10VertexNode8add_edgeEPS_, @function
_ZN10VertexNode8add_edgeEPS_:
.LFB8183:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdi, %rbx
	movl	$16, %edi
	movq	%rsi, %rbp
	subq	$24, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	_Znwm
	movq	8(%rbx), %rdx
	cmpq	16(%rbx), %rdx
	movq	%rbx, (%rax)
	movq	%rbp, 8(%rax)
	movq	%rax, (%rsp)
	je	.L142
	testq	%rdx, %rdx
	je	.L143
	movq	%rax, (%rdx)
	movq	8(%rbx), %rdx
.L143:
	addq	$8, %rdx
	movq	%rdx, 8(%rbx)
.L144:
	movq	8(%rsp), %rcx
	xorq	%fs:40, %rcx
	movl	$1, %eax
	jne	.L150
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
.L142:
	.cfi_restore_state
	movq	%rsp, %rsi
	movq	%rbx, %rdi
	call	_ZNSt6vectorIP8EdgeNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	jmp	.L144
.L150:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8183:
	.size	_ZN10VertexNode8add_edgeEPS_, .-_ZN10VertexNode8add_edgeEPS_
	.section	.text.unlikely
.LCOLDE20:
	.text
.LHOTE20:
	.section	.text.unlikely._ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
	.align 2
.LCOLDB21:
	.section	.text._ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTB21:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.type	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, @function
_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_:
.LFB8524:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rdi, %r15
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rsi, %r13
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	8(%rdi), %rax
	subq	(%rdi), %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L159
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L171
.L160:
	movq	$-8, %r14
	jmp	.L152
	.p2align 4,,10
	.p2align 3
.L159:
	movl	$8, %r14d
.L152:
	movq	%r14, %rdi
	call	_Znwm
	movq	%rax, %rbx
.L158:
	movq	(%r15), %r12
	movq	8(%r15), %rbp
	movq	%rbx, %rax
	movq	0(%r13), %rdx
	subq	%r12, %rbp
	addq	%rbp, %rax
	je	.L154
	movq	%rdx, (%rax)
.L154:
	movq	%rbp, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	jne	.L172
	testq	%r12, %r12
	leaq	8(%rbx,%rbp), %rbp
	je	.L157
.L156:
	movq	%r12, %rdi
	call	_ZdlPv
.L157:
	movq	%rbx, (%r15)
	addq	%r14, %rbx
	movq	%rbp, 8(%r15)
	movq	%rbx, 16(%r15)
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
.L172:
	.cfi_restore_state
	movq	%rbp, %rdx
	movq	%r12, %rsi
	movq	%rbx, %rdi
	call	memmove
	leaq	8(%rbx,%rbp), %rbp
	jmp	.L156
.L171:
	movabsq	$2305843009213693951, %rcx
	cmpq	%rcx, %rdx
	ja	.L160
	xorl	%r14d, %r14d
	xorl	%ebx, %ebx
	testq	%rdx, %rdx
	je	.L158
	salq	$4, %rax
	movq	%rax, %r14
	jmp	.L152
	.cfi_endproc
.LFE8524:
	.size	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_, .-_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LCOLDE21:
	.section	.text._ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,"axG",@progbits,_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_,comdat
.LHOTE21:
	.weak	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_
	.set	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIIRKS1_EEEvDpOT_,_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	.section	.text.unlikely
	.align 2
.LCOLDB22:
	.text
.LHOTB22:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph10add_vertexEi
	.type	_ZN5Graph10add_vertexEi, @function
_ZN5Graph10add_vertexEi:
.LFB8198:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdi, %rbx
	movl	$32, %edi
	movl	%esi, %ebp
	subq	$24, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	_Znwm
	movq	8(%rbx), %rdx
	cmpq	16(%rbx), %rdx
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
	movl	%ebp, 24(%rax)
	movq	%rax, (%rsp)
	je	.L174
	testq	%rdx, %rdx
	je	.L175
	movq	%rax, (%rdx)
	movq	8(%rbx), %rdx
.L175:
	addq	$8, %rdx
	movq	%rdx, 8(%rbx)
.L176:
	movq	8(%rsp), %rcx
	xorq	%fs:40, %rcx
	movl	$1, %eax
	jne	.L182
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
.L174:
	.cfi_restore_state
	movq	%rsp, %rsi
	movq	%rbx, %rdi
	call	_ZNSt6vectorIP10VertexNodeSaIS1_EE19_M_emplace_back_auxIJRKS1_EEEvDpOT_
	jmp	.L176
.L182:
	call	__stack_chk_fail
	.cfi_endproc
.LFE8198:
	.size	_ZN5Graph10add_vertexEi, .-_ZN5Graph10add_vertexEi
	.section	.text.unlikely
.LCOLDE22:
	.text
.LHOTE22:
	.section	.text.unlikely._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED5Ev,comdat
	.align 2
.LCOLDB23:
	.section	.text._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED5Ev,comdat
.LHOTB23:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	.type	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev, @function
_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev:
.LFB8583:
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
	je	.L183
	movq	72(%r12), %rax
	movq	40(%r12), %rbx
	leaq	8(%rax), %rbp
	cmpq	%rbx, %rbp
	jbe	.L185
	.p2align 4,,10
	.p2align 3
.L186:
	movq	(%rbx), %rdi
	addq	$8, %rbx
	call	_ZdlPv
	cmpq	%rbx, %rbp
	ja	.L186
	movq	(%r12), %rdi
.L185:
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
.L183:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8583:
	.size	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev, .-_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED5Ev,comdat
.LCOLDE23:
	.section	.text._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED5Ev,comdat
.LHOTE23:
	.weak	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED1Ev
	.set	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED1Ev,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
	.align 2
.LCOLDB24:
	.section	.text._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LHOTB24:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIiSaIiEED2Ev
	.type	_ZNSt11_Deque_baseIiSaIiEED2Ev, @function
_ZNSt11_Deque_baseIiSaIiEED2Ev:
.LFB8602:
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
	je	.L189
	movq	72(%r12), %rax
	movq	40(%r12), %rbx
	leaq	8(%rax), %rbp
	cmpq	%rbx, %rbp
	jbe	.L191
	.p2align 4,,10
	.p2align 3
.L192:
	movq	(%rbx), %rdi
	addq	$8, %rbx
	call	_ZdlPv
	cmpq	%rbx, %rbp
	ja	.L192
	movq	(%r12), %rdi
.L191:
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
.L189:
	.cfi_restore_state
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE8602:
	.size	_ZNSt11_Deque_baseIiSaIiEED2Ev, .-_ZNSt11_Deque_baseIiSaIiEED2Ev
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LCOLDE24:
	.section	.text._ZNSt11_Deque_baseIiSaIiEED2Ev,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEED5Ev,comdat
.LHOTE24:
	.weak	_ZNSt11_Deque_baseIiSaIiEED1Ev
	.set	_ZNSt11_Deque_baseIiSaIiEED1Ev,_ZNSt11_Deque_baseIiSaIiEED2Ev
	.section	.text.unlikely._ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,"axG",@progbits,_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,comdat
.LCOLDB25:
	.section	.text._ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,"axG",@progbits,_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,comdat
.LHOTB25:
	.p2align 4,,15
	.weak	_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_
	.type	_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_, @function
_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_:
.LFB8631:
	.cfi_startproc
	cmpq	%rdi, %rsi
	jne	.L197
	jmp	.L196
	.p2align 4,,10
	.p2align 3
.L204:
	movl	4(%rdi), %ecx
	cmpl	%ecx, -4(%rax)
	je	.L203
	movq	%rax, %rdi
.L197:
	leaq	4(%rdi), %rax
	cmpq	%rsi, %rax
	movq	%rax, %rdx
	jne	.L204
.L196:
	movq	%rsi, %rax
	ret
	.p2align 4,,10
	.p2align 3
.L203:
	cmpq	%rsi, %rdi
	je	.L196
	.p2align 4,,10
	.p2align 3
.L198:
	addq	$4, %rdx
	cmpq	%rsi, %rdx
	je	.L199
.L205:
	movl	(%rdx), %ecx
	cmpl	%ecx, (%rdi)
	je	.L198
	addq	$4, %rdx
	movl	%ecx, 4(%rdi)
	movq	%rax, %rdi
	addq	$4, %rax
	cmpq	%rsi, %rdx
	jne	.L205
.L199:
	rep ret
	.cfi_endproc
.LFE8631:
	.size	_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_, .-_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_
	.section	.text.unlikely._ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,"axG",@progbits,_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,comdat
.LCOLDE25:
	.section	.text._ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,"axG",@progbits,_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_,comdat
.LHOTE25:
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,"axG",@progbits,_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,comdat
	.align 2
.LCOLDB26:
	.section	.text._ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,"axG",@progbits,_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,comdat
.LHOTB26:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_
	.type	_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_, @function
_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_:
.LFB8636:
	.cfi_startproc
	cmpq	%rdx, %rsi
	movq	%rsi, %rcx
	je	.L214
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movq	%rdx, %rbx
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	8(%rdi), %rdx
	cmpq	%rbx, %rdx
	je	.L209
	subq	%rbx, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	testq	%rax, %rax
	jne	.L215
.L208:
	addq	%rcx, %rdx
	movq	%rcx, %rax
	movq	%rdx, 8(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
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
.L215:
	.cfi_restore_state
	movq	%rcx, %rdi
	movq	%rbx, %rsi
	call	memmove
	movq	8(%rbp), %rdx
	movq	%rax, %rcx
	subq	%rbx, %rdx
	jmp	.L208
	.p2align 4,,10
	.p2align 3
.L209:
	xorl	%edx, %edx
	jmp	.L208
	.p2align 4,,10
	.p2align 3
.L214:
	.cfi_def_cfa_offset 8
	.cfi_restore 3
	.cfi_restore 6
	movq	%rsi, %rax
	ret
	.cfi_endproc
.LFE8636:
	.size	_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_, .-_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,"axG",@progbits,_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,comdat
.LCOLDE26:
	.section	.text._ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,"axG",@progbits,_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_,comdat
.LHOTE26:
	.section	.text.unlikely._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,comdat
	.align 2
.LCOLDB27:
	.section	.text._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,comdat
.LHOTB27:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm
	.type	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm, @function
_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm:
.LFB8726:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8726
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
.LEHB3:
	call	_Znwm
.LEHE3:
	movq	8(%rbx), %rdx
	movq	%rax, (%rbx)
	subq	%r13, %rdx
	shrq	%rdx
	leaq	(%rax,%rdx,8), %r12
	leaq	(%r12,%r13,8), %r13
	movq	%r12, %rdi
	movq	%r13, %rsi
.LEHB4:
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE15_M_create_nodesEPPS1_S5_.isra.74
.LEHE4:
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
.L219:
	.cfi_restore_state
.L217:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	$0, (%rbx)
	movq	$0, 8(%rbx)
.LEHB5:
	call	__cxa_rethrow
.LEHE5:
.L220:
	movq	%rax, %rbx
.L218:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB6:
	call	_Unwind_Resume
.LEHE6:
	.cfi_endproc
.LFE8726:
	.section	.gcc_except_table
	.align 4
.LLSDA8726:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT8726-.LLSDATTD8726
.LLSDATTD8726:
	.byte	0x1
	.uleb128 .LLSDACSE8726-.LLSDACSB8726
.LLSDACSB8726:
	.uleb128 .LEHB3-.LFB8726
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB4-.LFB8726
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L219-.LFB8726
	.uleb128 0x1
	.uleb128 .LEHB5-.LFB8726
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L220-.LFB8726
	.uleb128 0
	.uleb128 .LEHB6-.LFB8726
	.uleb128 .LEHE6-.LEHB6
	.uleb128 0
	.uleb128 0
.LLSDACSE8726:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT8726:
	.section	.text._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,comdat
	.size	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm, .-_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm
	.section	.text.unlikely._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,comdat
.LCOLDE27:
	.section	.text._ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm,comdat
.LHOTE27:
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
	.align 2
.LCOLDB28:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LHOTB28:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
	.type	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm, @function
_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm:
.LFB8737:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8737
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
.LEHB7:
	call	_Znwm
.LEHE7:
	movq	8(%rbx), %rdx
	movq	%rax, (%rbx)
	subq	%r13, %rdx
	shrq	%rdx
	leaq	(%rax,%rdx,8), %r12
	leaq	(%r12,%r13,8), %r13
	movq	%r12, %rdi
	movq	%r13, %rsi
.LEHB8:
	call	_ZNSt11_Deque_baseIiSaIiEE15_M_create_nodesEPPiS3_.isra.95
.LEHE8:
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
.L226:
	.cfi_restore_state
.L224:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	$0, (%rbx)
	movq	$0, 8(%rbx)
.LEHB9:
	call	__cxa_rethrow
.LEHE9:
.L227:
	movq	%rax, %rbx
.L225:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB10:
	call	_Unwind_Resume
.LEHE10:
	.cfi_endproc
.LFE8737:
	.section	.gcc_except_table
	.align 4
.LLSDA8737:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT8737-.LLSDATTD8737
.LLSDATTD8737:
	.byte	0x1
	.uleb128 .LLSDACSE8737-.LLSDACSB8737
.LLSDACSB8737:
	.uleb128 .LEHB7-.LFB8737
	.uleb128 .LEHE7-.LEHB7
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB8-.LFB8737
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L226-.LFB8737
	.uleb128 0x1
	.uleb128 .LEHB9-.LFB8737
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L227-.LFB8737
	.uleb128 0
	.uleb128 .LEHB10-.LFB8737
	.uleb128 .LEHE10-.LEHB10
	.uleb128 0
	.uleb128 0
.LLSDACSE8737:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT8737:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
	.size	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm, .-_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
	.section	.text.unlikely._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LCOLDE28:
	.section	.text._ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,"axG",@progbits,_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm,comdat
.LHOTE28:
	.section	.text.unlikely._ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,comdat
	.align 2
.LCOLDB29:
	.section	.text._ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,comdat
.LHOTB29:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_
	.type	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_, @function
_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_:
.LFB8745:
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
	movq	%rsi, %r12
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 64
	movq	72(%rdi), %rbp
	movq	(%rdi), %rcx
	movq	8(%rdi), %rdx
	movq	%rbp, %rax
	subq	%rcx, %rax
	movq	%rdx, %rsi
	sarq	$3, %rax
	subq	%rax, %rsi
	cmpq	$1, %rsi
	jbe	.L252
.L231:
	movl	$512, %edi
	call	_Znwm
	movq	%rax, 8(%rbp)
	movq	48(%rbx), %rax
	movl	(%r12), %edx
	testq	%rax, %rax
	je	.L239
	movl	%edx, (%rax)
.L239:
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
.L252:
	.cfi_restore_state
	movq	40(%rdi), %rsi
	movq	%rbp, %rax
	subq	%rsi, %rax
	sarq	$3, %rax
	leaq	2(%rax), %r14
	leaq	1(%rax), %r13
	leaq	(%r14,%r14), %rax
	cmpq	%rax, %rdx
	ja	.L253
	testq	%rdx, %rdx
	je	.L240
	leaq	2(%rdx,%rdx), %rbp
	movabsq	$2305843009213693951, %rax
	cmpq	%rax, %rbp
	ja	.L254
.L237:
	leaq	0(,%rbp,8), %rdi
	call	_Znwm
	movq	%rax, %r15
	movq	%rbp, %rax
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
	jne	.L255
.L238:
	movq	(%rbx), %rdi
	call	_ZdlPv
	movq	%r15, (%rbx)
	movq	%rbp, 8(%rbx)
.L251:
	salq	$3, %r13
.L235:
	movq	%r14, 40(%rbx)
	movq	(%r14), %rax
	leaq	-8(%r14,%r13), %rbp
	movq	%rbp, 72(%rbx)
	movq	%rax, 24(%rbx)
	addq	$512, %rax
	movq	%rax, 32(%rbx)
	movq	0(%rbp), %rax
	movq	%rax, 56(%rbx)
	addq	$512, %rax
	movq	%rax, 64(%rbx)
	jmp	.L231
	.p2align 4,,10
	.p2align 3
.L253:
	subq	%r14, %rdx
	shrq	%rdx
	leaq	(%rcx,%rdx,8), %r14
	cmpq	%r14, %rsi
	jbe	.L233
	leaq	8(%rbp), %rdx
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L251
	movq	%r14, %rdi
	salq	$3, %r13
	call	memmove
	jmp	.L235
	.p2align 4,,10
	.p2align 3
.L240:
	movl	$3, %ebp
	jmp	.L237
	.p2align 4,,10
	.p2align 3
.L255:
	movq	%r14, %rdi
	call	memmove
	jmp	.L238
	.p2align 4,,10
	.p2align 3
.L233:
	leaq	8(%rbp), %rdx
	salq	$3, %r13
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L235
	movq	%r13, %rdi
	subq	%rdx, %rdi
	addq	%r14, %rdi
	call	memmove
	jmp	.L235
.L254:
	call	_ZSt17__throw_bad_allocv
	.cfi_endproc
.LFE8745:
	.size	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_, .-_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,comdat
.LCOLDE29:
	.section	.text._ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,"axG",@progbits,_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_,comdat
.LHOTE29:
	.weak	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIIRKiEEEvDpOT_
	.set	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIIRKiEEEvDpOT_,_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,comdat
	.align 2
.LCOLDB30:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,comdat
.LHOTB30:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_:
.LFB8758:
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
	je	.L264
	leaq	(%rax,%rax), %rdx
	cmpq	%rdx, %rax
	jbe	.L276
.L265:
	movq	$-4, %r13
	jmp	.L257
	.p2align 4,,10
	.p2align 3
.L264:
	movl	$4, %r13d
.L257:
	movq	%r13, %rdi
	call	_Znwm
	movq	%rax, %rbp
.L263:
	movq	(%rbx), %r14
	movq	8(%rbx), %rdx
	movl	(%r12), %ecx
	movq	%rbp, %r12
	subq	%r14, %rdx
	movq	%rdx, %rax
	sarq	$2, %rax
	addq	%rdx, %r12
	je	.L259
	movl	%ecx, (%r12)
.L259:
	testq	%rax, %rax
	jne	.L277
	addq	$4, %r12
	testq	%r14, %r14
	je	.L262
.L261:
	movq	%r14, %rdi
	call	_ZdlPv
.L262:
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
.L277:
	.cfi_restore_state
	movq	%r14, %rsi
	movq	%rbp, %rdi
	addq	$4, %r12
	call	memmove
	jmp	.L261
.L276:
	movabsq	$4611686018427387903, %rcx
	cmpq	%rcx, %rdx
	ja	.L265
	xorl	%r13d, %r13d
	xorl	%ebp, %ebp
	testq	%rdx, %rdx
	je	.L263
	leaq	0(,%rax,8), %r13
	jmp	.L257
	.cfi_endproc
.LFE8758:
	.size	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,comdat
.LCOLDE30:
	.section	.text._ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_,comdat
.LHOTE30:
	.weak	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIIiEEEvDpOT_,_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,comdat
	.align 2
.LCOLDB31:
	.section	.text._ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,comdat
.LHOTB31:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	.type	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_, @function
_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_:
.LFB8622:
	.cfi_startproc
	movq	8(%rdi), %rax
	cmpq	16(%rdi), %rax
	je	.L279
	testq	%rax, %rax
	movl	(%rsi), %edx
	je	.L280
	movl	%edx, (%rax)
.L280:
	addq	$4, %rax
	movq	%rax, 8(%rdi)
	ret
	.p2align 4,,10
	.p2align 3
.L279:
	jmp	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
	.cfi_endproc
.LFE8622:
	.size	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_, .-_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	.section	.text.unlikely._ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,comdat
.LCOLDE31:
	.section	.text._ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,"axG",@progbits,_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_,comdat
.LHOTE31:
	.weak	_ZNSt6vectorIiSaIiEE12emplace_backIIiEEEvDpOT_
	.set	_ZNSt6vectorIiSaIiEE12emplace_backIIiEEEvDpOT_,_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDB32:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTB32:
	.p2align 4,,15
	.weak	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.type	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, @function
_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_:
.LFB8887:
	.cfi_startproc
	cmpq	%rdi, %rsi
	je	.L303
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
	je	.L286
	movq	%rsi, %r14
	movq	%rdi, %r13
	movl	$4, %r12d
	.p2align 4,,10
	.p2align 3
.L294:
	movl	0(%rbp), %ebx
	cmpl	0(%r13), %ebx
	jl	.L305
	movl	-4(%rbp), %edx
	leaq	-4(%rbp), %rax
	cmpl	%edx, %ebx
	jl	.L293
	jmp	.L306
	.p2align 4,,10
	.p2align 3
.L296:
	movq	%rcx, %rax
.L293:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %ebx
	jl	.L296
.L292:
	movl	%ebx, (%rax)
.L291:
	addq	$4, %rbp
	cmpq	%rbp, %r14
	jne	.L294
.L286:
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
.L303:
	rep ret
	.p2align 4,,10
	.p2align 3
.L305:
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
	je	.L290
	movq	%r12, %rdi
	movq	%r13, %rsi
	subq	%rdx, %rdi
	addq	%rbp, %rdi
	call	memmove
.L290:
	movl	%ebx, 0(%r13)
	jmp	.L291
.L306:
	movq	%rbp, %rax
	jmp	.L292
	.cfi_endproc
.LFE8887:
	.size	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_, .-_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	.section	.text.unlikely._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LCOLDE32:
	.section	.text._ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,"axG",@progbits,_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_,comdat
.LHOTE32:
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDB33:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTB33:
	.p2align 4,,15
	.weak	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.type	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, @function
_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_:
.LFB9070:
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
	jge	.L308
	movq	%rsi, %r10
	jmp	.L310
	.p2align 4,,10
	.p2align 3
.L318:
	movq	%rax, %r10
.L310:
	leaq	1(%r10), %r8
	leaq	(%r8,%r8), %rax
	leaq	(%rdi,%r8,8), %r8
	leaq	-1(%rax), %r11
	movl	(%r8), %r9d
	leaq	(%rdi,%r11,4), %rbp
	movl	0(%rbp), %ebx
	cmpl	%r9d, %ebx
	jle	.L309
	movq	%rbp, %r8
	movl	%ebx, %r9d
	movq	%r11, %rax
.L309:
	cmpq	%r12, %rax
	movl	%r9d, (%rdi,%r10,4)
	jl	.L318
	testb	$1, %dl
	jne	.L311
.L317:
	subq	$2, %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%r9, %rdx
	sarq	%rdx
	cmpq	%rax, %rdx
	je	.L322
.L311:
	cmpq	%rsi, %rax
	jle	.L312
	leaq	-1(%rax), %rdx
	movq	%rdx, %r9
	shrq	$63, %r9
	addq	%rdx, %r9
	sarq	%r9
	movl	(%rdi,%r9,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L312
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	movl	%r10d, (%rdi,%rax,4)
	jge	.L312
.L315:
	leaq	-1(%r9), %rax
	movq	%rax, %rdx
	shrq	$63, %rdx
	addq	%rax, %rdx
	movq	%r9, %rax
	sarq	%rdx
	movl	(%rdi,%rdx,4), %r10d
	cmpl	%r10d, %ecx
	jle	.L312
	movq	%rdx, %r9
	movl	%r10d, (%rdi,%rax,4)
	cmpq	%r9, %rsi
	leaq	(%rdi,%r9,4), %r8
	jl	.L315
.L312:
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
.L322:
	.cfi_restore_state
	leaq	1(%rax,%rax), %rax
	leaq	(%rdi,%rax,4), %rdx
	movl	(%rdx), %r9d
	movl	%r9d, (%r8)
	movq	%rdx, %r8
	jmp	.L311
.L308:
	testb	$1, %dl
	leaq	(%rdi,%rsi,4), %r8
	movq	%rsi, %rax
	je	.L317
	jmp	.L312
	.cfi_endproc
.LFE9070:
	.size	_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_, .-_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_
	.section	.text.unlikely._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LCOLDE33:
	.section	.text._ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,"axG",@progbits,_ZSt13__adjust_heapIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEEliNS0_5__ops15_Iter_less_iterEEvT_T0_SA_T1_T2_,comdat
.LHOTE33:
	.section	.text.unlikely
.LCOLDB34:
	.text
.LHOTB34:
	.p2align 4,,15
	.type	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123, @function
_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123:
.LFB9235:
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
	jle	.L323
	testq	%rdx, %rdx
	movq	%rdi, %r12
	movq	%rdx, %r13
	je	.L325
	leaq	8(%rdi), %rbx
	movq	%rsi, %rbp
.L326:
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
	jge	.L331
	cmpl	%ecx, %eax
	jl	.L337
	cmpl	%ecx, %edi
	jge	.L349
.L350:
	movl	(%r12), %edx
	movl	%ecx, (%r12)
	movl	%edx, -4(%rsi)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
.L333:
	movq	%rbx, %r8
	movq	%rsi, %rcx
	.p2align 4,,10
	.p2align 3
.L335:
	leaq	-4(%r8), %rbp
	cmpl	%edi, %r9d
	movq	%rbp, %r14
	jl	.L338
	cmpl	%edi, %edx
	leaq	-4(%rcx), %rax
	jle	.L345
	leaq	-8(%rcx), %rax
	.p2align 4,,10
	.p2align 3
.L340:
	movq	%rax, %rcx
	subq	$4, %rax
	movl	4(%rax), %edx
	cmpl	%edi, %edx
	jg	.L340
	cmpq	%rcx, %rbp
	jnb	.L351
.L341:
	movl	%edx, -4(%r8)
	movl	%r9d, (%rcx)
	movl	-4(%rcx), %edx
	movl	(%r12), %edi
.L338:
	movl	(%r8), %r9d
	addq	$4, %r8
	jmp	.L335
.L345:
	movq	%rax, %rcx
	cmpq	%rcx, %rbp
	jb	.L341
.L351:
	movq	%r13, %rdx
	movq	%rbp, %rdi
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123
	movq	%rbp, %rax
	subq	%r12, %rax
	cmpq	$67, %rax
	jle	.L323
	testq	%r13, %r13
	je	.L325
	movq	%rbp, %rsi
	jmp	.L326
.L331:
	cmpl	%ecx, %edi
	jl	.L349
	cmpl	%ecx, %eax
	jl	.L350
.L337:
	movl	(%r12), %ecx
	movl	%eax, (%r12)
	movl	%ecx, (%rdx)
	movl	4(%r12), %r9d
	movl	(%r12), %edi
	movl	-4(%rsi), %edx
	jmp	.L333
.L349:
	movl	(%r12), %r9d
	movl	%edi, (%r12)
	movl	%r9d, 4(%r12)
	movl	-4(%rsi), %edx
	jmp	.L333
.L325:
	sarq	$2, %rax
	leaq	-2(%rax), %rbp
	movq	%rax, %rbx
	sarq	%rbp
	jmp	.L328
.L352:
	subq	$1, %rbp
.L328:
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
	jne	.L352
	subq	$4, %r14
.L329:
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
	jg	.L329
.L323:
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
.LFE9235:
	.size	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123, .-_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123
	.section	.text.unlikely
.LCOLDE34:
	.text
.LHOTE34:
	.section	.rodata.str1.1
.LC35:
	.string	"food.inp"
.LC36:
	.string	"food.out"
.LC37:
	.string	" \306\304\300\317\300\314 \276\310 \277\255\267\310\276\356\277\344"
.LC38:
	.string	"cut vertex "
.LC39:
	.string	"biconnected componenet \274\366 : "
.LC40:
	.string	"\271\370 \302\260 "
.LC41:
	.string	"output file\300\314 \276\310 \277\255\267\310\276\356\277\344"
.LC42:
	.string	"\261\327\267\241\307\301\277\241 \276\306\271\253\260\315\265\265 \276\370\276\356\277\344"
	.section	.text.unlikely
.LCOLDB43:
	.section	.text.startup,"ax",@progbits
.LHOTB43:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB8204:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA8204
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movl	$.LC35+8, %edx
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movl	$.LC35, %esi
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$1512, %rsp
	.cfi_def_cfa_offset 1568
	movq	%fs:40, %rax
	movq	%rax, 1496(%rsp)
	xorl	%eax, %eax
	leaq	400(%rsp), %rdi
	leaq	416(%rsp), %rax
	movq	%rax, 400(%rsp)
.LEHB11:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84
.LEHE11:
	leaq	448(%rsp), %rax
	leaq	432(%rsp), %rdi
	movl	$.LC36+8, %edx
	movl	$.LC36, %esi
	movq	%rax, 432(%rsp)
.LEHB12:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.84
.LEHE12:
	leaq	976(%rsp), %rdi
.LEHB13:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1Ev
.LEHE13:
	leaq	464(%rsp), %rdi
.LEHB14:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1Ev
.LEHE14:
	leaq	400(%rsp), %rsi
	leaq	976(%rsp), %rdi
	movl	$8, %edx
	movq	$0, 96(%rsp)
	movq	$0, 104(%rsp)
	leaq	96(%rsp), %rbp
	movq	$0, 112(%rsp)
	movl	$0, 76(%rsp)
.LEHB15:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE4openERKNSt7__cxx1112basic_stringIcS1_SaIcEEESt13_Ios_Openmode
	leaq	1096(%rsp), %rdi
	leaq	96(%rsp), %rbp
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	jne	.L354
	movq	408(%rsp), %rdx
	movq	400(%rsp), %rsi
	movl	$_ZSt4cout, %edi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	$19, %edx
	movl	$.LC37, %esi
	movq	%rax, %rdi
	movq	%rax, %rbx
	leaq	96(%rsp), %rbp
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	%rbx, %rdi
	leaq	96(%rsp), %rbp
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
.L355:
	leaq	96(%rsp), %rdi
	call	_ZN5GraphD1Ev
	leaq	464(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	leaq	976(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	432(%rsp), %rdi
	leaq	448(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L531
	call	_ZdlPv
.L531:
	movq	400(%rsp), %rdi
	leaq	416(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L532
	call	_ZdlPv
.L532:
	xorl	%eax, %eax
	movq	1496(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L696
	addq	$1512, %rsp
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
.L354:
	.cfi_restore_state
	leaq	76(%rsp), %rsi
	leaq	976(%rsp), %rdi
	call	_ZNSirsERi
	xorl	%ebx, %ebx
	jmp	.L358
	.p2align 4,,10
	.p2align 3
.L697:
	leaq	96(%rsp), %rbp
	addl	$1, %ebx
	movl	%ebx, %esi
	movq	%rbp, %rdi
	call	_ZN5Graph10add_vertexEi
.L358:
	cmpl	76(%rsp), %ebx
	jl	.L697
.L560:
	movl	$1, %ebx
.L357:
	leaq	80(%rsp), %rsi
	leaq	976(%rsp), %rdi
	leaq	96(%rsp), %rbp
	call	_ZNSirsERi
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L359
	movl	80(%rsp), %ecx
	testl	%ecx, %ecx
	je	.L560
	testb	%bl, %bl
	jne	.L561
	movq	96(%rsp), %rax
	movq	104(%rsp), %r8
	cmpq	%r8, %rax
	je	.L562
	movq	(%rax), %rdi
	leaq	8(%rax), %rdx
	movl	24(%rdi), %r9d
	cmpl	%r9d, %ecx
	jne	.L364
	jmp	.L698
	.p2align 4,,10
	.p2align 3
.L365:
	movq	(%rdx), %rsi
	addq	$8, %rdx
	cmpl	24(%rsi), %ecx
	je	.L362
.L364:
	cmpq	%r8, %rdx
	jne	.L365
	xorl	%esi, %esi
.L362:
	addq	$8, %rax
	cmpl	%r9d, %r12d
	jne	.L366
	jmp	.L361
	.p2align 4,,10
	.p2align 3
.L367:
	movq	(%rax), %rdi
	addq	$8, %rax
	cmpl	24(%rdi), %r12d
	je	.L361
.L366:
	cmpq	%r8, %rax
	jne	.L367
.L677:
	xorl	%edi, %edi
.L361:
	leaq	96(%rsp), %rbp
	call	_ZN10VertexNode8add_edgeEPS_
	jmp	.L357
.L561:
	movl	%ecx, %r12d
	xorl	%ebx, %ebx
	jmp	.L357
.L359:
	leaq	976(%rsp), %rdi
	leaq	96(%rsp), %rbp
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE5closeEv
.LEHE15:
	movq	104(%rsp), %rax
	cmpq	%rax, 96(%rsp)
	je	.L699
	movslq	76(%rsp), %rax
	movabsq	$2287828610704211968, %rdx
	movq	$0, 128(%rsp)
	movq	$0, 136(%rsp)
	movq	$0, 144(%rsp)
	cmpq	%rdx, %rax
	ja	.L700
	leaq	0(,%rax,4), %rdi
.LEHB16:
	call	_Znam
	movq	%rax, %rbp
	movslq	76(%rsp), %rax
	movabsq	$2287828610704211968, %rdx
	cmpq	%rdx, %rax
	ja	.L701
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movslq	76(%rsp), %rdi
	movq	%rax, 16(%rsp)
	call	_Znam
	movl	76(%rsp), %edx
	movq	%rax, %rbx
	testl	%edx, %edx
	jle	.L376
	subl	$1, %edx
	leaq	1(%rax,%rdx), %rdx
.L377:
	movb	$0, (%rax)
	addq	$1, %rax
	cmpq	%rax, %rdx
	jne	.L377
.L376:
	leaq	240(%rsp), %rdi
	xorl	%esi, %esi
	movq	$0, 240(%rsp)
	movq	$0, 248(%rsp)
	movq	$0, 256(%rsp)
	movq	$0, 264(%rsp)
	movq	$0, 272(%rsp)
	movq	$0, 280(%rsp)
	movq	$0, 288(%rsp)
	movq	$0, 296(%rsp)
	movq	$0, 304(%rsp)
	movq	$0, 312(%rsp)
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm
.LEHE16:
	leaq	160(%rsp), %rdi
	xorl	%esi, %esi
	movq	$0, 160(%rsp)
	movq	$0, 168(%rsp)
	movq	$0, 176(%rsp)
	movq	$0, 184(%rsp)
	movq	$0, 192(%rsp)
	movq	$0, 200(%rsp)
	movq	$0, 208(%rsp)
	movq	$0, 216(%rsp)
	movq	$0, 224(%rsp)
	movq	$0, 232(%rsp)
.LEHB17:
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EE17_M_initialize_mapEm
.LEHE17:
	movq	240(%rsp), %rax
	testq	%rax, %rax
	je	.L378
	movq	256(%rsp), %r8
	movq	176(%rsp), %rdi
	movq	184(%rsp), %rsi
	movq	192(%rsp), %rcx
	movq	200(%rsp), %rdx
	movq	%r8, 176(%rsp)
	movq	264(%rsp), %r8
	movq	%rdi, 256(%rsp)
	movq	208(%rsp), %rdi
	movq	%rsi, 264(%rsp)
	movq	216(%rsp), %rsi
	movq	%r8, 184(%rsp)
	movq	272(%rsp), %r8
	movq	%rcx, 272(%rsp)
	movq	224(%rsp), %rcx
	movq	%r8, 192(%rsp)
	movq	280(%rsp), %r8
	movq	%rdx, 280(%rsp)
	movq	232(%rsp), %rdx
	movq	%r8, 200(%rsp)
	movq	288(%rsp), %r8
	movq	%rdi, 288(%rsp)
	movq	%r8, 208(%rsp)
	movq	296(%rsp), %r8
	movq	%rsi, 296(%rsp)
	movq	%r8, 216(%rsp)
	movq	304(%rsp), %r8
	movq	%rcx, 304(%rsp)
	movq	%r8, 224(%rsp)
	movq	312(%rsp), %r8
	movq	%rdx, 312(%rsp)
	movq	%r8, 232(%rsp)
	movq	160(%rsp), %rdx
	movq	%rax, 160(%rsp)
	movq	168(%rsp), %rax
	movq	%rdx, 240(%rsp)
	movq	248(%rsp), %rdx
	movq	%rax, 248(%rsp)
	movq	%rdx, 168(%rsp)
.L378:
	leaq	240(%rsp), %rdi
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	movslq	76(%rsp), %r12
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %r12
	ja	.L379
	leaq	(%r12,%r12,2), %rax
	leaq	8(,%rax,8), %rdi
.L379:
.LEHB18:
	call	_Znam
	movq	%r12, (%rax)
	movq	%rax, 48(%rsp)
	xorl	%edx, %edx
	addq	$8, %rax
	testq	%r12, %r12
	movq	%rax, 8(%rsp)
	je	.L383
.L631:
	addq	$1, %rdx
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	$0, 16(%rax)
	addq	$24, %rax
	cmpq	%rdx, %r12
	jne	.L631
.L383:
	movl	76(%rsp), %r9d
	movl	$1, 84(%rsp)
	testl	%r9d, %r9d
	jle	.L565
	movl	$1, %eax
	xorl	%r15d, %r15d
	movl	$1, %r12d
	jmp	.L482
	.p2align 4,,10
	.p2align 3
.L385:
	movl	84(%rsp), %eax
	addl	$1, %eax
	cmpl	%eax, 76(%rsp)
	movl	%eax, 84(%rsp)
	jl	.L381
.L482:
	cltq
	cmpb	$0, -1(%rbx,%rax)
	jne	.L385
	leaq	320(%rsp), %rdi
	xorl	%esi, %esi
	movq	$0, 320(%rsp)
	movq	$0, 328(%rsp)
	movq	$0, 336(%rsp)
	movq	$0, 344(%rsp)
	movq	$0, 352(%rsp)
	movq	$0, 360(%rsp)
	movq	$0, 368(%rsp)
	movq	$0, 376(%rsp)
	movq	$0, 384(%rsp)
	movq	$0, 392(%rsp)
	call	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
.LEHE18:
	leaq	240(%rsp), %rdi
	xorl	%esi, %esi
	movq	$0, 240(%rsp)
	movq	$0, 248(%rsp)
	movq	$0, 256(%rsp)
	movq	$0, 264(%rsp)
	movq	$0, 272(%rsp)
	movq	$0, 280(%rsp)
	movq	$0, 288(%rsp)
	movq	$0, 296(%rsp)
	movq	$0, 304(%rsp)
	movq	$0, 312(%rsp)
.LEHB19:
	call	_ZNSt11_Deque_baseIiSaIiEE17_M_initialize_mapEm
.LEHE19:
	movq	320(%rsp), %rax
	testq	%rax, %rax
	je	.L386
	movq	336(%rsp), %r8
	movq	256(%rsp), %rdi
	movq	264(%rsp), %rsi
	movq	272(%rsp), %rcx
	movq	280(%rsp), %rdx
	movq	%r8, 256(%rsp)
	movq	344(%rsp), %r8
	movq	%rdi, 336(%rsp)
	movq	288(%rsp), %rdi
	movq	%rsi, 344(%rsp)
	movq	296(%rsp), %rsi
	movq	%r8, 264(%rsp)
	movq	352(%rsp), %r8
	movq	%rcx, 352(%rsp)
	movq	304(%rsp), %rcx
	movq	%r8, 272(%rsp)
	movq	360(%rsp), %r8
	movq	%rdx, 360(%rsp)
	movq	312(%rsp), %rdx
	movq	%r8, 280(%rsp)
	movq	368(%rsp), %r8
	movq	%rdi, 368(%rsp)
	movq	%r8, 288(%rsp)
	movq	376(%rsp), %r8
	movq	%rsi, 376(%rsp)
	movq	%r8, 296(%rsp)
	movq	384(%rsp), %r8
	movq	%rcx, 384(%rsp)
	movq	%r8, 304(%rsp)
	movq	392(%rsp), %r8
	movq	%rdx, 392(%rsp)
	movq	%r8, 312(%rsp)
	movq	240(%rsp), %rdx
	movq	%rax, 240(%rsp)
	movq	248(%rsp), %rax
	movq	%rdx, 320(%rsp)
	movq	328(%rsp), %rdx
	movq	%rax, 328(%rsp)
	movq	%rdx, 248(%rsp)
.L386:
	leaq	320(%rsp), %rdi
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
	movq	304(%rsp), %rax
	movq	288(%rsp), %r9
	subq	$4, %rax
	cmpq	%rax, %r9
	je	.L387
	testq	%r9, %r9
	movl	84(%rsp), %eax
	je	.L388
	movl	%eax, (%r9)
	movl	84(%rsp), %eax
.L388:
	addq	$4, %r9
	movq	%r9, 288(%rsp)
.L389:
	leal	1(%r12), %esi
	cmpq	%r9, 256(%rsp)
	movslq	%eax, %rcx
	leaq	0(,%rcx,4), %rdx
	movb	$1, -1(%rbx,%rcx)
	movl	%esi, 28(%rsp)
	movq	16(%rsp), %rsi
	movl	%r12d, -4(%rbp,%rdx)
	movl	%eax, -4(%rsi,%rdx)
	je	.L476
	movl	$0, 40(%rsp)
.L475:
	xorl	%r12d, %r12d
	.p2align 4,,10
	.p2align 3
.L410:
	movq	296(%rsp), %r10
	movq	312(%rsp), %r13
	movq	%r9, %rax
	cmpq	%r9, %r10
	je	.L702
.L392:
	movl	-4(%rax), %r8d
	movq	104(%rsp), %rcx
	movq	96(%rsp), %rax
	cmpq	%rcx, %rax
	je	.L445
	movq	(%rax), %rdi
	leaq	8(%rax), %rdx
	movl	24(%rdi), %r11d
	cmpl	%r11d, %r8d
	jne	.L396
	jmp	.L703
	.p2align 4,,10
	.p2align 3
.L397:
	movq	(%rdx), %rsi
	addq	$8, %rdx
	cmpl	24(%rsi), %r8d
	je	.L394
.L396:
	cmpq	%rcx, %rdx
	jne	.L397
.L445:
	movq	8, %rax
	ud2
.L696:
	call	__stack_chk_fail
.L584:
	leaq	240(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
.L534:
	movq	128(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L538
	call	_ZdlPv
.L538:
	leaq	96(%rsp), %rbp
.L539:
	movq	%rbp, %rdi
	call	_ZN5GraphD1Ev
	leaq	464(%rsp), %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L540:
	leaq	976(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
.L541:
	movq	432(%rsp), %rdi
	leaq	448(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L543
	call	_ZdlPv
.L543:
	movq	400(%rsp), %rdi
	leaq	416(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L544
	call	_ZdlPv
.L544:
	movq	%rbx, %rdi
.LEHB20:
	call	_Unwind_Resume
.LEHE20:
	.p2align 4,,10
	.p2align 3
.L703:
	movq	%rdi, %rsi
	.p2align 4,,10
	.p2align 3
.L394:
	movq	8(%rsi), %rdx
	subq	(%rsi), %rdx
	sarq	$3, %rdx
	cmpl	%edx, %r12d
	jge	.L398
	cmpq	%r9, %r10
	je	.L704
.L399:
	movl	-4(%r9), %edx
	addq	$8, %rax
	cmpl	%r11d, %edx
	jne	.L401
	jmp	.L400
	.p2align 4,,10
	.p2align 3
.L402:
	movq	(%rax), %rdi
	addq	$8, %rax
	cmpl	24(%rdi), %edx
	je	.L400
.L401:
	cmpq	%rcx, %rax
	jne	.L402
	xorl	%edi, %edi
.L400:
	movl	%r12d, %esi
.LEHB21:
	call	_ZN10VertexNode7getEdgeEi
	movq	8(%rax), %rax
	movslq	24(%rax), %rax
	cmpb	$0, -1(%rbx,%rax)
	movl	%eax, 88(%rsp)
	je	.L705
	addl	$1, %r12d
	movq	288(%rsp), %r9
	jmp	.L410
	.p2align 4,,10
	.p2align 3
.L702:
	movq	-8(%r13), %rax
	addq	$512, %rax
	jmp	.L392
	.p2align 4,,10
	.p2align 3
.L704:
	movq	-8(%r13), %r9
	addq	$512, %r9
	jmp	.L399
.L398:
	cmpq	%r9, %r10
	je	.L548
	movl	-4(%r9), %r12d
	subq	$4, %r9
	movq	%r9, 288(%rsp)
.L552:
	cmpq	256(%rsp), %r9
	je	.L476
	cmpq	296(%rsp), %r9
	je	.L706
.L444:
	movl	-4(%r9), %eax
	movq	16(%rsp), %rsi
	xorl	%r13d, %r13d
	movl	%eax, 92(%rsp)
	movslq	%r12d, %rax
	leaq	-4(%rsi,%rax,4), %r14
	.p2align 4,,10
	.p2align 3
.L457:
	movq	96(%rsp), %rax
	movq	104(%rsp), %rcx
	cmpq	%rcx, %rax
	je	.L445
	movq	(%rax), %rdi
	addq	$8, %rax
	movq	%rax, %rdx
	cmpl	%r12d, 24(%rdi)
	jne	.L448
	jmp	.L707
	.p2align 4,,10
	.p2align 3
.L451:
	movq	(%rdx), %rsi
	addq	$8, %rdx
	cmpl	24(%rsi), %r12d
	je	.L708
.L448:
	cmpq	%rcx, %rdx
	jne	.L451
	jmp	.L445
	.p2align 4,,10
	.p2align 3
.L708:
	movq	8(%rsi), %rdx
	subq	(%rsi), %rdx
	sarq	$3, %rdx
	cmpl	%edx, %r13d
	jl	.L454
	jmp	.L450
	.p2align 4,,10
	.p2align 3
.L455:
	movq	(%rax), %rdi
	addq	$8, %rax
	cmpl	24(%rdi), %r12d
	je	.L453
.L454:
	cmpq	%rcx, %rax
	jne	.L455
	xorl	%edi, %edi
.L453:
	movl	%r13d, %esi
	call	_ZN10VertexNode7getEdgeEi
	movq	8(%rax), %rax
	movslq	24(%rax), %rax
	cmpl	%eax, 92(%rsp)
	je	.L456
	movl	-4(%rbp,%rax,4), %eax
	cmpl	%eax, (%r14)
	jle	.L456
	movl	%eax, (%r14)
.L456:
	addl	$1, %r13d
	jmp	.L457
.L705:
	movq	288(%rsp), %rax
	cmpq	%rax, 296(%rsp)
	je	.L709
.L404:
	movl	-4(%rax), %ecx
	movq	104(%rsp), %rdx
	movq	96(%rsp), %rax
	cmpq	%rdx, %rax
	je	.L568
	movq	(%rax), %rdi
	addq	$8, %rax
	cmpl	%ecx, 24(%rdi)
	jne	.L407
	jmp	.L405
	.p2align 4,,10
	.p2align 3
.L408:
	movq	(%rax), %rdi
	addq	$8, %rax
	cmpl	%ecx, 24(%rdi)
	je	.L405
.L407:
	cmpq	%rax, %rdx
	jne	.L408
.L568:
	xorl	%edi, %edi
.L405:
	movl	%r12d, %esi
	call	_ZN10VertexNode7getEdgeEi
	movq	%rax, 32(%rsp)
	movq	288(%rsp), %rax
	cmpq	296(%rsp), %rax
	je	.L710
.L551:
	movl	-4(%rax), %edx
	cmpl	84(%rsp), %edx
	jne	.L678
	addl	$1, 40(%rsp)
	movl	40(%rsp), %eax
	cmpl	$1, %eax
	je	.L678
	movq	136(%rsp), %rax
	cmpq	144(%rsp), %rax
	je	.L414
	testq	%rax, %rax
	je	.L415
	movl	%edx, (%rax)
.L415:
	addq	$4, %rax
	movq	%rax, 136(%rsp)
.L417:
	movslq	%r15d, %rax
	movq	8(%rsp), %rsi
	movq	208(%rsp), %rdi
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %r12
	jmp	.L416
	.p2align 4,,10
	.p2align 3
.L419:
	movq	-8(%rdi), %rax
	leaq	320(%rsp), %rsi
	movq	%r12, %rdi
	movq	8(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rax
	cmpq	216(%rsp), %rax
	je	.L711
.L420:
	movq	-8(%rax), %rax
	leaq	320(%rsp), %rsi
	movq	%r12, %rdi
	movq	(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rdi
	movq	216(%rsp), %rax
	cmpq	%rax, %rdi
	movq	%rdi, %rdx
	je	.L712
	movq	-8(%rdx), %rdx
	movq	(%rdx), %rdx
	movl	24(%rdx), %esi
	cmpl	%esi, 84(%rsp)
	je	.L713
.L422:
	cmpq	%rax, %rdi
	je	.L425
	subq	$8, %rdi
	movq	%rdi, 208(%rsp)
.L416:
	movq	176(%rsp), %rax
	cmpq	%rdi, %rax
	je	.L418
.L720:
	cmpq	%rdi, 216(%rsp)
	jne	.L419
	movq	232(%rsp), %rax
	movq	-8(%rax), %rdi
	addq	$512, %rdi
	jmp	.L419
.L712:
	movq	232(%rsp), %rdx
	movq	-8(%rdx), %rdx
	addq	$512, %rdx
	movq	-8(%rdx), %rdx
	movq	(%rdx), %rdx
	movl	24(%rdx), %esi
	cmpl	%esi, 84(%rsp)
	jne	.L422
.L713:
	cmpq	%rax, %rdi
	je	.L423
	leaq	-8(%rdi), %rax
	movq	224(%rsp), %rdx
	movq	%rax, 208(%rsp)
.L424:
	subq	$8, %rdx
	addl	$1, %r15d
	cmpq	%rdx, %rax
	jne	.L714
.L427:
	movq	232(%rsp), %r14
	movq	160(%rsp), %rcx
	movq	168(%rsp), %rax
	movq	%r14, %rdx
	subq	%rcx, %rdx
	movq	%rax, %rsi
	sarq	$3, %rdx
	subq	%rdx, %rsi
	cmpq	$1, %rsi
	jbe	.L715
.L430:
	movl	$512, %edi
	call	_Znwm
	movq	%rax, 8(%r14)
	movq	208(%rsp), %rax
	testq	%rax, %rax
	je	.L438
	movq	32(%rsp), %rsi
	movq	%rsi, (%rax)
.L438:
	movq	232(%rsp), %rax
	leaq	8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 216(%rsp)
	movq	%rax, 208(%rsp)
	movq	%rdx, 224(%rsp)
	jmp	.L429
.L711:
	movq	232(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L420
.L707:
	movq	8(%rdi), %rax
	subq	(%rdi), %rax
	sarq	$3, %rax
	cmpl	%eax, %r13d
	jl	.L453
.L450:
	movslq	92(%rsp), %rax
	movq	16(%rsp), %rsi
	movl	(%r14), %edx
	movq	%rax, %rcx
	salq	$2, %rax
	leaq	-4(%rsi,%rax), %rsi
	cmpl	%edx, (%rsi)
	jle	.L458
	movl	%edx, (%rsi)
	movl	(%r14), %edx
.L458:
	cmpl	%edx, -4(%rbp,%rax)
	jg	.L459
	cmpl	84(%rsp), %ecx
	je	.L459
	movq	136(%rsp), %rax
	cmpq	144(%rsp), %rax
	je	.L460
	testq	%rax, %rax
	je	.L461
	movl	%ecx, (%rax)
.L461:
	addq	$4, %rax
	movq	%rax, 136(%rsp)
.L463:
	movslq	%r15d, %rax
	movq	8(%rsp), %rsi
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %r13
	movq	208(%rsp), %rax
	jmp	.L462
.L658:
	movq	8(%rax), %rax
	cmpl	%r12d, 24(%rax)
	je	.L470
	leaq	-8(%rdi), %rax
	movq	%rax, 208(%rsp)
.L462:
	cmpq	%rax, 176(%rsp)
	je	.L464
	cmpq	%rax, 216(%rsp)
	je	.L716
.L465:
	movq	-8(%rax), %rax
	leaq	320(%rsp), %rsi
	movq	%r13, %rdi
	movq	8(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rax
	cmpq	216(%rsp), %rax
	je	.L717
.L466:
	movq	-8(%rax), %rax
	leaq	320(%rsp), %rsi
	movq	%r13, %rdi
	movq	(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rdi
	cmpq	216(%rsp), %rdi
	movq	232(%rsp), %rax
	je	.L718
	movq	-8(%rdi), %rax
	movq	(%rax), %rdx
	movl	24(%rdx), %esi
	cmpl	%esi, 92(%rsp)
	jne	.L658
.L470:
	subq	$8, %rdi
	movq	%rdi, 208(%rsp)
.L464:
	addl	$1, %r15d
.L459:
	movq	288(%rsp), %r9
	movq	256(%rsp), %rax
.L442:
	cmpq	%rax, %r9
	jne	.L475
.L476:
	movslq	%r15d, %rax
	movq	8(%rsp), %rsi
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %r12
	movq	208(%rsp), %rax
	jmp	.L391
.L478:
	movq	-8(%rax), %rax
	leaq	320(%rsp), %rsi
	movq	%r12, %rdi
	movq	8(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rax
	cmpq	216(%rsp), %rax
	je	.L719
.L479:
	movq	-8(%rax), %rax
	leaq	320(%rsp), %rsi
	movq	%r12, %rdi
	movq	(%rax), %rax
	movl	24(%rax), %eax
	movl	%eax, 320(%rsp)
	call	_ZNSt6vectorIiSaIiEE12emplace_backIJiEEEvDpOT_
	movq	208(%rsp), %rdi
	cmpq	216(%rsp), %rdi
	je	.L480
	leaq	-8(%rdi), %rax
	movq	%rax, 208(%rsp)
.L391:
	cmpq	%rax, 176(%rsp)
	je	.L477
.L722:
	cmpq	%rax, 216(%rsp)
	jne	.L478
	movq	232(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L478
.L718:
	movq	-8(%rax), %rax
	movq	504(%rax), %rax
	movq	(%rax), %rdx
	movl	24(%rdx), %esi
	cmpl	%esi, 92(%rsp)
	je	.L468
	movq	8(%rax), %rax
	cmpl	%r12d, 24(%rax)
	je	.L468
	call	_ZdlPv
	movq	232(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 216(%rsp)
	addq	$504, %rax
	movq	%rax, 208(%rsp)
	movq	%rdx, 224(%rsp)
	jmp	.L462
.L717:
	movq	232(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L466
.L716:
	movq	232(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L465
.L678:
	movq	224(%rsp), %rdx
	movq	208(%rsp), %rax
	subq	$8, %rdx
	cmpq	%rdx, %rax
	je	.L427
.L714:
	testq	%rax, %rax
	je	.L428
	movq	32(%rsp), %rsi
	movq	%rsi, (%rax)
	movq	208(%rsp), %rax
.L428:
	addq	$8, %rax
	movq	%rax, 208(%rsp)
.L429:
	movslq	88(%rsp), %rax
	movq	288(%rsp), %r9
	movl	28(%rsp), %edi
	leaq	0(,%rax,4), %rsi
	movq	%rax, %rcx
	movb	$1, -1(%rbx,%rax)
	movq	304(%rsp), %rax
	leal	1(%rdi), %r12d
	leaq	-4(%rsi), %rdx
	movl	%edi, -4(%rbp,%rsi)
	subq	$4, %rax
	cmpq	%rax, %r9
	je	.L439
	testq	%r9, %r9
	je	.L571
	movl	%ecx, (%r9)
	movslq	88(%rsp), %rax
	salq	$2, %rax
	leaq	-4(%rax), %rdx
	movl	-4(%rbp,%rax), %eax
.L440:
	addq	$4, %r9
	movq	%r9, 288(%rsp)
.L441:
	movq	16(%rsp), %rsi
	movl	%r12d, 28(%rsp)
	movl	%eax, (%rsi,%rdx)
	movq	256(%rsp), %rax
	jmp	.L442
.L425:
	call	_ZdlPv
	movq	232(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	-8(%rax), %rdi
	leaq	512(%rdi), %rax
	movq	%rdi, 216(%rsp)
	addq	$504, %rdi
	movq	%rdi, 208(%rsp)
	movq	%rax, 224(%rsp)
	movq	176(%rsp), %rax
	cmpq	%rdi, %rax
	jne	.L720
.L418:
	movq	224(%rsp), %rdx
	jmp	.L424
.L710:
	movq	312(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L551
.L709:
	movq	312(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L404
.L548:
	movq	-8(%r13), %rax
	movq	%r10, %rdi
	movl	508(%rax), %r12d
	call	_ZdlPv
	movq	312(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 312(%rsp)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 296(%rsp)
	addq	$508, %rax
	movq	%rax, 288(%rsp)
	movq	%rax, %r9
	movq	%rdx, 304(%rsp)
	jmp	.L552
.L706:
	movq	312(%rsp), %rax
	movq	-8(%rax), %r9
	addq	$512, %r9
	jmp	.L444
.L571:
	movl	28(%rsp), %eax
	jmp	.L440
.L439:
	leaq	88(%rsp), %rsi
	leaq	240(%rsp), %rdi
	call	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_
	movslq	88(%rsp), %rax
	movq	288(%rsp), %r9
	salq	$2, %rax
	leaq	-4(%rax), %rdx
	movl	-4(%rbp,%rax), %eax
	jmp	.L441
.L715:
	movq	200(%rsp), %rsi
	movq	%r14, %r13
	subq	%rsi, %r13
	sarq	$3, %r13
	leaq	1(%r13), %r12
	addq	$2, %r13
	leaq	(%r13,%r13), %rdx
	cmpq	%rdx, %rax
	jbe	.L431
	subq	%r13, %rax
	shrq	%rax
	leaq	(%rcx,%rax,8), %r13
	cmpq	%r13, %rsi
	jbe	.L432
	leaq	8(%r14), %rdx
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	jne	.L721
.L679:
	salq	$3, %r12
.L434:
	movq	%r13, 200(%rsp)
	movq	0(%r13), %rax
	leaq	-8(%r13,%r12), %r14
	movq	%r14, 232(%rsp)
	movq	%rax, 184(%rsp)
	addq	$512, %rax
	movq	%rax, 192(%rsp)
	movq	(%r14), %rax
	movq	%rax, 216(%rsp)
	addq	$512, %rax
	movq	%rax, 224(%rsp)
	jmp	.L430
.L719:
	movq	232(%rsp), %rax
	movq	-8(%rax), %rax
	addq	$512, %rax
	jmp	.L479
.L480:
	call	_ZdlPv
	movq	232(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 216(%rsp)
	addq	$504, %rax
	cmpq	%rax, 176(%rsp)
	movq	%rax, 208(%rsp)
	movq	%rdx, 224(%rsp)
	jne	.L722
.L477:
	leaq	240(%rsp), %rdi
	addl	$1, %r15d
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
	movl	28(%rsp), %r12d
	jmp	.L385
.L414:
	leaq	84(%rsp), %rsi
	leaq	128(%rsp), %rdi
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
.LEHE21:
	jmp	.L417
.L587:
	leaq	240(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
.L536:
	leaq	160(%rsp), %rdi
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	jmp	.L534
.L423:
	call	_ZdlPv
	movq	232(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 216(%rsp)
	addq	$504, %rax
	movq	%rax, 208(%rsp)
	movq	%rdx, 224(%rsp)
	jmp	.L424
.L701:
.LEHB22:
	call	__cxa_throw_bad_array_new_length
.LEHE22:
.L583:
	movq	%rax, %rbx
	jmp	.L534
.L585:
	movq	%rax, %rbx
	jmp	.L536
.L565:
	xorl	%r15d, %r15d
.L381:
	movq	136(%rsp), %r12
	movq	128(%rsp), %r14
	cmpq	%r14, %r12
	je	.L572
	movq	%r12, %r13
	movl	$63, %edx
	movq	%r12, %rsi
	subq	%r14, %r13
	movq	%r14, %rdi
	movq	%r13, %rax
	sarq	$2, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123
	cmpq	$67, %r13
	jle	.L484
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	leaq	64(%r14), %r13
	movq	%r14, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1584
	movq	%r13, %rsi
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	cmpq	%r13, %r12
	movq	%r13, %rax
	popq	%rdi
	.cfi_def_cfa_offset 1576
	popq	%r8
	.cfi_def_cfa_offset 1568
	je	.L680
.L620:
	movl	(%rax), %esi
	movl	-4(%rax), %ecx
	movq	%rax, %rdx
	leaq	-4(%rax), %rdi
	cmpl	%ecx, %esi
	jge	.L486
.L573:
	movq	%rdi, %rdx
	movl	%ecx, 4(%rdi)
	leaq	-4(%rdi), %rdi
	movl	-4(%rdx), %ecx
	cmpl	%ecx, %esi
	jl	.L573
.L486:
	addq	$4, %rax
	movl	%esi, (%rdx)
	cmpq	%rax, %r12
	jne	.L620
.L680:
	movq	136(%rsp), %r12
	movq	128(%rsp), %rdi
.L483:
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	movq	%r12, %rsi
	pushq	$0
	.cfi_def_cfa_offset 1584
	call	_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_
	leaq	144(%rsp), %rdi
	movq	%r12, %rdx
	movq	%rax, %rsi
	call	_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_
	popq	%rax
	.cfi_def_cfa_offset 1576
	popq	%rdx
	.cfi_def_cfa_offset 1568
	movl	$.LC38, %esi
	movl	$11, %edx
	movl	$_ZSt4cout, %edi
.LEHB23:
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	$_ZSt4cout, %edi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	movq	128(%rsp), %r12
	cmpq	%r12, 136(%rsp)
	je	.L492
.L619:
	movl	(%r12), %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC9, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	addq	$4, %r12
	cmpq	%r12, 136(%rsp)
	jne	.L619
.L492:
	movl	$_ZSt4cout, %edi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	movl	$28, %edx
	movl	$.LC39, %esi
	movl	$_ZSt4cout, %edi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	%r15d, %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movq	%rax, %rdi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	movl	76(%rsp), %eax
	testl	%eax, %eax
	jle	.L574
	movq	8(%rsp), %r13
	xorl	%r15d, %r15d
	movq	$-1, %r14
	movl	$0, 28(%rsp)
.L517:
	movq	8(%r13), %r12
	movq	0(%r13), %rcx
	cmpq	%rcx, %r12
	je	.L494
	movq	%r12, %r8
	movl	$63, %edx
	movq	%rcx, %rdi
	subq	%rcx, %r8
	movq	%r12, %rsi
	movq	%rcx, 32(%rsp)
	movq	%r8, %rax
	movq	%r8, 40(%rsp)
	sarq	$2, %rax
	bsrq	%rax, %rax
	xorq	$63, %rax
	cltq
	subq	%rax, %rdx
	addq	%rdx, %rdx
	call	_ZSt16__introsort_loopIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEElNS0_5__ops15_Iter_less_iterEEvT_S9_T0_T1_.isra.123
	movq	40(%rsp), %r8
	movq	32(%rsp), %rcx
	cmpq	$67, %r8
	jle	.L495
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	leaq	64(%rcx), %rax
	movq	%rcx, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1584
	movq	%rax, %rsi
	movq	%rax, 48(%rsp)
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	popq	%r11
	.cfi_def_cfa_offset 1576
	popq	%rax
	.cfi_def_cfa_offset 1568
	movq	32(%rsp), %rax
	cmpq	%rax, %r12
	movq	%rax, %rdi
	je	.L497
.L618:
	movl	(%rdi), %esi
	movl	-4(%rdi), %edx
	leaq	-4(%rdi), %rax
	cmpl	%esi, %edx
	jg	.L499
	jmp	.L723
	.p2align 4,,10
	.p2align 3
.L576:
	movq	%rcx, %rax
.L499:
	movl	%edx, 4(%rax)
	movl	-4(%rax), %edx
	leaq	-4(%rax), %rcx
	cmpl	%edx, %esi
	jl	.L576
	addq	$4, %rdi
	movl	%esi, (%rax)
	cmpq	%rdi, %r12
	jne	.L618
.L497:
	movq	8(%r13), %r12
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	movq	0(%r13), %rdi
	pushq	$0
	.cfi_def_cfa_offset 1584
	movq	%r12, %rsi
	call	_ZSt8__uniqueIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops19_Iter_equal_to_iterEET_S9_S9_T0_
	movq	%r12, %rdx
	movq	%rax, %rsi
	movq	%r13, %rdi
	call	_ZNSt6vectorIiSaIiEE8_M_eraseEN9__gnu_cxx17__normal_iteratorIPiS1_EES5_
	movq	8(%r13), %rdx
	movq	0(%r13), %rax
	movslq	44(%rsp), %rcx
	popq	%rdi
	.cfi_def_cfa_offset 1576
	movq	%rdx, %rsi
	subq	%rax, %rsi
	sarq	$2, %rsi
	cmpq	%rsi, %rcx
	popq	%r8
	.cfi_def_cfa_offset 1568
	jb	.L506
	jne	.L503
	cmpq	%rax, %rdx
	jne	.L724
.L503:
	movl	%r15d, %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$6, %edx
	movl	$.LC40, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	0(%r13), %r12
	cmpq	8(%r13), %r12
	je	.L514
.L617:
	movl	(%r12), %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC9, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	addq	$4, %r12
	cmpq	%r12, 8(%r13)
	jne	.L617
.L514:
	movq	_ZSt4cout(%rip), %rax
	movq	-24(%rax), %rax
	movq	_ZSt4cout+240(%rax), %r12
	testq	%r12, %r12
	je	.L725
	cmpb	$0, 56(%r12)
	je	.L515
	movsbl	67(%r12), %esi
.L516:
	movl	$_ZSt4cout, %edi
	call	_ZNSo3putEc
	movq	%rax, %rdi
	call	_ZNSo5flushEv
.LEHE23:
.L494:
	addl	$1, %r15d
	addq	$24, %r13
	cmpl	%r15d, 76(%rsp)
	jg	.L517
	leaq	(%r14,%r14,2), %r12
	salq	$3, %r12
	jmp	.L493
.L700:
.LEHB24:
	call	__cxa_throw_bad_array_new_length
.LEHE24:
.L699:
	movl	$24, %edx
	movl	$.LC42, %esi
	movl	$_ZSt4cout, %edi
	leaq	96(%rsp), %rbp
.LEHB25:
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	$_ZSt4cout, %edi
	leaq	96(%rsp), %rbp
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
.LEHE25:
	jmp	.L355
.L698:
	movq	%rdi, %rsi
	jmp	.L362
.L562:
	xorl	%esi, %esi
	jmp	.L677
.L460:
	leaq	92(%rsp), %rsi
	leaq	128(%rsp), %rdi
.LEHB26:
	call	_ZNSt6vectorIiSaIiEE19_M_emplace_back_auxIJiEEEvDpOT_
	jmp	.L463
.L468:
	call	_ZdlPv
	movq	232(%rsp), %rax
	leaq	-8(%rax), %rdx
	movq	%rdx, 232(%rsp)
	movq	-8(%rax), %rax
	leaq	512(%rax), %rdx
	movq	%rax, 216(%rsp)
	addq	$504, %rax
	movq	%rax, 208(%rsp)
	movq	%rdx, 224(%rsp)
	jmp	.L464
.L586:
	leaq	320(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt11_Deque_baseIiSaIiEED2Ev
	jmp	.L536
.L387:
	leaq	84(%rsp), %rsi
	leaq	240(%rsp), %rdi
	call	_ZNSt5dequeIiSaIiEE16_M_push_back_auxIJRKiEEEvDpOT_
	movq	288(%rsp), %r9
	movl	84(%rsp), %eax
	jmp	.L389
.L721:
	movq	%r13, %rdi
	salq	$3, %r12
	call	memmove
	jmp	.L434
.L432:
	leaq	8(%r14), %rdx
	salq	$3, %r12
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L434
	movq	%r12, %rdi
	subq	%rdx, %rdi
	addq	%r13, %rdi
	call	memmove
	jmp	.L434
.L431:
	testq	%rax, %rax
	je	.L570
	leaq	2(%rax,%rax), %r14
	movabsq	$2305843009213693951, %rax
	cmpq	%rax, %r14
	ja	.L726
.L436:
	leaq	0(,%r14,8), %rdi
	call	_Znwm
	movq	%rax, %rsi
	movq	%rax, 56(%rsp)
	movq	%r14, %rax
	subq	%r13, %rax
	shrq	%rax
	leaq	(%rsi,%rax,8), %r13
	movq	232(%rsp), %rax
	movq	200(%rsp), %rsi
	leaq	8(%rax), %rdx
	subq	%rsi, %rdx
	movq	%rdx, %rax
	sarq	$3, %rax
	testq	%rax, %rax
	je	.L437
	movq	%r13, %rdi
	call	memmove
.L437:
	movq	160(%rsp), %rdi
	call	_ZdlPv
	movq	56(%rsp), %rax
	movq	%r14, 168(%rsp)
	movq	%rax, 160(%rsp)
	jmp	.L679
.L726:
	call	_ZSt17__throw_bad_allocv
.LEHE26:
.L570:
	movl	$3, %r14d
	jmp	.L436
.L582:
	movq	%rax, %rbx
	jmp	.L539
.L581:
	movq	%rax, %rbx
	jmp	.L540
.L580:
	movq	%rax, %rbx
	jmp	.L541
.L579:
	movq	%rax, %rbx
	jmp	.L543
.L484:
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	movq	%r12, %rsi
	movq	%r14, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1584
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	movq	152(%rsp), %r12
	movq	144(%rsp), %rdi
	popq	%rcx
	.cfi_def_cfa_offset 1576
	popq	%rsi
	.cfi_def_cfa_offset 1568
	jmp	.L483
.L572:
	movq	%r12, %rdi
	jmp	.L483
.L505:
	cmpq	%rcx, %rdi
	je	.L503
.L506:
	movl	%esi, 28(%rsp)
	movslq	%r15d, %r14
	jmp	.L503
.L723:
	movq	%rdi, %rax
	addq	$4, %rdi
	cmpq	%rdi, %r12
	movl	%esi, (%rax)
	jne	.L618
	jmp	.L497
	.p2align 4,,10
	.p2align 3
.L495:
	subq	$8, %rsp
	.cfi_def_cfa_offset 1576
	movq	%r12, %rsi
	movq	%rcx, %rdi
	pushq	$0
	.cfi_def_cfa_offset 1584
	call	_ZSt16__insertion_sortIN9__gnu_cxx17__normal_iteratorIPiSt6vectorIiSaIiEEEENS0_5__ops15_Iter_less_iterEEvT_S9_T0_
	popq	%r9
	.cfi_def_cfa_offset 1576
	popq	%r10
	.cfi_def_cfa_offset 1568
	jmp	.L497
.L515:
	movq	%r12, %rdi
.LEHB27:
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	(%r12), %rax
	movl	$10, %esi
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L516
	movq	%r12, %rdi
	call	*%rax
	movsbl	%al, %esi
	jmp	.L516
.L574:
	movq	$-24, %r12
.L493:
	addq	8(%rsp), %r12
	movq	(%r12), %r13
	cmpq	8(%r12), %r13
	je	.L521
.L616:
	movl	0(%r13), %esi
	movl	$_ZSt4cout, %edi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC9, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	addq	$4, %r13
	cmpq	%r13, 8(%r12)
	jne	.L616
.L521:
	movl	$_ZSt4cout, %edi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	leaq	432(%rsp), %rsi
	leaq	464(%rsp), %rdi
	movl	$48, %edx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE4openERKNSt7__cxx1112basic_stringIcS1_SaIcEEESt13_Ios_Openmode
	leaq	576(%rsp), %rdi
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	je	.L727
	movq	(%r12), %r13
	cmpq	%r13, 8(%r12)
	je	.L523
.L524:
	movl	0(%r13), %esi
	leaq	464(%rsp), %rdi
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC9, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	addq	$4, %r13
	cmpq	%r13, 8(%r12)
	jne	.L524
	jmp	.L523
.L724:
	movq	8(%rsp), %rdi
	movslq	%r14d, %rcx
	leaq	(%rcx,%rcx,2), %rcx
	leaq	(%rdi,%rcx,8), %rcx
	movq	8(%rcx), %rdi
	movq	(%rcx), %rcx
	movq	%rdi, %r8
	subq	%rcx, %r8
	movq	%r8, %r9
	sarq	$2, %r9
	cmpq	%r9, %rsi
	jle	.L509
	leaq	(%rax,%r8), %rdx
	cmpq	%rdx, %rax
	jne	.L509
	jmp	.L505
	.p2align 4,,10
	.p2align 3
.L666:
	jg	.L503
	addq	$4, %rax
	addq	$4, %rcx
	cmpq	%rax, %rdx
	je	.L505
.L509:
	movl	(%rcx), %r11d
	cmpl	%r11d, (%rax)
	jge	.L666
	movl	%esi, 28(%rsp)
	movslq	%r15d, %r14
	jmp	.L503
.L725:
	call	_ZSt16__throw_bad_castv
.L727:
	movl	$25, %edx
	movl	$.LC41, %esi
	movl	$_ZSt4cout, %edi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movl	$_ZSt4cout, %edi
	call	_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
.LEHE27:
.L523:
	cmpq	$0, 8(%rsp)
	je	.L526
	movq	48(%rsp), %rax
	movq	8(%rsp), %rsi
	movq	(%rax), %rax
	leaq	(%rax,%rax,2), %rax
	leaq	(%rsi,%rax,8), %r12
	cmpq	%r12, %rsi
	je	.L528
.L632:
	subq	$24, %r12
	movq	(%r12), %rdi
	testq	%rdi, %rdi
	je	.L527
	call	_ZdlPv
.L527:
	cmpq	%r12, 8(%rsp)
	jne	.L632
.L528:
	movq	48(%rsp), %rdi
	call	_ZdaPv
.L526:
	movq	%rbp, %rdi
	call	_ZdaPv
	movq	16(%rsp), %rdi
	call	_ZdaPv
	movq	%rbx, %rdi
	call	_ZdaPv
	leaq	160(%rsp), %rdi
	call	_ZNSt11_Deque_baseIP8EdgeNodeSaIS1_EED2Ev
	movq	128(%rsp), %rdi
	testq	%rdi, %rdi
	je	.L355
	call	_ZdlPv
	jmp	.L355
	.cfi_endproc
.LFE8204:
	.section	.gcc_except_table
.LLSDA8204:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE8204-.LLSDACSB8204
.LLSDACSB8204:
	.uleb128 .LEHB11-.LFB8204
	.uleb128 .LEHE11-.LEHB11
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB12-.LFB8204
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L579-.LFB8204
	.uleb128 0
	.uleb128 .LEHB13-.LFB8204
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L580-.LFB8204
	.uleb128 0
	.uleb128 .LEHB14-.LFB8204
	.uleb128 .LEHE14-.LEHB14
	.uleb128 .L581-.LFB8204
	.uleb128 0
	.uleb128 .LEHB15-.LFB8204
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L582-.LFB8204
	.uleb128 0
	.uleb128 .LEHB16-.LFB8204
	.uleb128 .LEHE16-.LEHB16
	.uleb128 .L583-.LFB8204
	.uleb128 0
	.uleb128 .LEHB17-.LFB8204
	.uleb128 .LEHE17-.LEHB17
	.uleb128 .L584-.LFB8204
	.uleb128 0
	.uleb128 .LEHB18-.LFB8204
	.uleb128 .LEHE18-.LEHB18
	.uleb128 .L585-.LFB8204
	.uleb128 0
	.uleb128 .LEHB19-.LFB8204
	.uleb128 .LEHE19-.LEHB19
	.uleb128 .L586-.LFB8204
	.uleb128 0
	.uleb128 .LEHB20-.LFB8204
	.uleb128 .LEHE20-.LEHB20
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB21-.LFB8204
	.uleb128 .LEHE21-.LEHB21
	.uleb128 .L587-.LFB8204
	.uleb128 0
	.uleb128 .LEHB22-.LFB8204
	.uleb128 .LEHE22-.LEHB22
	.uleb128 .L583-.LFB8204
	.uleb128 0
	.uleb128 .LEHB23-.LFB8204
	.uleb128 .LEHE23-.LEHB23
	.uleb128 .L585-.LFB8204
	.uleb128 0
	.uleb128 .LEHB24-.LFB8204
	.uleb128 .LEHE24-.LEHB24
	.uleb128 .L583-.LFB8204
	.uleb128 0
	.uleb128 .LEHB25-.LFB8204
	.uleb128 .LEHE25-.LEHB25
	.uleb128 .L582-.LFB8204
	.uleb128 0
	.uleb128 .LEHB26-.LFB8204
	.uleb128 .LEHE26-.LEHB26
	.uleb128 .L587-.LFB8204
	.uleb128 0
	.uleb128 .LEHB27-.LFB8204
	.uleb128 .LEHE27-.LEHB27
	.uleb128 .L585-.LFB8204
	.uleb128 0
.LLSDACSE8204:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE43:
	.section	.text.startup
.LHOTE43:
	.section	.text.unlikely
.LCOLDB44:
	.section	.text.startup
.LHOTB44:
	.p2align 4,,15
	.type	_GLOBAL__sub_I__ZN10VertexNodeD2Ev, @function
_GLOBAL__sub_I__ZN10VertexNodeD2Ev:
.LFB9111:
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
.LFE9111:
	.size	_GLOBAL__sub_I__ZN10VertexNodeD2Ev, .-_GLOBAL__sub_I__ZN10VertexNodeD2Ev
	.section	.text.unlikely
.LCOLDE44:
	.section	.text.startup
.LHOTE44:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__ZN10VertexNodeD2Ev
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
'''
fgeeks = ''' .file	"geeks.cpp"
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
'''
fs1_4 = '''
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
'''
fs1_3 = '''
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
'''
fs2 = ''' .file	"f2.cpp"
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
'''
fs1_2 = '''
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
'''
fs1_1 = ''' .file	"1-1.cpp"
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
.LFB2287:
	.cfi_startproc
	movl	%esi, (%rdi)
	movl	%edx, 4(%rdi)
	ret
	.cfi_endproc
.LFE2287:
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
	.globl	_ZN5GraphC2Ev
	.type	_ZN5GraphC2Ev, @function
_ZN5GraphC2Ev:
.LFB2293:
	.cfi_startproc
	leaq	24(%rdi), %rax
	movl	$0, 24(%rdi)
	movq	$0, 32(%rdi)
	movq	$0, 56(%rdi)
	movq	%rax, 40(%rdi)
	movq	%rax, 48(%rdi)
	ret
	.cfi_endproc
.LFE2293:
	.size	_ZN5GraphC2Ev, .-_ZN5GraphC2Ev
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.globl	_ZN5GraphC1Ev
	.set	_ZN5GraphC1Ev,_ZN5GraphC2Ev
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph10setVerticeEi
	.type	_ZN5Graph10setVerticeEi, @function
_ZN5Graph10setVerticeEi:
.LFB2301:
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
	ja	.L5
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L5:
	call	_Znam
	xorl	%ecx, %ecx
	movq	%rbx, (%rax)
	addq	$8, %rax
	testq	%rbx, %rbx
	movq	%rax, %rdx
	je	.L7
	.p2align 4,,10
	.p2align 3
.L10:
	addq	$1, %rcx
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rbx, %rcx
	jne	.L10
.L7:
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE2301:
	.size	_ZN5Graph10setVerticeEi, .-_ZN5Graph10setVerticeEi
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
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
.LFB2302:
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
.LFE2302:
	.size	_ZN5Graph7addEdgeEii, .-_ZN5Graph7addEdgeEii
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC5:
	.string	"./food.out"
.LC6:
	.string	" "
	.section	.text.unlikely
	.align 2
.LCOLDB7:
	.text
.LHOTB7:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph24getMaxBiconnectComponentEv
	.type	_ZN5Graph24getMaxBiconnectComponentEv, @function
_ZN5Graph24getMaxBiconnectComponentEv:
.LFB2308:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2308
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
	subq	$536, %rsp
	.cfi_def_cfa_offset 576
	leaq	248(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 520(%rsp)
	xorl	%eax, %eax
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+8(%rip), %r12
	movb	$0, 472(%rsp)
	xorl	%esi, %esi
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+16(%rip), %r13
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 248(%rsp)
	movq	$0, 464(%rsp)
	movb	$0, 473(%rsp)
	movq	-24(%r12), %rax
	movq	$0, 480(%rsp)
	movq	$0, 488(%rsp)
	movq	$0, 496(%rsp)
	movq	$0, 504(%rsp)
	movq	%r12, (%rsp)
	leaq	(%rsp,%rax), %rdi
	movq	%r13, (%rdi)
.LEHB0:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE0:
	leaq	8(%rsp), %rdi
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, (%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 248(%rsp)
.LEHB1:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE1:
	leaq	8(%rsp), %rsi
	leaq	248(%rsp), %rdi
.LEHB2:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	8(%rsp), %rdi
	movl	$48, %edx
	movl	$.LC5, %esi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	movq	(%rsp), %rax
	movq	-24(%rax), %rax
	leaq	(%rsp,%rax), %rdi
	je	.L41
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE2:
.L19:
	movq	40(%rbp), %rbx
	addq	$24, %rbp
	cmpq	%rbp, %rbx
	je	.L26
	.p2align 4,,10
	.p2align 3
.L35:
	movl	32(%rbx), %esi
	movq	%rsp, %rdi
.LEHB3:
	call	_ZNSolsEi
	movl	$1, %edx
	movl	$.LC6, %esi
	movq	%rax, %rdi
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rbp, %rax
	movq	%rax, %rbx
	jne	.L35
.L26:
	leaq	8(%rsp), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE3:
	testq	%rax, %rax
	je	.L42
.L28:
	leaq	8(%rsp), %rdi
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, (%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 248(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 8(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	112(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	64(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 8(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r12), %rax
	leaq	248(%rsp), %rdi
	movq	%r13, (%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 248(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	520(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L43
	addq	$536, %rsp
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
.L41:
	.cfi_restore_state
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB4:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE4:
	jmp	.L19
.L42:
	movq	(%rsp), %rax
	movq	-24(%rax), %rax
	leaq	(%rsp,%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB5:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE5:
	jmp	.L28
.L31:
	movq	%rax, %rbx
	movq	%rsp, %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB6:
	call	_Unwind_Resume
.L34:
	leaq	8(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rax
.L21:
	movq	-24(%r12), %rdx
	movq	%rax, %rbx
	movq	%r13, (%rsp,%rdx)
.L22:
	leaq	248(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 248(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	%rbx, %rdi
	call	_Unwind_Resume
.LEHE6:
.L33:
	jmp	.L21
.L32:
	movq	%rax, %rbx
	jmp	.L22
.L43:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2308:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA2308:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2308-.LLSDACSB2308
.LLSDACSB2308:
	.uleb128 .LEHB0-.LFB2308
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L32-.LFB2308
	.uleb128 0
	.uleb128 .LEHB1-.LFB2308
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L33-.LFB2308
	.uleb128 0
	.uleb128 .LEHB2-.LFB2308
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L34-.LFB2308
	.uleb128 0
	.uleb128 .LEHB3-.LFB2308
	.uleb128 .LEHE3-.LEHB3
	.uleb128 .L31-.LFB2308
	.uleb128 0
	.uleb128 .LEHB4-.LFB2308
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L34-.LFB2308
	.uleb128 0
	.uleb128 .LEHB5-.LFB2308
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L31-.LFB2308
	.uleb128 0
	.uleb128 .LEHB6-.LFB2308
	.uleb128 .LEHE6-.LEHB6
	.uleb128 0
	.uleb128 0
.LLSDACSE2308:
	.text
	.size	_ZN5Graph24getMaxBiconnectComponentEv, .-_ZN5Graph24getMaxBiconnectComponentEv
	.section	.text.unlikely
.LCOLDE7:
	.text
.LHOTE7:
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDB8:
	.section	.text._ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTB8:
	.p2align 4,,15
	.weak	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.type	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, @function
_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_:
.LFB2314:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movl	%r8d, %r15d
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdi, %r14
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdx, %rbx
	movq	%rsi, %r12
	movq	%rcx, %r13
	subq	$24, %rsp
	.cfi_def_cfa_offset 80
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	__errno_location
	movl	%r15d, %edx
	movq	%rax, %rbp
	movl	$0, (%rax)
	movq	%rsp, %rsi
	movq	%rbx, %rdi
	call	*%r14
	movq	(%rsp), %rdx
	cmpq	%rdx, %rbx
	je	.L54
	cmpl	$34, 0(%rbp)
	je	.L46
	movl	$2147483648, %esi
	movl	$4294967295, %ecx
	addq	%rax, %rsi
	cmpq	%rcx, %rsi
	ja	.L46
	testq	%r13, %r13
	je	.L48
	subq	%rbx, %rdx
	movq	%rdx, 0(%r13)
.L48:
	movq	8(%rsp), %rdi
	xorq	%fs:40, %rdi
	jne	.L55
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
.L46:
	.cfi_restore_state
	movq	%r12, %rdi
	call	_ZSt20__throw_out_of_rangePKc
.L54:
	movq	%r12, %rdi
	call	_ZSt24__throw_invalid_argumentPKc
.L55:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2314:
	.size	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, .-_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDE8:
	.section	.text._ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTE8:
	.weak	_ZN9__gnu_cxx6__stoaIlicIiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.set	_ZN9__gnu_cxx6__stoaIlicIiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
	.align 2
.LCOLDB9:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTB9:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE:
.LFB2542:
	.cfi_startproc
	testq	%rsi, %rsi
	je	.L66
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
.L62:
	movq	24(%rbx), %rsi
	movq	%r12, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	16(%rbx), %rbp
	movq	%rbx, %rdi
	call	_ZdlPv
	testq	%rbp, %rbp
	movq	%rbp, %rbx
	jne	.L62
	popq	%rbx
	.cfi_restore 3
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_restore 6
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_restore 12
	.cfi_def_cfa_offset 8
.L66:
	rep ret
	.cfi_endproc
.LFE2542:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LCOLDE9:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE,comdat
.LHOTE9:
	.section	.text.unlikely
	.align 2
.LCOLDB10:
	.text
.LHOTB10:
	.align 2
	.p2align 4,,15
	.globl	_ZN5GraphC2Ei
	.type	_ZN5GraphC2Ei, @function
_ZN5GraphC2Ei:
.LFB2299:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2299
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	leaq	24(%rdi), %rax
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	movslq	%esi, %rbx
	movq	%rdi, %rbp
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movq	%rax, 40(%rdi)
	movq	%rax, 48(%rdi)
	movabsq	$382805968326492160, %rax
	movl	$0, 24(%rdi)
	movq	$0, 32(%rdi)
	cmpq	%rax, %rbx
	movq	$0, 56(%rdi)
	movl	%esi, (%rdi)
	movl	$0, 4(%rdi)
	movq	$-1, %rdi
	ja	.L68
	leaq	(%rbx,%rbx,2), %rax
	leaq	8(,%rax,8), %rdi
.L68:
.LEHB7:
	call	_Znam
.LEHE7:
	movq	%rbx, (%rax)
	xorl	%ecx, %ecx
	addq	$8, %rax
	testq	%rbx, %rbx
	movq	%rax, %rdx
	je	.L70
	.p2align 4,,10
	.p2align 3
.L75:
	addq	$1, %rcx
	movq	$0, 16(%rdx)
	movq	%rdx, (%rdx)
	movq	%rdx, 8(%rdx)
	addq	$24, %rdx
	cmpq	%rcx, %rbx
	jne	.L75
.L70:
	movq	%rax, 8(%rbp)
	addq	$8, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L74:
	.cfi_restore_state
	movq	32(%rbp), %rsi
	leaq	16(%rbp), %rdi
	movq	%rax, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB8:
	call	_Unwind_Resume
.LEHE8:
	.cfi_endproc
.LFE2299:
	.section	.gcc_except_table
.LLSDA2299:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2299-.LLSDACSB2299
.LLSDACSB2299:
	.uleb128 .LEHB7-.LFB2299
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L74-.LFB2299
	.uleb128 0
	.uleb128 .LEHB8-.LFB2299
	.uleb128 .LEHE8-.LEHB8
	.uleb128 0
	.uleb128 0
.LLSDACSE2299:
	.text
	.size	_ZN5GraphC2Ei, .-_ZN5GraphC2Ei
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.globl	_ZN5GraphC1Ei
	.set	_ZN5GraphC1Ei,_ZN5GraphC2Ei
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
	.align 2
.LCOLDB11:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTB11:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_:
.LFB2561:
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
	je	.L90
	movl	(%rsi), %ecx
	jmp	.L81
	.p2align 4,,10
	.p2align 3
.L96:
	movq	16(%rbx), %rax
	testq	%rax, %rax
	je	.L82
.L97:
	movq	%rax, %rbx
.L81:
	movl	32(%rbx), %edx
	cmpl	%ecx, %edx
	jg	.L96
	movq	24(%rbx), %rax
	testq	%rax, %rax
	jne	.L97
.L82:
	cmpl	%ecx, %edx
	movq	%rbx, %rax
	jg	.L80
	cmpl	%ecx, %edx
	jl	.L86
.L94:
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
.L90:
	.cfi_restore_state
	movq	%r12, %rbx
	.p2align 4,,10
	.p2align 3
.L80:
	cmpq	%rbx, 24(%r13)
	je	.L86
	movq	%rbx, %rdi
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movl	(%r14), %ecx
	movl	32(%rax), %edx
	cmpl	%ecx, %edx
	jge	.L94
.L86:
	cmpq	%rbx, %r12
	je	.L92
	xorl	%r15d, %r15d
	movl	32(%rbx), %eax
	cmpl	%eax, (%r14)
	setl	%r15b
.L87:
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
.L92:
	.cfi_restore_state
	movl	$1, %r15d
	jmp	.L87
	.cfi_endproc
.LFE2561:
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LCOLDE11:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_,comdat
.LHOTE11:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.align 2
.LCOLDB12:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTB12:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_:
.LFB2726:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2726
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
	je	.L99
	movq	8(%r15), %rax
	testq	%rax, %rax
	movq	%rax, 8(%rcx)
	je	.L100
	cmpq	24(%rax), %r15
	je	.L154
	movq	$0, 16(%rax)
.L105:
	movl	32(%rbx), %eax
	movl	%eax, 32(%r15)
.L120:
	movl	(%rbx), %eax
	movq	$0, 24(%r15)
	cmpq	$0, 24(%rbx)
	movq	$0, 16(%r15)
	movq	%rdx, 8(%r15)
	movl	%eax, (%r15)
	je	.L106
	movq	24(%rbx), %rsi
	movq	%r12, %rcx
	movq	%r15, %rdx
	movq	%r14, %rdi
.LEHB9:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%r15)
.L106:
	movq	16(%rbx), %rbp
	movq	%r15, %r13
	testq	%rbp, %rbp
	jne	.L142
	jmp	.L135
	.p2align 4,,10
	.p2align 3
.L110:
	movq	$0, 16(%rax)
.L150:
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
	je	.L115
	movq	%r12, %rcx
	movq	%rbx, %rdx
	movq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	movq	%rax, 24(%rbx)
.L115:
	movq	16(%rbp), %rbp
	testq	%rbp, %rbp
	je	.L135
	movq	%rbx, %r13
.L142:
	movq	8(%r12), %rbx
	testq	%rbx, %rbx
	je	.L108
	movq	8(%rbx), %rax
	testq	%rax, %rax
	movq	%rax, 8(%r12)
	je	.L109
	cmpq	24(%rax), %rbx
	jne	.L110
	movq	$0, 24(%rax)
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L150
	movq	24(%rax), %rdx
	movq	%rax, 8(%r12)
	testq	%rdx, %rdx
	jne	.L113
	jmp	.L155
	.p2align 4,,10
	.p2align 3
.L126:
	movq	%rax, %rdx
.L113:
	movq	24(%rdx), %rax
	testq	%rax, %rax
	jne	.L126
	movq	%rdx, 8(%r12)
.L112:
	movq	16(%rdx), %rax
	testq	%rax, %rax
	je	.L150
	movq	%rax, 8(%r12)
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L109:
	movq	$0, (%r12)
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L108:
	movl	$40, %edi
	call	_Znwm
.LEHE9:
	movq	%rax, %rbx
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L135:
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
.L155:
	.cfi_restore_state
	movq	%rax, %rdx
	jmp	.L112
.L154:
	movq	$0, 24(%rax)
	movq	16(%rax), %rax
	testq	%rax, %rax
	je	.L105
	movq	%rax, 8(%rcx)
	movq	24(%rax), %rcx
	testq	%rcx, %rcx
	jne	.L104
	jmp	.L156
	.p2align 4,,10
	.p2align 3
.L124:
	movq	%rax, %rcx
.L104:
	movq	24(%rcx), %rax
	testq	%rax, %rax
	jne	.L124
	movq	%rcx, 8(%r12)
.L103:
	movq	16(%rcx), %rax
	testq	%rax, %rax
	je	.L105
	movq	%rax, 8(%r12)
	jmp	.L105
.L100:
	movq	$0, (%rcx)
	jmp	.L105
.L99:
	movl	$40, %edi
	movq	%rdx, 8(%rsp)
.LEHB10:
	call	_Znwm
.LEHE10:
	movq	%rax, %r15
	movl	32(%rbx), %eax
	movq	8(%rsp), %rdx
	movl	%eax, 32(%r15)
	jmp	.L120
.L156:
	movq	%rax, %rcx
	jmp	.L103
.L127:
.L118:
	movq	%rax, %rdi
	call	__cxa_begin_catch
	movq	%r15, %rsi
	movq	%r14, %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.LEHB11:
	call	__cxa_rethrow
.LEHE11:
.L128:
	movq	%rax, %rbx
.L119:
	call	__cxa_end_catch
	movq	%rbx, %rdi
.LEHB12:
	call	_Unwind_Resume
.LEHE12:
	.cfi_endproc
.LFE2726:
	.section	.gcc_except_table
	.align 4
.LLSDA2726:
	.byte	0xff
	.byte	0x3
	.uleb128 .LLSDATT2726-.LLSDATTD2726
.LLSDATTD2726:
	.byte	0x1
	.uleb128 .LLSDACSE2726-.LLSDACSB2726
.LLSDACSB2726:
	.uleb128 .LEHB9-.LFB2726
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L127-.LFB2726
	.uleb128 0x1
	.uleb128 .LEHB10-.LFB2726
	.uleb128 .LEHE10-.LEHB10
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB11-.LFB2726
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L128-.LFB2726
	.uleb128 0
	.uleb128 .LEHB12-.LFB2726
	.uleb128 .LEHE12-.LEHB12
	.uleb128 0
	.uleb128 0
.LLSDACSE2726:
	.byte	0x1
	.byte	0
	.align 4
	.long	0

.LLSDATT2726:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LCOLDE12:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_,comdat
.LHOTE12:
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
	.align 2
.LCOLDB13:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LHOTB13:
	.align 2
	.p2align 4,,15
	.weak	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
	.type	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_, @function
_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_:
.LFB2577:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2577
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
	je	.L158
	movq	16(%rdi), %rax
	movq	32(%rdi), %rdx
	movq	%rsi, %rbp
	movq	%rdi, 16(%rsp)
	testq	%rax, %rax
	movq	%rax, (%rsp)
	movq	%rdx, 8(%rsp)
	je	.L159
	movq	16(%rdx), %rdx
	movq	$0, 8(%rax)
	testq	%rdx, %rdx
	je	.L160
	movq	%rdx, 8(%rsp)
.L160:
	leaq	8(%rbx), %rdx
	movq	$0, 16(%rbx)
	movq	$0, 40(%rbx)
	movq	%rdx, 24(%rbx)
	movq	%rdx, 32(%rbx)
	movq	16(%rbp), %rsi
	testq	%rsi, %rsi
	je	.L166
	movq	%rsp, %rcx
	movq	%rbx, %rdi
.LEHB13:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE7_M_copyINS5_20_Reuse_or_alloc_nodeEEEPSt13_Rb_tree_nodeIiEPKS9_SA_RT_
.LEHE13:
	movq	%rax, 16(%rbx)
	movq	%rax, %rcx
	jmp	.L162
	.p2align 4,,10
	.p2align 3
.L167:
	movq	%rdx, %rcx
.L162:
	movq	16(%rcx), %rdx
	testq	%rdx, %rdx
	jne	.L167
	movq	%rcx, 24(%rbx)
	jmp	.L163
	.p2align 4,,10
	.p2align 3
.L168:
	movq	%rdx, %rax
.L163:
	movq	24(%rax), %rdx
	testq	%rdx, %rdx
	jne	.L168
	movq	%rax, 32(%rbx)
	movq	40(%rbp), %rax
	movq	16(%rsp), %rdi
	movq	%rax, 40(%rbx)
	movq	(%rsp), %rax
.L161:
	movq	%rax, %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
.L158:
	movq	24(%rsp), %rdi
	xorq	%fs:40, %rdi
	movq	%rbx, %rax
	jne	.L176
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
.L159:
	.cfi_restore_state
	movq	$0, 8(%rsp)
	jmp	.L160
	.p2align 4,,10
	.p2align 3
.L166:
	movq	%rbx, %rdi
	jmp	.L161
.L169:
	movq	%rax, %rbx
	jmp	.L164
.L176:
	call	__stack_chk_fail
.L164:
	movq	16(%rsp), %rdi
	movq	(%rsp), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB14:
	call	_Unwind_Resume
.LEHE14:
	.cfi_endproc
.LFE2577:
	.section	.gcc_except_table
.LLSDA2577:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2577-.LLSDACSB2577
.LLSDACSB2577:
	.uleb128 .LEHB13-.LFB2577
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L169-.LFB2577
	.uleb128 0
	.uleb128 .LEHB14-.LFB2577
	.uleb128 .LEHE14-.LEHB14
	.uleb128 0
	.uleb128 0
.LLSDACSE2577:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
	.size	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_, .-_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
	.section	.text.unlikely._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LCOLDE13:
	.section	.text._ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,"axG",@progbits,_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_,comdat
.LHOTE13:
	.section	.text.unlikely
	.align 2
.LCOLDB14:
	.text
.LHOTB14:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.type	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, @function
_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_:
.LFB2303:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2303
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movl	%esi, %r14d
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdx, %rax
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rcx, %r11
	subq	$200, %rsp
	.cfi_def_cfa_offset 256
	movq	%rdx, 8(%rsp)
	movslq	%r14d, %rdx
	movq	%rcx, 64(%rsp)
	movq	%fs:40, %rcx
	movq	%rcx, 184(%rsp)
	xorl	%ecx, %ecx
	leaq	0(,%rdx,4), %rcx
	leaq	136(%rsp), %rsi
	movq	$0, 144(%rsp)
	movq	%rdi, 48(%rsp)
	movq	%r9, 24(%rsp)
	addq	%rcx, %rax
	movq	%rcx, %r10
	movq	%rcx, 32(%rsp)
	movq	%rax, 56(%rsp)
	movq	%rax, %rcx
	movq	%r11, %rax
	addq	%r10, %rax
	movq	%rsi, 152(%rsp)
	movq	%rsi, 160(%rsp)
	movq	%rax, %r10
	movq	%rax, 40(%rsp)
	movl	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip), %eax
	movl	$0, 136(%rsp)
	movq	$0, 168(%rsp)
	addl	$1, %eax
	movl	%eax, (%r10)
	movl	%eax, _ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time(%rip)
	movl	%eax, (%rcx)
	leaq	(%rdx,%rdx,2), %rax
	movq	8(%rdi), %rcx
	salq	$3, %rax
	movq	%rax, 16(%rsp)
	addq	%rcx, %rax
	movq	(%rax), %r13
	cmpq	%r13, %rax
	je	.L199
	leal	1(%r14), %eax
	leaq	16(%rdi), %rdx
	movq	%r8, %rbx
	movl	$0, 80(%rsp)
	movq	%rsi, 72(%rsp)
	movl	%eax, 84(%rsp)
	movq	%rdi, %rax
	movq	%rdx, 88(%rsp)
	addq	$24, %rax
	movq	%rax, 96(%rsp)
	jmp	.L193
	.p2align 4,,10
	.p2align 3
.L179:
	movq	24(%rsp), %rax
	movq	32(%rsp), %rsi
	cmpl	(%rax,%rsi), %r12d
	je	.L182
	movq	40(%rsp), %rax
	cmpl	(%rax), %edx
	jge	.L182
	movl	%edx, (%rax)
	movl	$24, %edi
.LEHB15:
	call	_Znwm
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movq	%rbx, %rsi
	movl	%r14d, 16(%rax)
	movl	%r12d, 20(%rax)
	movq	%rax, %rdi
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%rbx)
.L232:
	movq	48(%rsp), %rax
	movq	8(%rax), %rcx
.L182:
	movq	16(%rsp), %rax
	movq	0(%r13), %r13
	addq	%rcx, %rax
	cmpq	%rax, %r13
	je	.L237
.L193:
	movslq	16(%r13), %rax
	movq	8(%rsp), %rsi
	movl	(%rsi,%rax,4), %edx
	movq	%rax, %r12
	leaq	0(,%rax,4), %rbp
	cmpl	$-1, %edx
	jne	.L179
	movq	24(%rsp), %r15
	movl	$24, %edi
	addl	$1, 80(%rsp)
	movl	%r14d, (%r15,%rax,4)
	call	_Znwm
	movq	%rbx, %rsi
	movq	%rax, %rdi
	movq	$0, (%rax)
	movq	$0, 8(%rax)
	movl	%r14d, 16(%rax)
	movl	%r12d, 20(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	movq	%r15, %r9
	addq	$1, 16(%rbx)
	movq	64(%rsp), %r15
	movq	8(%rsp), %rdx
	movq	48(%rsp), %rdi
	movq	%rbx, %r8
	movl	%r12d, %esi
	movq	%r15, %rcx
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	movq	40(%rsp), %rcx
	addq	%r15, %rbp
	movl	(%rcx), %eax
	cmpl	%eax, 0(%rbp)
	cmovle	0(%rbp), %eax
	movl	%eax, (%rcx)
	movq	56(%rsp), %rax
	movl	(%rax), %eax
	cmpl	$1, %eax
	je	.L238
	jle	.L232
	cmpl	0(%rbp), %eax
	jg	.L232
	leaq	124(%rsp), %rbp
	jmp	.L215
	.p2align 4,,10
	.p2align 3
.L183:
	leaq	128(%rsp), %rdi
	addl	$1, %eax
	movq	%rbp, %rsi
	movl	%eax, 124(%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	128(%rsp), %rdi
	movq	%rbp, %rsi
	movl	20(%rax), %eax
	addl	$1, %eax
	movl	%eax, 124(%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %r15
	subq	$1, 16(%rbx)
	movq	%r15, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r15, %rdi
	call	_ZdlPv
.L215:
	movq	8(%rbx), %rdx
	movl	16(%rdx), %eax
	cmpl	%eax, %r14d
	jne	.L183
	cmpl	20(%rdx), %r12d
	jne	.L183
	movl	84(%rsp), %eax
	leaq	128(%rsp), %rdi
	movq	%rbp, %rsi
	movl	%eax, 124(%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rax
	leaq	128(%rsp), %rdi
	movq	%rbp, %rsi
	movl	20(%rax), %eax
	addl	$1, %eax
	movl	%eax, 124(%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	8(%rbx), %rbp
	subq	$1, 16(%rbx)
	movq	%rbp, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%rbp, %rdi
	call	_ZdlPv
	movq	48(%rsp), %rax
	movq	56(%rax), %rax
	cmpq	%rax, 168(%rsp)
	ja	.L185
	je	.L239
.L188:
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	addl	$1, count_t(%rip)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	72(%rsp), %rax
	movq	$0, 144(%rsp)
	movq	$0, 168(%rsp)
	movq	%rax, 152(%rsp)
	movq	%rax, 160(%rsp)
	movq	48(%rsp), %rax
	movq	8(%rax), %rcx
	jmp	.L182
	.p2align 4,,10
	.p2align 3
.L238:
	cmpl	$1, 80(%rsp)
	leaq	124(%rsp), %rbp
	jne	.L215
	jmp	.L232
.L241:
	movq	104(%rsp), %rbx
	.p2align 4,,10
	.p2align 3
.L185:
	movq	88(%rsp), %rdi
	leaq	128(%rsp), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
.LEHE15:
	jmp	.L188
.L237:
	movq	144(%rsp), %rsi
.L178:
	leaq	128(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	184(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L240
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
.L239:
	.cfi_restore_state
	movq	48(%rsp), %rax
	movq	152(%rsp), %rbp
	movq	40(%rax), %r12
	cmpq	%r12, 96(%rsp)
	setne	%al
	cmpq	72(%rsp), %rbp
	movl	%eax, %edx
	je	.L187
	testb	%al, %al
	je	.L187
	movl	32(%r12), %eax
	cmpl	%eax, 32(%rbp)
	jl	.L185
	jg	.L188
	movq	%rbx, 104(%rsp)
	movq	72(%rsp), %r15
	movq	%r12, %rbx
	movq	96(%rsp), %r12
	jmp	.L190
	.p2align 4,,10
	.p2align 3
.L243:
	testb	%al, %al
	je	.L230
	movl	32(%rbx), %eax
	cmpl	%eax, 32(%rbp)
	jl	.L241
	jg	.L242
.L190:
	movq	%rbp, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%rbx, %rdi
	movq	%rax, %rbp
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %r12
	movq	%rax, %rbx
	setne	%al
	cmpq	%r15, %rbp
	movl	%eax, %edx
	jne	.L243
.L230:
	movq	104(%rsp), %rbx
.L187:
	cmpq	72(%rsp), %rbp
	jne	.L188
	testb	%dl, %dl
	jne	.L185
	jmp	.L188
	.p2align 4,,10
	.p2align 3
.L242:
	movq	104(%rsp), %rbx
	jmp	.L188
.L199:
	xorl	%esi, %esi
	jmp	.L178
.L200:
	movq	144(%rsp), %rsi
	leaq	128(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB16:
	call	_Unwind_Resume
.LEHE16:
.L240:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2303:
	.section	.gcc_except_table
.LLSDA2303:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2303-.LLSDACSB2303
.LLSDACSB2303:
	.uleb128 .LEHB15-.LFB2303
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L200-.LFB2303
	.uleb128 0
	.uleb128 .LEHB16-.LFB2303
	.uleb128 .LEHE16-.LEHB16
	.uleb128 0
	.uleb128 0
.LLSDACSE2303:
	.text
	.size	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_, .-_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
	.section	.text.unlikely
.LCOLDE14:
	.text
.LHOTE14:
	.section	.text.unlikely
	.align 2
.LCOLDB15:
	.text
.LHOTB15:
	.align 2
	.p2align 4,,15
	.globl	_ZN5Graph3BCCEv
	.type	_ZN5Graph3BCCEv, @function
_ZN5Graph3BCCEv:
.LFB2304:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2304
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
	subq	$152, %rsp
	.cfi_def_cfa_offset 208
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	movslq	(%rdi), %rax
	cmpq	%rbx, %rax
	ja	.L245
	movq	%rdi, %r12
	leaq	0(,%rax,4), %rdi
.LEHB17:
	call	_Znam
	movq	%rax, %r13
	movslq	(%r12), %rax
	cmpq	%rbx, %rax
	ja	.L245
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movq	%rax, (%rsp)
	movslq	(%r12), %rax
	cmpq	%rbx, %rax
	ja	.L245
	leaq	0(,%rax,4), %rdi
	call	_Znam
	movslq	4(%r12), %rbp
	movq	%rax, 8(%rsp)
	movabsq	$382805968326492160, %rax
	movq	$-1, %rdi
	cmpq	%rax, %rbp
	ja	.L247
	leaq	0(%rbp,%rbp,2), %rax
	leaq	8(,%rax,8), %rdi
.L247:
	call	_Znam
.LEHE17:
	movq	%rbp, (%rax)
	movq	%rax, %rbx
	leaq	8(%rax), %rax
	xorl	%edx, %edx
	testq	%rbp, %rbp
	movq	%rax, 16(%rsp)
	je	.L251
.L290:
	addq	$1, %rdx
	movq	$0, 16(%rax)
	movq	%rax, (%rax)
	movq	%rax, 8(%rax)
	addq	$24, %rax
	cmpq	%rdx, %rbp
	jne	.L290
.L251:
	movl	(%r12), %edx
	leaq	88(%rsp), %rax
	movl	$0, 88(%rsp)
	movq	$0, 96(%rsp)
	movq	$0, 120(%rsp)
	movq	%rax, 104(%rsp)
	movq	%rax, 112(%rsp)
	testl	%edx, %edx
	jle	.L273
	movq	(%rsp), %rcx
	movq	8(%rsp), %rsi
	xorl	%eax, %eax
.L252:
	movl	$-1, 0(%r13,%rax,4)
	movl	$-1, (%rcx,%rax,4)
	movl	$-1, (%rsi,%rax,4)
	addq	$1, %rax
	cmpl	%eax, %edx
	jg	.L252
	leaq	16(%r12), %rax
	xorl	%ebp, %ebp
	movq	%rax, 48(%rsp)
	leaq	24(%r12), %rax
	movq	%rax, 56(%rsp)
	leaq	88(%rsp), %rax
	movq	%rax, 40(%rsp)
	.p2align 4,,10
	.p2align 3
.L266:
	cmpl	$-1, 0(%r13,%rbp,4)
	je	.L253
.L256:
	cmpq	$0, 24(%rbx)
	je	.L255
	.p2align 4,,10
	.p2align 3
.L286:
	movq	16(%rbx), %rax
	leaq	76(%rsp), %rsi
	leaq	80(%rsp), %rdi
	movl	16(%rax), %eax
	addl	$1, %eax
	movl	%eax, 76(%rsp)
.LEHB18:
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	16(%rbx), %rax
	leaq	76(%rsp), %rsi
	leaq	80(%rsp), %rdi
	movl	20(%rax), %eax
	addl	$1, %eax
	movl	%eax, 76(%rsp)
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE16_M_insert_uniqueIiEESt4pairISt17_Rb_tree_iteratorIiEbEOT_
	movq	16(%rbx), %r14
	subq	$1, 24(%rbx)
	movq	%r14, %rdi
	call	_ZNSt8__detail15_List_node_base9_M_unhookEv
	movq	%r14, %rdi
	call	_ZdlPv
	cmpq	$0, 24(%rbx)
	jne	.L286
	movq	56(%r12), %rax
	cmpq	%rax, 120(%rsp)
	jbe	.L308
.L260:
	movq	48(%rsp), %rdi
	leaq	80(%rsp), %rsi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEEaSERKS5_
.L261:
	addl	$1, count_t(%rip)
.L255:
	leal	1(%rbp), %eax
	addq	$1, %rbp
	cmpl	%eax, (%r12)
	jg	.L266
	movq	96(%rsp), %rsi
.L249:
	leaq	80(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	136(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L309
	addq	$152, %rsp
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
.L308:
	.cfi_restore_state
	jne	.L261
	movq	40(%r12), %r15
	cmpq	%r15, 56(%rsp)
	movq	104(%rsp), %r14
	setne	%al
	cmpq	40(%rsp), %r14
	movl	%eax, %esi
	je	.L259
	testb	%al, %al
	je	.L259
	movl	32(%r15), %eax
	cmpl	%eax, 32(%r14)
	jl	.L260
	jg	.L261
	movq	%r12, %rax
	movq	%r13, 24(%rsp)
	movq	%rbx, 32(%rsp)
	movq	%r14, %r13
	movq	%r15, %r12
	movq	%rbp, %r14
	movq	56(%rsp), %rbx
	movq	40(%rsp), %rbp
	movq	%rax, %r15
	jmp	.L263
.L312:
	testb	%al, %al
	je	.L303
	movl	32(%r12), %eax
	cmpl	%eax, 32(%r13)
	jl	.L310
	jg	.L311
.L263:
	movq	%r13, %rdi
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	movq	%r12, %rdi
	movq	%rax, %r13
	call	_ZSt18_Rb_tree_incrementPKSt18_Rb_tree_node_base
	cmpq	%rax, %rbx
	movq	%rax, %r12
	setne	%al
	cmpq	%rbp, %r13
	movl	%eax, %esi
	jne	.L312
.L303:
	movq	%r14, %rbp
	movq	32(%rsp), %rbx
	movq	%r13, %r14
	movq	24(%rsp), %r13
	movq	%r15, %r12
.L259:
	cmpq	40(%rsp), %r14
	jne	.L261
	testb	%sil, %sil
	jne	.L260
	jmp	.L261
	.p2align 4,,10
	.p2align 3
.L253:
	movq	8(%rsp), %r9
	movq	16(%rsp), %r8
	movq	%r13, %rdx
	movq	(%rsp), %rcx
	movl	%ebp, %esi
	movq	%r12, %rdi
	call	_ZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_
.LEHE18:
	jmp	.L256
.L311:
	movq	24(%rsp), %r13
	movq	32(%rsp), %rbx
	movq	%r14, %rbp
	movq	%r15, %r12
	jmp	.L261
.L310:
	movq	24(%rsp), %r13
	movq	32(%rsp), %rbx
	movq	%r14, %rbp
	movq	%r15, %r12
	jmp	.L260
.L273:
	xorl	%esi, %esi
	jmp	.L249
.L274:
	movq	96(%rsp), %rsi
	leaq	80(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	%rbx, %rdi
.LEHB19:
	call	_Unwind_Resume
.L309:
	call	__stack_chk_fail
.L245:
	call	__cxa_throw_bad_array_new_length
.LEHE19:
	.cfi_endproc
.LFE2304:
	.section	.gcc_except_table
.LLSDA2304:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2304-.LLSDACSB2304
.LLSDACSB2304:
	.uleb128 .LEHB17-.LFB2304
	.uleb128 .LEHE17-.LEHB17
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB18-.LFB2304
	.uleb128 .LEHE18-.LEHB18
	.uleb128 .L274-.LFB2304
	.uleb128 0
	.uleb128 .LEHB19-.LFB2304
	.uleb128 .LEHE19-.LEHB19
	.uleb128 0
	.uleb128 0
.LLSDACSE2304:
	.text
	.size	_ZN5Graph3BCCEv, .-_ZN5Graph3BCCEv
	.section	.text.unlikely
.LCOLDE15:
	.text
.LHOTE15:
	.section	.rodata.str1.1
.LC16:
	.string	"./food.inp"
.LC17:
	.string	"stoi"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC18:
	.string	"basic_string::_M_construct null not valid"
	.section	.text.unlikely
.LCOLDB19:
	.section	.text.startup,"ax",@progbits
.LHOTB19:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB2309:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA2309
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
	movl	$.LC16, %esi
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$1064, %rsp
	.cfi_def_cfa_offset 1120
	leaq	528(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1048(%rsp)
	xorl	%eax, %eax
.LEHB20:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1EPKcSt13_Ios_Openmode
.LEHE20:
	leaq	112(%rsp), %rax
	leaq	648(%rsp), %rdi
	movq	$0, 104(%rsp)
	movb	$0, 112(%rsp)
	movl	$0, 56(%rsp)
	movq	%rax, 96(%rsp)
	leaq	56(%rsp), %rax
	movq	$0, 64(%rsp)
	movq	$0, 88(%rsp)
	movq	%rax, 72(%rsp)
	movq	%rax, 80(%rsp)
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	je	.L343
	leaq	96(%rsp), %rsi
	leaq	528(%rsp), %rdi
.LEHB21:
	call	_ZSt7getlineIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	96(%rsp), %rdx
	movl	$10, %r8d
	xorl	%ecx, %ecx
	movl	$.LC17, %esi
	movl	$strtol, %edi
	call	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	leaq	32(%rsp), %rdi
	movl	%eax, %esi
	call	_ZN5Graph10setVerticeEi
	movq	528(%rsp), %rax
	leaq	256(%rsp), %r15
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+16(%rip), %rbx
	movq	-24(%rax), %rax
	movq	768(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	je	.L341
	.p2align 4,,10
	.p2align 3
.L371:
	cmpb	$0, 56(%rbp)
	je	.L317
	movsbl	67(%rbp), %edx
.L318:
	leaq	96(%rsp), %rsi
	leaq	528(%rsp), %rdi
	call	_ZSt7getlineIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EES4_
.LEHE21:
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L319
	movq	%r15, %rdi
	call	_ZNSt8ios_baseC2Ev
	movb	$0, 480(%rsp)
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	leaq	128(%rsp), %rdi
	movq	-24(%rbx), %rax
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 256(%rsp)
	xorl	%esi, %esi
	movq	$0, 472(%rsp)
	movb	$0, 481(%rsp)
	movq	$0, 488(%rsp)
	movq	$0, 496(%rsp)
	movq	$0, 504(%rsp)
	movq	$0, 512(%rsp)
	movq	%rbx, 128(%rsp)
	movq	%rcx, 128(%rsp,%rax)
	movq	$0, 136(%rsp)
	addq	-24(%rbx), %rdi
.LEHB22:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE22:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+32(%rip), %rbp
	xorl	%esi, %esi
	movq	-24(%rbp), %rax
	movq	%rbp, 144(%rsp)
	leaq	144(%rsp,%rax), %rdi
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rax
	movq	%rax, (%rdi)
.LEHB23:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE23:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+8(%rip), %r14
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	leaq	208(%rsp), %rdi
	movq	-24(%r14), %rax
	movq	%rcx, 128(%rsp,%rax)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 128(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 256(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 144(%rsp)
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 152(%rsp)
	movq	$0, 160(%rsp)
	movq	$0, 168(%rsp)
	movq	$0, 176(%rsp)
	movq	$0, 184(%rsp)
	movq	$0, 192(%rsp)
	movq	$0, 200(%rsp)
	call	_ZNSt6localeC1Ev
	movq	96(%rsp), %r13
	leaq	240(%rsp), %rax
	movq	104(%rsp), %r12
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 152(%rsp)
	movl	$0, 216(%rsp)
	movq	%rax, 224(%rsp)
	movq	%r13, %rax
	addq	%r12, %rax
	je	.L322
	testq	%r13, %r13
	jne	.L322
	movl	$.LC18, %edi
.LEHB24:
	call	_ZSt19__throw_logic_errorPKc
.LEHE24:
.L322:
	cmpq	$15, %r12
	movq	%r12, 24(%rsp)
	ja	.L384
	cmpq	$1, %r12
	je	.L385
	testq	%r12, %r12
	jne	.L386
.L375:
	movq	224(%rsp), %rax
.L327:
	movq	%r12, 232(%rsp)
	movb	$0, (%rax,%r12)
	leaq	128(%rsp), %rax
	movq	224(%rsp), %rsi
	xorl	%ecx, %ecx
	xorl	%edx, %edx
	leaq	24(%rax), %rdi
	movl	$24, 216(%rsp)
.LEHB25:
	call	_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEE7_M_syncEPcmm
.LEHE25:
	leaq	128(%rsp), %rax
	movq	%r15, %rdi
	leaq	24(%rax), %rsi
.LEHB26:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE26:
	leaq	96(%rsp), %rsi
	leaq	128(%rsp), %rdi
.LEHB27:
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	96(%rsp), %rdx
	movl	$10, %r8d
	xorl	%ecx, %ecx
	movl	$.LC17, %esi
	movl	$strtol, %edi
	call	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	subl	$1, %eax
	cltq
	leaq	(%rax,%rax,2), %r13
	salq	$3, %r13
	jmp	.L338
	.p2align 4,,10
	.p2align 3
.L388:
	movq	96(%rsp), %rdx
	movl	$10, %r8d
	xorl	%ecx, %ecx
	movl	$.LC17, %esi
	movl	$strtol, %edi
	call	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	testl	%eax, %eax
	jne	.L387
.L338:
	leaq	96(%rsp), %rsi
	leaq	128(%rsp), %rdi
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
.LEHE27:
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	je	.L388
	movq	224(%rsp), %rdi
	leaq	240(%rsp), %rax
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 128(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 256(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 144(%rsp)
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 152(%rsp)
	cmpq	%rax, %rdi
	je	.L340
	call	_ZdlPv
.L340:
	leaq	208(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 152(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r14), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	movq	%r15, %rdi
	movq	%rcx, 128(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 144(%rsp,%rax)
	movq	-24(%rbx), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	%rcx, 128(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 256(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	528(%rsp), %rax
	movq	-24(%rax), %rax
	movq	768(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	jne	.L371
.L341:
.LEHB28:
	call	_ZSt16__throw_bad_castv
.LEHE28:
	.p2align 4,,10
	.p2align 3
.L387:
	movq	96(%rsp), %rdx
	movl	$10, %r8d
	xorl	%ecx, %ecx
	movl	$.LC17, %esi
	movl	$strtol, %edi
.LEHB29:
	call	_ZN9__gnu_cxx6__stoaIlicJiEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	subl	$1, %eax
	movl	$24, %edi
	movq	%r13, %r12
	movl	%eax, 12(%rsp)
	addq	40(%rsp), %r12
	call	_Znwm
.LEHE29:
	movl	12(%rsp), %ecx
	movq	$0, (%rax)
	movq	%r12, %rsi
	movq	$0, 8(%rax)
	movq	%rax, %rdi
	movl	%ecx, 16(%rax)
	call	_ZNSt8__detail15_List_node_base7_M_hookEPS0_
	addq	$1, 16(%r12)
	addl	$1, 36(%rsp)
	jmp	.L338
.L317:
	movq	%rbp, %rdi
.LEHB30:
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %edx
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L318
	movl	$10, %esi
	movq	%rbp, %rdi
	call	*%rax
.LEHE30:
	movsbl	%al, %edx
	jmp	.L318
.L384:
	leaq	128(%rsp), %rax
	leaq	24(%rsp), %rsi
	xorl	%edx, %edx
	leaq	96(%rax), %rdi
.LEHB31:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_createERmm
.LEHE31:
	movq	%rax, %rdi
	movq	%rax, 224(%rsp)
	movq	24(%rsp), %rax
	movq	%rax, 240(%rsp)
.L325:
	movq	%r12, %rdx
	movq	%r13, %rsi
	call	memcpy
	movq	24(%rsp), %r12
	jmp	.L375
.L385:
	movzbl	0(%r13), %eax
	movb	%al, 240(%rsp)
	leaq	240(%rsp), %rax
	jmp	.L327
.L319:
	leaq	528(%rsp), %rdi
.LEHB32:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE5closeEv
.L343:
	leaq	32(%rsp), %rdi
	call	_ZN5Graph3BCCEv
	leaq	32(%rsp), %rdi
	call	_ZN5Graph24getMaxBiconnectComponentEv
.LEHE32:
	movq	64(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	96(%rsp), %rdi
	leaq	112(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L344
	call	_ZdlPv
.L344:
	leaq	528(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	xorl	%eax, %eax
	movq	1048(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L389
	addq	$1064, %rsp
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
.L386:
	.cfi_restore_state
	leaq	240(%rsp), %rdi
	jmp	.L325
.L357:
	movq	%rax, %r12
.L335:
	leaq	208(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 152(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r14), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	movq	%rcx, 128(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 144(%rsp,%rax)
	movq	-24(%rbx), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rbx
	movq	%rbx, 128(%rsp,%rax)
	movq	%r12, %rbx
.L324:
	leaq	256(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 256(%rsp)
	call	_ZNSt8ios_baseD2Ev
.L336:
	movq	64(%rsp), %rsi
	leaq	48(%rsp), %rdi
	call	_ZNSt8_Rb_treeIiiSt9_IdentityIiESt4lessIiESaIiEE8_M_eraseEPSt13_Rb_tree_nodeIiE
	movq	96(%rsp), %rdi
	leaq	112(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L346
	call	_ZdlPv
.L346:
	leaq	528(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rdi
.LEHB33:
	call	_Unwind_Resume
.LEHE33:
.L358:
	movq	%rax, %r12
.L378:
	movq	224(%rsp), %rdi
	leaq	240(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L335
	call	_ZdlPv
	jmp	.L335
.L355:
	movq	%rax, %r12
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 152(%rsp)
	jmp	.L378
.L353:
	leaq	128(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEED1Ev
	jmp	.L336
.L389:
	call	__stack_chk_fail
.L352:
	movq	%rax, %rbx
	jmp	.L336
.L354:
	movq	%rax, %rbx
	jmp	.L324
.L356:
	movq	-24(%rbx), %rdx
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rbx
	movq	%rbx, 128(%rsp,%rdx)
	movq	%rax, %rbx
	jmp	.L324
	.cfi_endproc
.LFE2309:
	.section	.gcc_except_table
.LLSDA2309:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE2309-.LLSDACSB2309
.LLSDACSB2309:
	.uleb128 .LEHB20-.LFB2309
	.uleb128 .LEHE20-.LEHB20
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB21-.LFB2309
	.uleb128 .LEHE21-.LEHB21
	.uleb128 .L352-.LFB2309
	.uleb128 0
	.uleb128 .LEHB22-.LFB2309
	.uleb128 .LEHE22-.LEHB22
	.uleb128 .L354-.LFB2309
	.uleb128 0
	.uleb128 .LEHB23-.LFB2309
	.uleb128 .LEHE23-.LEHB23
	.uleb128 .L356-.LFB2309
	.uleb128 0
	.uleb128 .LEHB24-.LFB2309
	.uleb128 .LEHE24-.LEHB24
	.uleb128 .L357-.LFB2309
	.uleb128 0
	.uleb128 .LEHB25-.LFB2309
	.uleb128 .LEHE25-.LEHB25
	.uleb128 .L358-.LFB2309
	.uleb128 0
	.uleb128 .LEHB26-.LFB2309
	.uleb128 .LEHE26-.LEHB26
	.uleb128 .L355-.LFB2309
	.uleb128 0
	.uleb128 .LEHB27-.LFB2309
	.uleb128 .LEHE27-.LEHB27
	.uleb128 .L353-.LFB2309
	.uleb128 0
	.uleb128 .LEHB28-.LFB2309
	.uleb128 .LEHE28-.LEHB28
	.uleb128 .L352-.LFB2309
	.uleb128 0
	.uleb128 .LEHB29-.LFB2309
	.uleb128 .LEHE29-.LEHB29
	.uleb128 .L353-.LFB2309
	.uleb128 0
	.uleb128 .LEHB30-.LFB2309
	.uleb128 .LEHE30-.LEHB30
	.uleb128 .L352-.LFB2309
	.uleb128 0
	.uleb128 .LEHB31-.LFB2309
	.uleb128 .LEHE31-.LEHB31
	.uleb128 .L357-.LFB2309
	.uleb128 0
	.uleb128 .LEHB32-.LFB2309
	.uleb128 .LEHE32-.LEHB32
	.uleb128 .L352-.LFB2309
	.uleb128 0
	.uleb128 .LEHB33-.LFB2309
	.uleb128 .LEHE33-.LEHB33
	.uleb128 0
	.uleb128 0
.LLSDACSE2309:
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
	.type	_GLOBAL__sub_I_count_t, @function
_GLOBAL__sub_I_count_t:
.LFB2899:
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
.LFE2899:
	.size	_GLOBAL__sub_I_count_t, .-_GLOBAL__sub_I_count_t
	.section	.text.unlikely
.LCOLDE20:
	.section	.text.startup
.LHOTE20:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_count_t
	.local	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time
	.comm	_ZZN5Graph7BCCUtilEiPiS0_PNSt7__cxx114listI4EdgeSaIS3_EEES0_E4time,4,4
	.globl	count_t
	.bss
	.align 4
	.type	count_t, @object
	.size	count_t, 4
count_t:
	.zero	4
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
'''
s2_1 ='''.file	"2-1.cpp"
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
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"basic_string::_M_construct null not valid"
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.type	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31, @function
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31:
.LFB2197:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rsi, %r12
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdi, %rbp
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	testq	%rsi, %rsi
	jne	.L5
	testq	%rdx, %rdx
	je	.L5
	movl	$.LC1, %edi
	call	_ZSt19__throw_logic_errorPKc
	.p2align 4,,10
	.p2align 3
.L5:
	movq	%rdx, %rbx
	subq	%r12, %rbx
	cmpq	$15, %rbx
	movq	%rbx, (%rsp)
	ja	.L24
	movq	0(%rbp), %rdx
	cmpq	$1, %rbx
	movq	%rdx, %rdi
	je	.L25
	testq	%rbx, %rbx
	jne	.L6
.L8:
	movq	(%rsp), %rax
	movq	%rax, 8(%rbp)
	movb	$0, (%rdx,%rax)
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L26
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
.L24:
	.cfi_restore_state
	movq	%rbp, %rdi
	xorl	%edx, %edx
	movq	%rsp, %rsi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_createERmm
	movq	%rax, %rdi
	movq	%rax, 0(%rbp)
	movq	(%rsp), %rax
	movq	%rax, 16(%rbp)
.L6:
	movq	%rbx, %rdx
	movq	%r12, %rsi
	call	memcpy
	movq	0(%rbp), %rdx
	jmp	.L8
	.p2align 4,,10
	.p2align 3
.L25:
	movzbl	(%r12), %eax
	movb	%al, (%rdx)
	movq	0(%rbp), %rdx
	jmp	.L8
.L26:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2197:
	.size	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31, .-_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.set	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25,_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.type	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27, @function
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27:
.LFB2193:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	leaq	16(%rdi), %rax
	orq	$-1, %rdx
	movq	%rdi, %rbp
	movq	%rsi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	testq	%rsi, %rsi
	movq	%rax, (%rdi)
	je	.L28
	movq	%rsi, %rdi
	call	strlen
	leaq	(%rbx,%rax), %rdx
.L28:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	movq	%rbx, %rsi
	movq	%rbp, %rdi
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25
	.cfi_endproc
.LFE2193:
	.size	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27, .-_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.text.unlikely
.LCOLDB4:
	.text
.LHOTB4:
	.p2align 4,,15
	.globl	_Z9GetLength5PointS_
	.type	_Z9GetLength5PointS_, @function
_Z9GetLength5PointS_:
.LFB1861:
	.cfi_startproc
	movsd	8(%rdi), %xmm0
	movsd	(%rdi), %xmm2
	subsd	8(%rsi), %xmm0
	movsd	16(%rdi), %xmm1
	subsd	(%rsi), %xmm2
	subsd	16(%rsi), %xmm1
	mulsd	%xmm0, %xmm0
	mulsd	%xmm2, %xmm2
	mulsd	%xmm1, %xmm1
	addsd	%xmm0, %xmm2
	addsd	%xmm2, %xmm1
	sqrtsd	%xmm1, %xmm0
	ucomisd	%xmm0, %xmm0
	jp	.L39
	ret
	.p2align 4,,10
	.p2align 3
.L39:
	movapd	%xmm1, %xmm0
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	call	sqrt
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1861:
	.size	_Z9GetLength5PointS_, .-_Z9GetLength5PointS_
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.text.unlikely
.LCOLDB6:
	.text
.LHOTB6:
	.p2align 4,,15
	.globl	_Z17GetShortestLengthP5Point
	.type	_Z17GetShortestLengthP5Point, @function
_Z17GetShortestLengthP5Point:
.LFB1860:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	subq	$144, %rsp
	.cfi_def_cfa_offset 160
	movsd	64(%rdi), %xmm7
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	movsd	%xmm7, 24(%rsp)
	movsd	56(%rdi), %xmm7
	movsd	40(%rdi), %xmm6
	movsd	%xmm7, 40(%rsp)
	movsd	48(%rdi), %xmm7
	movsd	32(%rdi), %xmm5
	movsd	%xmm7, 32(%rsp)
	movsd	16(%rdi), %xmm7
	movsd	24(%rdi), %xmm4
	movsd	%xmm7, 16(%rsp)
	movsd	8(%rdi), %xmm7
	movsd	.LC5(%rip), %xmm3
	movsd	%xmm7, (%rsp)
	movsd	(%rdi), %xmm7
	movsd	%xmm7, 8(%rsp)
	.p2align 4,,10
	.p2align 3
.L41:
	movsd	24(%rsp), %xmm7
	leaq	112(%rsp), %rsi
	leaq	80(%rsp), %rdi
	movsd	32(%rsp), %xmm2
	movsd	%xmm3, 72(%rsp)
	movsd	40(%rsp), %xmm3
	movsd	%xmm6, 96(%rsp)
	movsd	%xmm6, 64(%rsp)
	movsd	%xmm5, 88(%rsp)
	movsd	%xmm5, 56(%rsp)
	movsd	%xmm7, 128(%rsp)
	movsd	%xmm3, 120(%rsp)
	movsd	%xmm2, 112(%rsp)
	movsd	%xmm4, 80(%rsp)
	movsd	%xmm4, 48(%rsp)
	call	_Z9GetLength5PointS_
	movsd	24(%rsp), %xmm7
	leaq	112(%rsp), %rsi
	movsd	40(%rsp), %xmm3
	leaq	80(%rsp), %rdi
	movsd	32(%rsp), %xmm2
	movsd	(%rsp), %xmm1
	movsd	8(%rsp), %xmm4
	movsd	%xmm7, 128(%rsp)
	movsd	16(%rsp), %xmm7
	cvttsd2si	%xmm0, %ebx
	movsd	%xmm3, 120(%rsp)
	movsd	%xmm2, 112(%rsp)
	movsd	%xmm1, 88(%rsp)
	movsd	%xmm4, 80(%rsp)
	movsd	%xmm7, 96(%rsp)
	call	_Z9GetLength5PointS_
	cvttsd2si	%xmm0, %eax
	movsd	16(%rsp), %xmm2
	movsd	64(%rsp), %xmm6
	movsd	(%rsp), %xmm1
	movsd	56(%rsp), %xmm5
	addsd	%xmm6, %xmm2
	movsd	8(%rsp), %xmm0
	movsd	48(%rsp), %xmm4
	addsd	%xmm5, %xmm1
	movsd	72(%rsp), %xmm3
	addsd	%xmm4, %xmm0
	mulsd	%xmm3, %xmm2
	mulsd	%xmm3, %xmm1
	cmpl	%eax, %ebx
	mulsd	%xmm3, %xmm0
	je	.L49
	jg	.L45
	movsd	%xmm2, 16(%rsp)
	movsd	%xmm1, (%rsp)
	movsd	%xmm0, 8(%rsp)
	jmp	.L41
	.p2align 4,,10
	.p2align 3
.L45:
	movapd	%xmm2, %xmm6
	movapd	%xmm1, %xmm5
	movapd	%xmm0, %xmm4
	jmp	.L41
	.p2align 4,,10
	.p2align 3
.L49:
	movsd	24(%rsp), %xmm5
	leaq	112(%rsp), %rsi
	movsd	40(%rsp), %xmm6
	leaq	80(%rsp), %rdi
	movsd	%xmm5, 128(%rsp)
	movsd	32(%rsp), %xmm5
	movsd	%xmm6, 120(%rsp)
	movsd	%xmm5, 112(%rsp)
	movsd	%xmm2, 96(%rsp)
	movsd	%xmm1, 88(%rsp)
	movsd	%xmm0, 80(%rsp)
	call	_Z9GetLength5PointS_
	call	ceil
	movq	136(%rsp), %rdx
	xorq	%fs:40, %rdx
	cvttsd2si	%xmm0, %eax
	jne	.L50
	addq	$144, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L50:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE1860:
	.size	_Z17GetShortestLengthP5Point, .-_Z17GetShortestLengthP5Point
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDB7:
	.section	.text._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTB7:
	.p2align 4,,15
	.weak	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.type	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, @function
_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_:
.LFB1870:
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
	movq	%rdi, %r13
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movq	%rdx, %rbx
	movq	%rcx, %r12
	subq	$16, %rsp
	.cfi_def_cfa_offset 64
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	__errno_location
	movq	%rsp, %rsi
	movq	%rax, %rbp
	movl	$0, (%rax)
	movq	%rbx, %rdi
	call	*%r13
	movq	(%rsp), %rdx
	cmpq	%rdx, %rbx
	je	.L60
	cmpl	$34, 0(%rbp)
	je	.L61
	testq	%r12, %r12
	je	.L54
	subq	%rbx, %rdx
	movq	%rdx, (%r12)
.L54:
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L62
	addq	$16, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 48
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
.L60:
	.cfi_restore_state
	movq	%r14, %rdi
	call	_ZSt24__throw_invalid_argumentPKc
.L62:
	call	__stack_chk_fail
.L61:
	movq	%r14, %rdi
	call	_ZSt20__throw_out_of_rangePKc
	.cfi_endproc
.LFE1870:
	.size	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, .-_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDE7:
	.section	.text._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTE7:
	.weak	_ZN9__gnu_cxx6__stoaIddcIEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.set	_ZN9__gnu_cxx6__stoaIddcIEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LCOLDB8:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LHOTB8:
	.p2align 4,,15
	.weak	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
	.type	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_, @function
_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_:
.LFB1950:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1950
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	leaq	16(%rdi), %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdx, %rbp
	movq	%rdi, %rbx
	movq	%r12, (%rdi)
	movq	(%rsi), %rax
	movq	%rax, %rdx
	addq	8(%rsi), %rdx
	movq	%rax, %rsi
.LEHB0:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
.LEHE0:
	movq	8(%rbp), %rdx
	movq	0(%rbp), %rsi
	movq	%rbx, %rdi
.LEHB1:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_appendEPKcm
.LEHE1:
	movq	%rbx, %rax
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L66:
	.cfi_restore_state
	movq	%rax, %rbp
.L64:
	movq	(%rbx), %rdi
	cmpq	%r12, %rdi
	je	.L65
	call	_ZdlPv
.L65:
	movq	%rbp, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
	.cfi_endproc
.LFE1950:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"aG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LLSDA1950:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1950-.LLSDACSB1950
.LLSDACSB1950:
	.uleb128 .LEHB0-.LFB1950
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1950
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L66-.LFB1950
	.uleb128 0
	.uleb128 .LEHB2-.LFB1950
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE1950:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
	.size	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_, .-_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
	.section	.text.unlikely._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LCOLDE8:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LHOTE8:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC9:
	.string	"stod"
	.section	.text.unlikely
.LCOLDB10:
	.text
.LHOTB10:
	.p2align 4,,15
	.globl	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
	.type	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_, @function
_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_:
.LFB1859:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1859
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rsi, %rdx
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdi, %rsi
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$1096, %rsp
	.cfi_def_cfa_offset 1152
	leaq	160(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1080(%rsp)
	xorl	%eax, %eax
.LEHB3:
	call	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
.LEHE3:
	leaq	816(%rsp), %rdi
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movb	$0, 1040(%rsp)
	leaq	560(%rsp), %rdi
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	xorl	%esi, %esi
	movq	$0, 1032(%rsp)
	movb	$0, 1041(%rsp)
	movq	%rax, 560(%rsp)
	movq	-24(%rax), %rax
	movq	$0, 1048(%rsp)
	movq	$0, 1056(%rsp)
	movq	$0, 1064(%rsp)
	movq	$0, 1072(%rsp)
	movq	%rbx, 560(%rsp,%rax)
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movq	$0, 568(%rsp)
	addq	-24(%rax), %rdi
.LEHB4:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE4:
	leaq	560(%rsp), %rax
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 560(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 816(%rsp)
	leaq	16(%rax), %rdi
.LEHB5:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE5:
	leaq	560(%rsp), %rax
	leaq	576(%rsp), %rsi
	leaq	256(%rax), %rdi
.LEHB6:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	560(%rsp), %rax
	movq	160(%rsp), %rsi
	movl	$8, %edx
	leaq	16(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	560(%rsp), %rdi
	movq	560(%rsp), %rax
	je	.L145
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE6:
.L72:
	movq	160(%rsp), %rdi
	leaq	176(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L78
	call	_ZdlPv
.L78:
	leaq	48(%rsp), %rax
	leaq	680(%rsp), %rdi
	movq	$0, 40(%rsp)
	movb	$0, 48(%rsp)
	movq	%rax, 32(%rsp)
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	je	.L115
	movl	$72, %edi
.LEHB7:
	call	_Znam
	movq	%rax, 24(%rsp)
	movq	560(%rsp), %rax
	movq	-24(%rax), %rax
	movq	800(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	je	.L101
	movq	24(%rsp), %rax
	leaq	80(%rsp), %r14
	leaq	112(%rsp), %r15
	leaq	8(%rax), %rbx
	jmp	.L102
	.p2align 4,,10
	.p2align 3
.L96:
	movq	256(%rsp), %rdi
	leaq	272(%rsp), %rax
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 160(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 288(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 176(%rsp)
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	cmpq	%rax, %rdi
	je	.L113
	call	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L113:
	leaq	240(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r13), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	leaq	288(%rsp), %rdi
	movq	%rcx, 160(%rsp,%rax)
	movq	-24(%r12), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 176(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	128(%rsp), %rdi
	leaq	144(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L98
	call	_ZdlPv
.L98:
	movq	96(%rsp), %rdi
	cmpq	%r15, %rdi
	je	.L99
	call	_ZdlPv
.L99:
	movq	64(%rsp), %rdi
	cmpq	%r14, %rdi
	je	.L100
	call	_ZdlPv
.L100:
	movq	560(%rsp), %rax
	addq	$24, %rbx
	movq	-24(%rax), %rax
	movq	800(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	je	.L101
.L102:
	cmpb	$0, 56(%rbp)
	je	.L81
	movsbl	67(%rbp), %edx
.L82:
	leaq	32(%rsp), %rsi
	leaq	560(%rsp), %rdi
	call	_ZSt7getlineIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EES4_
.LEHE7:
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L83
	leaq	144(%rsp), %rax
	leaq	288(%rsp), %rdi
	movq	%r14, 64(%rsp)
	movq	$0, 72(%rsp)
	movb	$0, 80(%rsp)
	movq	%rax, 128(%rsp)
	movq	%r15, 96(%rsp)
	movq	$0, 104(%rsp)
	movb	$0, 112(%rsp)
	movq	$0, 136(%rsp)
	movb	$0, 144(%rsp)
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+16(%rip), %rbp
	movb	$0, 512(%rsp)
	leaq	160(%rsp), %rdi
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	xorl	%esi, %esi
	movq	$0, 504(%rsp)
	movb	$0, 513(%rsp)
	movq	-24(%rbp), %rax
	movq	$0, 520(%rsp)
	movq	$0, 528(%rsp)
	movq	$0, 536(%rsp)
	movq	$0, 544(%rsp)
	movq	%rbp, 160(%rsp)
	movq	%rcx, 160(%rsp,%rax)
	movq	$0, 168(%rsp)
	addq	-24(%rbp), %rdi
.LEHB8:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE8:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+32(%rip), %r12
	xorl	%esi, %esi
	movq	-24(%r12), %rax
	movq	%r12, 176(%rsp)
	leaq	176(%rsp,%rax), %rdi
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rax
	movq	%rax, (%rdi)
.LEHB9:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE9:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+8(%rip), %r13
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	leaq	240(%rsp), %rdi
	movq	-24(%r13), %rax
	movq	%rcx, 160(%rsp,%rax)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 160(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 288(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 176(%rsp)
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	movq	$0, 192(%rsp)
	movq	$0, 200(%rsp)
	movq	$0, 208(%rsp)
	movq	$0, 216(%rsp)
	movq	$0, 224(%rsp)
	movq	$0, 232(%rsp)
	call	_ZNSt6localeC1Ev
	movq	32(%rsp), %rsi
	leaq	272(%rsp), %rax
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	movl	$0, 248(%rsp)
	movq	%rax, 256(%rsp)
	leaq	160(%rsp), %rax
	movq	%rsi, %rdx
	addq	40(%rsp), %rdx
	leaq	96(%rax), %rdi
.LEHB10:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25
.LEHE10:
	leaq	160(%rsp), %rax
	movq	256(%rsp), %rsi
	xorl	%ecx, %ecx
	xorl	%edx, %edx
	movl	$24, 248(%rsp)
	leaq	24(%rax), %rdi
.LEHB11:
	call	_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEE7_M_syncEPcmm
.LEHE11:
	leaq	160(%rsp), %rax
	leaq	184(%rsp), %rsi
	leaq	128(%rax), %rdi
.LEHB12:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE12:
	.p2align 4,,10
	.p2align 3
.L92:
	leaq	64(%rsp), %rsi
	leaq	160(%rsp), %rdi
.LEHB13:
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	leaq	96(%rsp), %rsi
	leaq	160(%rsp), %rdi
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	leaq	128(%rsp), %rsi
	leaq	160(%rsp), %rdi
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	movq	128(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	movq	96(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	movsd	%xmm0, 8(%rsp)
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	movq	64(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	movsd	%xmm0, 16(%rsp)
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
.LEHE13:
	movsd	16(%rsp), %xmm1
	movsd	8(%rsp), %xmm2
	movsd	%xmm1, (%rbx)
	movsd	%xmm2, 8(%rbx)
	movsd	%xmm0, -8(%rbx)
	jmp	.L92
.L81:
	movq	%rbp, %rdi
.LEHB14:
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %edx
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L82
	movl	$10, %esi
	movq	%rbp, %rdi
	call	*%rax
	movsbl	%al, %edx
	jmp	.L82
.L83:
	leaq	560(%rsp), %rax
	leaq	16(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE14:
	testq	%rax, %rax
	je	.L146
.L136:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L79
	call	_ZdlPv
.L79:
	leaq	576(%rsp), %rdi
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 560(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 816(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 576(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	680(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	632(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 576(%rsp)
	call	_ZNSt6localeD1Ev
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	leaq	816(%rsp), %rdi
	movq	-24(%rax), %rax
	movq	%rbx, 560(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	1080(%rsp), %rbx
	xorq	%fs:40, %rbx
	movq	24(%rsp), %rax
	jne	.L147
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
.L145:
	.cfi_restore_state
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB15:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE15:
	jmp	.L72
.L115:
	movq	$0, 24(%rsp)
	jmp	.L79
.L117:
	movq	%rax, %rbx
.L109:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L110
	call	_ZdlPv
.L110:
	leaq	560(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
.L137:
	movq	%rbx, %rdi
.LEHB16:
	call	_Unwind_Resume
.LEHE16:
.L124:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rbx
	movq	-24(%rbp), %rdx
	movq	%rbx, 160(%rsp,%rdx)
	movq	%rax, %rbx
.L86:
	leaq	288(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	call	_ZNSt8ios_baseD2Ev
.L95:
	movq	128(%rsp), %rdi
	leaq	144(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L106
	call	_ZdlPv
.L106:
	movq	96(%rsp), %rdi
	leaq	112(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L107
	call	_ZdlPv
.L107:
	movq	64(%rsp), %rdi
	leaq	80(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L109
	call	_ZdlPv
	jmp	.L109
.L125:
	movq	%rax, %rbx
.L94:
	leaq	240(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r13), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	movq	-24(%r12), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 176(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	jmp	.L86
.L126:
	movq	%rax, %rbx
.L140:
	movq	256(%rsp), %rdi
	leaq	272(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L94
	call	_ZdlPv
	jmp	.L94
.L123:
	movq	%rax, %rbx
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	jmp	.L140
.L101:
.LEHB17:
	call	_ZSt16__throw_bad_castv
.L122:
	movq	%rax, %rbx
	jmp	.L86
.L120:
.L74:
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rbx
	movq	-24(%rbx), %rdx
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	movq	%rbx, 560(%rsp,%rdx)
	movq	%rax, %rbx
.L75:
	leaq	816(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	160(%rsp), %rdi
	leaq	176(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L137
	call	_ZdlPv
	jmp	.L137
.L121:
	leaq	576(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rax
	jmp	.L74
.L118:
	leaq	160(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEED1Ev
	jmp	.L95
.L146:
	movq	560(%rsp), %rax
	leaq	560(%rsp), %rdi
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE17:
	jmp	.L136
.L147:
	call	__stack_chk_fail
.L119:
	movq	%rax, %rbx
	jmp	.L75
	.cfi_endproc
.LFE1859:
	.section	.gcc_except_table,"a",@progbits
.LLSDA1859:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1859-.LLSDACSB1859
.LLSDACSB1859:
	.uleb128 .LEHB3-.LFB1859
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB4-.LFB1859
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L119-.LFB1859
	.uleb128 0
	.uleb128 .LEHB5-.LFB1859
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L120-.LFB1859
	.uleb128 0
	.uleb128 .LEHB6-.LFB1859
	.uleb128 .LEHE6-.LEHB6
	.uleb128 .L121-.LFB1859
	.uleb128 0
	.uleb128 .LEHB7-.LFB1859
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L117-.LFB1859
	.uleb128 0
	.uleb128 .LEHB8-.LFB1859
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L122-.LFB1859
	.uleb128 0
	.uleb128 .LEHB9-.LFB1859
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L124-.LFB1859
	.uleb128 0
	.uleb128 .LEHB10-.LFB1859
	.uleb128 .LEHE10-.LEHB10
	.uleb128 .L125-.LFB1859
	.uleb128 0
	.uleb128 .LEHB11-.LFB1859
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L126-.LFB1859
	.uleb128 0
	.uleb128 .LEHB12-.LFB1859
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L123-.LFB1859
	.uleb128 0
	.uleb128 .LEHB13-.LFB1859
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L118-.LFB1859
	.uleb128 0
	.uleb128 .LEHB14-.LFB1859
	.uleb128 .LEHE14-.LEHB14
	.uleb128 .L117-.LFB1859
	.uleb128 0
	.uleb128 .LEHB15-.LFB1859
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L121-.LFB1859
	.uleb128 0
	.uleb128 .LEHB16-.LFB1859
	.uleb128 .LEHE16-.LEHB16
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB17-.LFB1859
	.uleb128 .LEHE17-.LEHB17
	.uleb128 .L117-.LFB1859
	.uleb128 0
.LLSDACSE1859:
	.text
	.size	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_, .-_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.section	.text.unlikely
.LCOLDB11:
	.text
.LHOTB11:
	.p2align 4,,15
	.globl	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
	.type	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i, @function
_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i:
.LFB1862:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1862
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	%edx, %r12d
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rsi, %rdx
	movq	%rdi, %rsi
	subq	$560, %rsp
	.cfi_def_cfa_offset 592
	movq	%rsp, %rdi
	movq	%fs:40, %rax
	movq	%rax, 552(%rsp)
	xorl	%eax, %eax
.LEHB18:
	call	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
.LEHE18:
	leaq	280(%rsp), %rdi
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+8(%rip), %rbx
	movb	$0, 504(%rsp)
	leaq	32(%rsp), %rdi
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+16(%rip), %rbp
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	xorl	%esi, %esi
	movq	$0, 496(%rsp)
	movb	$0, 505(%rsp)
	addq	-24(%rbx), %rdi
	movq	$0, 512(%rsp)
	movq	$0, 520(%rsp)
	movq	$0, 528(%rsp)
	movq	$0, 536(%rsp)
	movq	%rbx, 32(%rsp)
	movq	%rbp, (%rdi)
.LEHB19:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE19:
	leaq	32(%rsp), %rax
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 32(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 280(%rsp)
	leaq	8(%rax), %rdi
.LEHB20:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE20:
	leaq	32(%rsp), %rax
	leaq	40(%rsp), %rsi
	leaq	248(%rax), %rdi
.LEHB21:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	32(%rsp), %rax
	movq	(%rsp), %rsi
	movl	$48, %edx
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	32(%rsp), %rdi
	movq	32(%rsp), %rax
	je	.L169
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE21:
.L150:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L156
	call	_ZdlPv
.L156:
	leaq	32(%rsp), %rdi
	movl	%r12d, %esi
.LEHB22:
	call	_ZNSolsEi
	leaq	32(%rsp), %rax
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE22:
	testq	%rax, %rax
	je	.L157
.L158:
	leaq	40(%rsp), %rdi
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 32(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 280(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 40(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	144(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	96(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 40(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%rbx), %rax
	leaq	280(%rsp), %rdi
	movq	%rbp, 32(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	552(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L170
	addq	$560, %rsp
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
.L169:
	.cfi_restore_state
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB23:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE23:
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L157:
	movq	32(%rsp), %rax
	leaq	32(%rsp), %rdi
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB24:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE24:
	jmp	.L158
.L170:
	call	__stack_chk_fail
.L161:
	leaq	32(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L167:
	movq	%rbx, %rdi
.LEHB25:
	call	_Unwind_Resume
.LEHE25:
.L162:
	movq	%rax, %rbx
.L153:
	leaq	280(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L167
	call	_ZdlPv
	jmp	.L167
.L164:
	leaq	40(%rsp), %rdi
	movq	%rax, %r12
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%r12, %rax
.L152:
	movq	-24(%rbx), %rdx
	movq	%rax, %rbx
	movq	%rbp, 32(%rsp,%rdx)
	jmp	.L153
.L163:
	jmp	.L152
	.cfi_endproc
.LFE1862:
	.section	.gcc_except_table
.LLSDA1862:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1862-.LLSDACSB1862
.LLSDACSB1862:
	.uleb128 .LEHB18-.LFB1862
	.uleb128 .LEHE18-.LEHB18
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB19-.LFB1862
	.uleb128 .LEHE19-.LEHB19
	.uleb128 .L162-.LFB1862
	.uleb128 0
	.uleb128 .LEHB20-.LFB1862
	.uleb128 .LEHE20-.LEHB20
	.uleb128 .L163-.LFB1862
	.uleb128 0
	.uleb128 .LEHB21-.LFB1862
	.uleb128 .LEHE21-.LEHB21
	.uleb128 .L164-.LFB1862
	.uleb128 0
	.uleb128 .LEHB22-.LFB1862
	.uleb128 .LEHE22-.LEHB22
	.uleb128 .L161-.LFB1862
	.uleb128 0
	.uleb128 .LEHB23-.LFB1862
	.uleb128 .LEHE23-.LEHB23
	.uleb128 .L164-.LFB1862
	.uleb128 0
	.uleb128 .LEHB24-.LFB1862
	.uleb128 .LEHE24-.LEHB24
	.uleb128 .L161-.LFB1862
	.uleb128 0
	.uleb128 .LEHB25-.LFB1862
	.uleb128 .LEHE25-.LEHB25
	.uleb128 0
	.uleb128 0
.LLSDACSE1862:
	.text
	.size	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i, .-_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
	.section	.text.unlikely
.LCOLDE11:
	.text
.LHOTE11:
	.section	.rodata.str1.1
.LC12:
	.string	"connect.inp"
.LC13:
	.string	"./"
.LC14:
	.string	"connect.out"
	.section	.text.unlikely
.LCOLDB15:
	.section	.text.startup,"ax",@progbits
.LHOTB15:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1858:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1858
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$.LC12, %esi
	subq	$80, %rsp
	.cfi_def_cfa_offset 96
	leaq	32(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 72(%rsp)
	xorl	%eax, %eax
.LEHB26:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE26:
	movl	$.LC13, %esi
	movq	%rsp, %rdi
.LEHB27:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE27:
	leaq	32(%rsp), %rsi
	movq	%rsp, %rdi
.LEHB28:
	call	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
.LEHE28:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L172
	call	_ZdlPv
.L172:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L173
	call	_ZdlPv
.L173:
	movq	%rbx, %rdi
	call	_Z17GetShortestLengthP5Point
	leaq	32(%rsp), %rdi
	movl	$.LC14, %esi
	movl	%eax, %ebx
.LEHB29:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE29:
	movl	$.LC13, %esi
	movq	%rsp, %rdi
.LEHB30:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE30:
	leaq	32(%rsp), %rsi
	movl	%ebx, %edx
	movq	%rsp, %rdi
.LEHB31:
	call	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
.LEHE31:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L174
	call	_ZdlPv
.L174:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L175
	call	_ZdlPv
.L175:
	xorl	%eax, %eax
	movq	72(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L193
	addq	$80, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L193:
	.cfi_restore_state
	call	__stack_chk_fail
.L188:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rdx
	movq	%rax, %rbx
	cmpq	%rdx, %rdi
	je	.L182
	call	_ZdlPv
.L182:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rdx
	cmpq	%rdx, %rdi
	je	.L183
.L191:
	call	_ZdlPv
.L183:
	movq	%rbx, %rdi
.LEHB32:
	call	_Unwind_Resume
.LEHE32:
.L187:
	movq	%rax, %rbx
	jmp	.L182
.L186:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L178
	call	_ZdlPv
.L178:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	jne	.L191
	jmp	.L183
.L185:
	movq	%rax, %rbx
	jmp	.L178
	.cfi_endproc
.LFE1858:
	.section	.gcc_except_table
.LLSDA1858:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1858-.LLSDACSB1858
.LLSDACSB1858:
	.uleb128 .LEHB26-.LFB1858
	.uleb128 .LEHE26-.LEHB26
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB27-.LFB1858
	.uleb128 .LEHE27-.LEHB27
	.uleb128 .L185-.LFB1858
	.uleb128 0
	.uleb128 .LEHB28-.LFB1858
	.uleb128 .LEHE28-.LEHB28
	.uleb128 .L186-.LFB1858
	.uleb128 0
	.uleb128 .LEHB29-.LFB1858
	.uleb128 .LEHE29-.LEHB29
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB30-.LFB1858
	.uleb128 .LEHE30-.LEHB30
	.uleb128 .L187-.LFB1858
	.uleb128 0
	.uleb128 .LEHB31-.LFB1858
	.uleb128 .LEHE31-.LEHB31
	.uleb128 .L188-.LFB1858
	.uleb128 0
	.uleb128 .LEHB32-.LFB1858
	.uleb128 .LEHE32-.LEHB32
	.uleb128 0
	.uleb128 0
.LLSDACSE1858:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE15:
	.section	.text.startup
.LHOTE15:
	.section	.text.unlikely
.LCOLDB16:
	.section	.text.startup
.LHOTB16:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB2165:
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
.LFE2165:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.text.unlikely
.LCOLDE16:
	.section	.text.startup
.LHOTE16:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_main
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC5:
	.long	0
	.long	1071644672
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
'''
s3 = '''.file	"3.c"
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
'''
s2 = '''.file	"2.cpp"
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
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"basic_string::_M_construct null not valid"
	.section	.text.unlikely,"ax",@progbits
	.align 2
.LCOLDB2:
	.text
.LHOTB2:
	.align 2
	.p2align 4,,15
	.type	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31, @function
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31:
.LFB2197:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movq	%rsi, %r12
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdi, %rbp
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	testq	%rsi, %rsi
	jne	.L5
	testq	%rdx, %rdx
	je	.L5
	movl	$.LC1, %edi
	call	_ZSt19__throw_logic_errorPKc
	.p2align 4,,10
	.p2align 3
.L5:
	movq	%rdx, %rbx
	subq	%r12, %rbx
	cmpq	$15, %rbx
	movq	%rbx, (%rsp)
	ja	.L24
	movq	0(%rbp), %rdx
	cmpq	$1, %rbx
	movq	%rdx, %rdi
	je	.L25
	testq	%rbx, %rbx
	jne	.L6
.L8:
	movq	(%rsp), %rax
	movq	%rax, 8(%rbp)
	movb	$0, (%rdx,%rax)
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L26
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
.L24:
	.cfi_restore_state
	movq	%rbp, %rdi
	xorl	%edx, %edx
	movq	%rsp, %rsi
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_createERmm
	movq	%rax, %rdi
	movq	%rax, 0(%rbp)
	movq	(%rsp), %rax
	movq	%rax, 16(%rbp)
.L6:
	movq	%rbx, %rdx
	movq	%r12, %rsi
	call	memcpy
	movq	0(%rbp), %rdx
	jmp	.L8
	.p2align 4,,10
	.p2align 3
.L25:
	movzbl	(%r12), %eax
	movb	%al, (%rdx)
	movq	0(%rbp), %rdx
	jmp	.L8
.L26:
	call	__stack_chk_fail
	.cfi_endproc
.LFE2197:
	.size	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31, .-_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
	.section	.text.unlikely
.LCOLDE2:
	.text
.LHOTE2:
	.set	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25,_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
	.section	.text.unlikely
	.align 2
.LCOLDB3:
	.text
.LHOTB3:
	.align 2
	.p2align 4,,15
	.type	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27, @function
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27:
.LFB2193:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	leaq	16(%rdi), %rax
	orq	$-1, %rdx
	movq	%rdi, %rbp
	movq	%rsi, %rbx
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	testq	%rsi, %rsi
	movq	%rax, (%rdi)
	je	.L28
	movq	%rsi, %rdi
	call	strlen
	leaq	(%rbx,%rax), %rdx
.L28:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	movq	%rbx, %rsi
	movq	%rbp, %rdi
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	jmp	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25
	.cfi_endproc
.LFE2193:
	.size	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27, .-_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
	.section	.text.unlikely
.LCOLDE3:
	.text
.LHOTE3:
	.section	.text.unlikely
.LCOLDB4:
	.text
.LHOTB4:
	.p2align 4,,15
	.globl	_Z9GetLength5PointS_
	.type	_Z9GetLength5PointS_, @function
_Z9GetLength5PointS_:
.LFB1861:
	.cfi_startproc
	movsd	(%rdi), %xmm0
	movsd	8(%rdi), %xmm2
	subsd	(%rsi), %xmm0
	movsd	16(%rdi), %xmm1
	subsd	8(%rsi), %xmm2
	subsd	16(%rsi), %xmm1
	mulsd	%xmm0, %xmm0
	mulsd	%xmm2, %xmm2
	mulsd	%xmm1, %xmm1
	addsd	%xmm0, %xmm2
	addsd	%xmm2, %xmm1
	sqrtsd	%xmm1, %xmm0
	ucomisd	%xmm0, %xmm0
	jp	.L39
	ret
	.p2align 4,,10
	.p2align 3
.L39:
	movapd	%xmm1, %xmm0
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	call	sqrt
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1861:
	.size	_Z9GetLength5PointS_, .-_Z9GetLength5PointS_
	.section	.text.unlikely
.LCOLDE4:
	.text
.LHOTE4:
	.section	.text.unlikely
.LCOLDB6:
	.text
.LHOTB6:
	.p2align 4,,15
	.globl	_Z17GetShortestLengthP5Point
	.type	_Z17GetShortestLengthP5Point, @function
_Z17GetShortestLengthP5Point:
.LFB1860:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	subq	$144, %rsp
	.cfi_def_cfa_offset 160
	movsd	24(%rdi), %xmm7
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	movsd	%xmm7, 8(%rsp)
	movsd	32(%rdi), %xmm7
	movsd	(%rdi), %xmm6
	movsd	%xmm7, (%rsp)
	movsd	40(%rdi), %xmm7
	movsd	8(%rdi), %xmm5
	movsd	%xmm7, 16(%rsp)
	movsd	48(%rdi), %xmm7
	movsd	16(%rdi), %xmm4
	movsd	%xmm7, 40(%rsp)
	movsd	56(%rdi), %xmm7
	movsd	.LC5(%rip), %xmm3
	movsd	%xmm7, 32(%rsp)
	movsd	64(%rdi), %xmm7
	movsd	%xmm7, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L41:
	movsd	40(%rsp), %xmm7
	leaq	112(%rsp), %rsi
	leaq	80(%rsp), %rdi
	movsd	24(%rsp), %xmm2
	movsd	%xmm3, 72(%rsp)
	movsd	32(%rsp), %xmm3
	movsd	%xmm6, 80(%rsp)
	movsd	%xmm6, 64(%rsp)
	movsd	%xmm5, 88(%rsp)
	movsd	%xmm5, 56(%rsp)
	movsd	%xmm7, 112(%rsp)
	movsd	%xmm3, 120(%rsp)
	movsd	%xmm2, 128(%rsp)
	movsd	%xmm4, 96(%rsp)
	movsd	%xmm4, 48(%rsp)
	call	_Z9GetLength5PointS_
	movsd	40(%rsp), %xmm7
	leaq	112(%rsp), %rsi
	movsd	32(%rsp), %xmm3
	leaq	80(%rsp), %rdi
	movsd	24(%rsp), %xmm2
	movsd	(%rsp), %xmm1
	movsd	16(%rsp), %xmm4
	movsd	%xmm7, 112(%rsp)
	movsd	8(%rsp), %xmm7
	cvttsd2si	%xmm0, %ebx
	movsd	%xmm3, 120(%rsp)
	movsd	%xmm2, 128(%rsp)
	movsd	%xmm1, 88(%rsp)
	movsd	%xmm4, 96(%rsp)
	movsd	%xmm7, 80(%rsp)
	call	_Z9GetLength5PointS_
	cvttsd2si	%xmm0, %eax
	movsd	48(%rsp), %xmm4
	movsd	16(%rsp), %xmm0
	movsd	(%rsp), %xmm1
	movsd	56(%rsp), %xmm5
	addsd	%xmm4, %xmm0
	movsd	8(%rsp), %xmm2
	movsd	64(%rsp), %xmm6
	addsd	%xmm5, %xmm1
	movsd	72(%rsp), %xmm3
	addsd	%xmm6, %xmm2
	mulsd	%xmm3, %xmm0
	mulsd	%xmm3, %xmm1
	cmpl	%eax, %ebx
	mulsd	%xmm3, %xmm2
	je	.L49
	jl	.L45
	movapd	%xmm0, %xmm4
	movapd	%xmm1, %xmm5
	movapd	%xmm2, %xmm6
	jmp	.L41
	.p2align 4,,10
	.p2align 3
.L45:
	movsd	%xmm0, 16(%rsp)
	movsd	%xmm1, (%rsp)
	movsd	%xmm2, 8(%rsp)
	jmp	.L41
	.p2align 4,,10
	.p2align 3
.L49:
	movsd	40(%rsp), %xmm5
	leaq	112(%rsp), %rsi
	movsd	32(%rsp), %xmm6
	leaq	80(%rsp), %rdi
	movsd	%xmm5, 112(%rsp)
	movsd	24(%rsp), %xmm5
	movsd	%xmm6, 120(%rsp)
	movsd	%xmm5, 128(%rsp)
	movsd	%xmm2, 80(%rsp)
	movsd	%xmm1, 88(%rsp)
	movsd	%xmm0, 96(%rsp)
	call	_Z9GetLength5PointS_
	call	ceil
	movq	136(%rsp), %rdx
	xorq	%fs:40, %rdx
	cvttsd2si	%xmm0, %eax
	jne	.L50
	addq	$144, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L50:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE1860:
	.size	_Z17GetShortestLengthP5Point, .-_Z17GetShortestLengthP5Point
	.section	.text.unlikely
.LCOLDE6:
	.text
.LHOTE6:
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDB7:
	.section	.text._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTB7:
	.p2align 4,,15
	.weak	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.type	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, @function
_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_:
.LFB1870:
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
	movq	%rdi, %r13
	pushq	%rbx
	.cfi_def_cfa_offset 48
	.cfi_offset 3, -48
	movq	%rdx, %rbx
	movq	%rcx, %r12
	subq	$16, %rsp
	.cfi_def_cfa_offset 64
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	call	__errno_location
	movq	%rsp, %rsi
	movq	%rax, %rbp
	movl	$0, (%rax)
	movq	%rbx, %rdi
	call	*%r13
	movq	(%rsp), %rdx
	cmpq	%rdx, %rbx
	je	.L60
	cmpl	$34, 0(%rbp)
	je	.L61
	testq	%r12, %r12
	je	.L54
	subq	%rbx, %rdx
	movq	%rdx, (%r12)
.L54:
	movq	8(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L62
	addq	$16, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 48
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
.L60:
	.cfi_restore_state
	movq	%r14, %rdi
	call	_ZSt24__throw_invalid_argumentPKc
.L62:
	call	__stack_chk_fail
.L61:
	movq	%r14, %rdi
	call	_ZSt20__throw_out_of_rangePKc
	.cfi_endproc
.LFE1870:
	.size	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_, .-_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LCOLDE7:
	.section	.text._ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,"axG",@progbits,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,comdat
.LHOTE7:
	.weak	_ZN9__gnu_cxx6__stoaIddcIEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.set	_ZN9__gnu_cxx6__stoaIddcIEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_,_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	.section	.text.unlikely._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LCOLDB8:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LHOTB8:
	.p2align 4,,15
	.weak	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
	.type	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_, @function
_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_:
.LFB1950:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1950
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	leaq	16(%rdi), %r12
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rdx, %rbp
	movq	%rdi, %rbx
	movq	%r12, (%rdi)
	movq	(%rsi), %rax
	movq	%rax, %rdx
	addq	8(%rsi), %rdx
	movq	%rax, %rsi
.LEHB0:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPcEEvT_S7_St20forward_iterator_tag.isra.31
.LEHE0:
	movq	8(%rbp), %rdx
	movq	0(%rbp), %rsi
	movq	%rbx, %rdi
.LEHB1:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_appendEPKcm
.LEHE1:
	movq	%rbx, %rax
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L66:
	.cfi_restore_state
	movq	%rax, %rbp
.L64:
	movq	(%rbx), %rdi
	cmpq	%r12, %rdi
	je	.L65
	call	_ZdlPv
.L65:
	movq	%rbp, %rdi
.LEHB2:
	call	_Unwind_Resume
.LEHE2:
	.cfi_endproc
.LFE1950:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"aG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LLSDA1950:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1950-.LLSDACSB1950
.LLSDACSB1950:
	.uleb128 .LEHB0-.LFB1950
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1950
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L66-.LFB1950
	.uleb128 0
	.uleb128 .LEHB2-.LFB1950
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE1950:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
	.size	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_, .-_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
	.section	.text.unlikely._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LCOLDE8:
	.section	.text._ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,"axG",@progbits,_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_,comdat
.LHOTE8:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC9:
	.string	"stod"
	.section	.text.unlikely
.LCOLDB10:
	.text
.LHOTB10:
	.p2align 4,,15
	.globl	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
	.type	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_, @function
_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_:
.LFB1859:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1859
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	movq	%rsi, %rdx
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	movq	%rdi, %rsi
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$1096, %rsp
	.cfi_def_cfa_offset 1152
	leaq	160(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 1080(%rsp)
	xorl	%eax, %eax
.LEHB3:
	call	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
.LEHE3:
	leaq	816(%rsp), %rdi
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movb	$0, 1040(%rsp)
	leaq	560(%rsp), %rdi
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	xorl	%esi, %esi
	movq	$0, 1032(%rsp)
	movb	$0, 1041(%rsp)
	movq	%rax, 560(%rsp)
	movq	-24(%rax), %rax
	movq	$0, 1048(%rsp)
	movq	$0, 1056(%rsp)
	movq	$0, 1064(%rsp)
	movq	$0, 1072(%rsp)
	movq	%rbx, 560(%rsp,%rax)
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movq	$0, 568(%rsp)
	addq	-24(%rax), %rdi
.LEHB4:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE4:
	leaq	560(%rsp), %rax
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 560(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 816(%rsp)
	leaq	16(%rax), %rdi
.LEHB5:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE5:
	leaq	560(%rsp), %rax
	leaq	576(%rsp), %rsi
	leaq	256(%rax), %rdi
.LEHB6:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	560(%rsp), %rax
	movq	160(%rsp), %rsi
	movl	$8, %edx
	leaq	16(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	560(%rsp), %rdi
	movq	560(%rsp), %rax
	je	.L145
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE6:
.L72:
	movq	160(%rsp), %rdi
	leaq	176(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L78
	call	_ZdlPv
.L78:
	leaq	48(%rsp), %rax
	leaq	680(%rsp), %rdi
	movq	$0, 40(%rsp)
	movb	$0, 48(%rsp)
	movq	%rax, 32(%rsp)
	call	_ZNKSt12__basic_fileIcE7is_openEv
	testb	%al, %al
	je	.L115
	movl	$72, %edi
.LEHB7:
	call	_Znam
	movq	%rax, 24(%rsp)
	movq	560(%rsp), %rax
	movq	-24(%rax), %rax
	movq	800(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	je	.L101
	movq	24(%rsp), %rbx
	leaq	80(%rsp), %r14
	leaq	112(%rsp), %r15
	jmp	.L102
	.p2align 4,,10
	.p2align 3
.L96:
	movq	256(%rsp), %rdi
	leaq	272(%rsp), %rax
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 160(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 288(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 176(%rsp)
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	cmpq	%rax, %rdi
	je	.L113
	call	_ZdlPv
	.p2align 4,,10
	.p2align 3
.L113:
	leaq	240(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r13), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	leaq	288(%rsp), %rdi
	movq	%rcx, 160(%rsp,%rax)
	movq	-24(%r12), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 176(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	128(%rsp), %rdi
	leaq	144(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L98
	call	_ZdlPv
.L98:
	movq	96(%rsp), %rdi
	cmpq	%r15, %rdi
	je	.L99
	call	_ZdlPv
.L99:
	movq	64(%rsp), %rdi
	cmpq	%r14, %rdi
	je	.L100
	call	_ZdlPv
.L100:
	movq	560(%rsp), %rax
	addq	$24, %rbx
	movq	-24(%rax), %rax
	movq	800(%rsp,%rax), %rbp
	testq	%rbp, %rbp
	je	.L101
.L102:
	cmpb	$0, 56(%rbp)
	je	.L81
	movsbl	67(%rbp), %edx
.L82:
	leaq	32(%rsp), %rsi
	leaq	560(%rsp), %rdi
	call	_ZSt7getlineIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EES4_
.LEHE7:
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L83
	leaq	144(%rsp), %rax
	leaq	288(%rsp), %rdi
	movq	%r14, 64(%rsp)
	movq	$0, 72(%rsp)
	movb	$0, 80(%rsp)
	movq	%rax, 128(%rsp)
	movq	%r15, 96(%rsp)
	movq	$0, 104(%rsp)
	movb	$0, 112(%rsp)
	movq	$0, 136(%rsp)
	movb	$0, 144(%rsp)
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+16(%rip), %rbp
	movb	$0, 512(%rsp)
	leaq	160(%rsp), %rdi
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	xorl	%esi, %esi
	movq	$0, 504(%rsp)
	movb	$0, 513(%rsp)
	movq	-24(%rbp), %rax
	movq	$0, 520(%rsp)
	movq	$0, 528(%rsp)
	movq	$0, 536(%rsp)
	movq	$0, 544(%rsp)
	movq	%rbp, 160(%rsp)
	movq	%rcx, 160(%rsp,%rax)
	movq	$0, 168(%rsp)
	addq	-24(%rbp), %rdi
.LEHB8:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE8:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+32(%rip), %r12
	xorl	%esi, %esi
	movq	-24(%r12), %rax
	movq	%r12, 176(%rsp)
	leaq	176(%rsp,%rax), %rdi
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rax
	movq	%rax, (%rdi)
.LEHB9:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE9:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+8(%rip), %r13
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	leaq	240(%rsp), %rdi
	movq	-24(%r13), %rax
	movq	%rcx, 160(%rsp,%rax)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24, 160(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+104, 288(%rsp)
	movq	$_ZTVNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+64, 176(%rsp)
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	movq	$0, 192(%rsp)
	movq	$0, 200(%rsp)
	movq	$0, 208(%rsp)
	movq	$0, 216(%rsp)
	movq	$0, 224(%rsp)
	movq	$0, 232(%rsp)
	call	_ZNSt6localeC1Ev
	movq	32(%rsp), %rsi
	leaq	272(%rsp), %rax
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	movl	$0, 248(%rsp)
	movq	%rax, 256(%rsp)
	leaq	160(%rsp), %rax
	movq	%rsi, %rdx
	addq	40(%rsp), %rdx
	leaq	96(%rax), %rdi
.LEHB10:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructIPKcEEvT_S8_St20forward_iterator_tag.isra.25
.LEHE10:
	leaq	160(%rsp), %rax
	movq	256(%rsp), %rsi
	xorl	%ecx, %ecx
	xorl	%edx, %edx
	movl	$24, 248(%rsp)
	leaq	24(%rax), %rdi
.LEHB11:
	call	_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEE7_M_syncEPcmm
.LEHE11:
	leaq	160(%rsp), %rax
	leaq	184(%rsp), %rsi
	leaq	128(%rax), %rdi
.LEHB12:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE12:
	.p2align 4,,10
	.p2align 3
.L92:
	leaq	64(%rsp), %rsi
	leaq	160(%rsp), %rdi
.LEHB13:
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	leaq	96(%rsp), %rsi
	leaq	160(%rsp), %rdi
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	leaq	128(%rsp), %rsi
	leaq	160(%rsp), %rdi
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE
	movq	(%rax), %rdx
	movq	-24(%rdx), %rdx
	testb	$5, 32(%rax,%rdx)
	jne	.L96
	movq	128(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	movq	96(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	movsd	%xmm0, 8(%rsp)
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
	movq	64(%rsp), %rdx
	xorl	%ecx, %ecx
	movl	$.LC9, %esi
	movl	$strtod, %edi
	movsd	%xmm0, 16(%rsp)
	call	_ZN9__gnu_cxx6__stoaIddcJEEET0_PFT_PKT1_PPS3_DpT2_EPKcS5_PmS9_
.LEHE13:
	movsd	16(%rsp), %xmm1
	movsd	8(%rsp), %xmm2
	movsd	%xmm0, (%rbx)
	movsd	%xmm1, 8(%rbx)
	movsd	%xmm2, 16(%rbx)
	jmp	.L92
.L81:
	movq	%rbp, %rdi
.LEHB14:
	call	_ZNKSt5ctypeIcE13_M_widen_initEv
	movq	0(%rbp), %rax
	movl	$10, %edx
	movq	48(%rax), %rax
	cmpq	$_ZNKSt5ctypeIcE8do_widenEc, %rax
	je	.L82
	movl	$10, %esi
	movq	%rbp, %rdi
	call	*%rax
	movsbl	%al, %edx
	jmp	.L82
.L83:
	leaq	560(%rsp), %rax
	leaq	16(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE14:
	testq	%rax, %rax
	je	.L146
.L136:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L79
	call	_ZdlPv
.L79:
	leaq	576(%rsp), %rdi
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+24, 560(%rsp)
	movq	$_ZTVSt14basic_ifstreamIcSt11char_traitsIcEE+64, 816(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 576(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	680(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	632(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 576(%rsp)
	call	_ZNSt6localeD1Ev
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rax
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	leaq	816(%rsp), %rdi
	movq	-24(%rax), %rax
	movq	%rbx, 560(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	1080(%rsp), %rbx
	xorq	%fs:40, %rbx
	movq	24(%rsp), %rax
	jne	.L147
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
.L145:
	.cfi_restore_state
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB15:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE15:
	jmp	.L72
.L115:
	movq	$0, 24(%rsp)
	jmp	.L79
.L117:
	movq	%rax, %rbx
.L109:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L110
	call	_ZdlPv
.L110:
	leaq	560(%rsp), %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
.L137:
	movq	%rbx, %rdi
.LEHB16:
	call	_Unwind_Resume
.LEHE16:
.L124:
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rbx
	movq	-24(%rbp), %rdx
	movq	%rbx, 160(%rsp,%rdx)
	movq	%rax, %rbx
.L86:
	leaq	288(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 288(%rsp)
	call	_ZNSt8ios_baseD2Ev
.L95:
	movq	128(%rsp), %rdi
	leaq	144(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L106
	call	_ZdlPv
.L106:
	movq	96(%rsp), %rdi
	leaq	112(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L107
	call	_ZdlPv
.L107:
	movq	64(%rsp), %rdi
	leaq	80(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L109
	call	_ZdlPv
	jmp	.L109
.L125:
	movq	%rax, %rbx
.L94:
	leaq	240(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 184(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%r13), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+48(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	movq	-24(%r12), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+40(%rip), %rcx
	movq	%rcx, 176(%rsp,%rax)
	movq	-24(%rbp), %rax
	movq	_ZTTNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEEE+24(%rip), %rcx
	movq	%rcx, 160(%rsp,%rax)
	jmp	.L86
.L126:
	movq	%rax, %rbx
.L140:
	movq	256(%rsp), %rdi
	leaq	272(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L94
	call	_ZdlPv
	jmp	.L94
.L123:
	movq	%rax, %rbx
	movq	$_ZTVNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEEE+16, 184(%rsp)
	jmp	.L140
.L101:
.LEHB17:
	call	_ZSt16__throw_bad_castv
.L122:
	movq	%rax, %rbx
	jmp	.L86
.L120:
.L74:
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+8(%rip), %rbx
	movq	-24(%rbx), %rdx
	movq	_ZTTSt14basic_ifstreamIcSt11char_traitsIcEE+16(%rip), %rbx
	movq	%rbx, 560(%rsp,%rdx)
	movq	%rax, %rbx
.L75:
	leaq	816(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 816(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	160(%rsp), %rdi
	leaq	176(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L137
	call	_ZdlPv
	jmp	.L137
.L121:
	leaq	576(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rax
	jmp	.L74
.L118:
	leaq	160(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt7__cxx1118basic_stringstreamIcSt11char_traitsIcESaIcEED1Ev
	jmp	.L95
.L146:
	movq	560(%rsp), %rax
	leaq	560(%rsp), %rdi
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE17:
	jmp	.L136
.L147:
	call	__stack_chk_fail
.L119:
	movq	%rax, %rbx
	jmp	.L75
	.cfi_endproc
.LFE1859:
	.section	.gcc_except_table,"a",@progbits
.LLSDA1859:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1859-.LLSDACSB1859
.LLSDACSB1859:
	.uleb128 .LEHB3-.LFB1859
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB4-.LFB1859
	.uleb128 .LEHE4-.LEHB4
	.uleb128 .L119-.LFB1859
	.uleb128 0
	.uleb128 .LEHB5-.LFB1859
	.uleb128 .LEHE5-.LEHB5
	.uleb128 .L120-.LFB1859
	.uleb128 0
	.uleb128 .LEHB6-.LFB1859
	.uleb128 .LEHE6-.LEHB6
	.uleb128 .L121-.LFB1859
	.uleb128 0
	.uleb128 .LEHB7-.LFB1859
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L117-.LFB1859
	.uleb128 0
	.uleb128 .LEHB8-.LFB1859
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L122-.LFB1859
	.uleb128 0
	.uleb128 .LEHB9-.LFB1859
	.uleb128 .LEHE9-.LEHB9
	.uleb128 .L124-.LFB1859
	.uleb128 0
	.uleb128 .LEHB10-.LFB1859
	.uleb128 .LEHE10-.LEHB10
	.uleb128 .L125-.LFB1859
	.uleb128 0
	.uleb128 .LEHB11-.LFB1859
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L126-.LFB1859
	.uleb128 0
	.uleb128 .LEHB12-.LFB1859
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L123-.LFB1859
	.uleb128 0
	.uleb128 .LEHB13-.LFB1859
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L118-.LFB1859
	.uleb128 0
	.uleb128 .LEHB14-.LFB1859
	.uleb128 .LEHE14-.LEHB14
	.uleb128 .L117-.LFB1859
	.uleb128 0
	.uleb128 .LEHB15-.LFB1859
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L121-.LFB1859
	.uleb128 0
	.uleb128 .LEHB16-.LFB1859
	.uleb128 .LEHE16-.LEHB16
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB17-.LFB1859
	.uleb128 .LEHE17-.LEHB17
	.uleb128 .L117-.LFB1859
	.uleb128 0
.LLSDACSE1859:
	.text
	.size	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_, .-_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
	.section	.text.unlikely
.LCOLDE10:
	.text
.LHOTE10:
	.section	.text.unlikely
.LCOLDB11:
	.text
.LHOTB11:
	.p2align 4,,15
	.globl	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
	.type	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i, @function
_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i:
.LFB1862:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1862
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	%edx, %r12d
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	movq	%rsi, %rdx
	movq	%rdi, %rsi
	subq	$560, %rsp
	.cfi_def_cfa_offset 592
	movq	%rsp, %rdi
	movq	%fs:40, %rax
	movq	%rax, 552(%rsp)
	xorl	%eax, %eax
.LEHB18:
	call	_ZStplIcSt11char_traitsIcESaIcEENSt7__cxx1112basic_stringIT_T0_T1_EERKS8_SA_
.LEHE18:
	leaq	280(%rsp), %rdi
	call	_ZNSt8ios_baseC2Ev
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+8(%rip), %rbx
	movb	$0, 504(%rsp)
	leaq	32(%rsp), %rdi
	movq	_ZTTSt14basic_ofstreamIcSt11char_traitsIcEE+16(%rip), %rbp
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	xorl	%esi, %esi
	movq	$0, 496(%rsp)
	movb	$0, 505(%rsp)
	addq	-24(%rbx), %rdi
	movq	$0, 512(%rsp)
	movq	$0, 520(%rsp)
	movq	$0, 528(%rsp)
	movq	$0, 536(%rsp)
	movq	%rbx, 32(%rsp)
	movq	%rbp, (%rdi)
.LEHB19:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
.LEHE19:
	leaq	32(%rsp), %rax
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 32(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 280(%rsp)
	leaq	8(%rax), %rdi
.LEHB20:
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEEC1Ev
.LEHE20:
	leaq	32(%rsp), %rax
	leaq	40(%rsp), %rsi
	leaq	248(%rax), %rdi
.LEHB21:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE4initEPSt15basic_streambufIcS1_E
	leaq	32(%rsp), %rax
	movq	(%rsp), %rsi
	movl	$48, %edx
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	testq	%rax, %rax
	leaq	32(%rsp), %rdi
	movq	32(%rsp), %rax
	je	.L169
	addq	-24(%rax), %rdi
	xorl	%esi, %esi
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE21:
.L150:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L156
	call	_ZdlPv
.L156:
	leaq	32(%rsp), %rdi
	movl	%r12d, %esi
.LEHB22:
	call	_ZNSolsEi
	leaq	32(%rsp), %rax
	leaq	8(%rax), %rdi
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
.LEHE22:
	testq	%rax, %rax
	je	.L157
.L158:
	leaq	40(%rsp), %rdi
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+24, 32(%rsp)
	movq	$_ZTVSt14basic_ofstreamIcSt11char_traitsIcEE+64, 280(%rsp)
	movq	$_ZTVSt13basic_filebufIcSt11char_traitsIcEE+16, 40(%rsp)
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEE5closeEv
	leaq	144(%rsp), %rdi
	call	_ZNSt12__basic_fileIcED1Ev
	leaq	96(%rsp), %rdi
	movq	$_ZTVSt15basic_streambufIcSt11char_traitsIcEE+16, 40(%rsp)
	call	_ZNSt6localeD1Ev
	movq	-24(%rbx), %rax
	leaq	280(%rsp), %rdi
	movq	%rbp, 32(%rsp,%rax)
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	552(%rsp), %rax
	xorq	%fs:40, %rax
	jne	.L170
	addq	$560, %rsp
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
.L169:
	.cfi_restore_state
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB23:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE23:
	jmp	.L150
	.p2align 4,,10
	.p2align 3
.L157:
	movq	32(%rsp), %rax
	leaq	32(%rsp), %rdi
	addq	-24(%rax), %rdi
	movl	32(%rdi), %esi
	orl	$4, %esi
.LEHB24:
	call	_ZNSt9basic_iosIcSt11char_traitsIcEE5clearESt12_Ios_Iostate
.LEHE24:
	jmp	.L158
.L170:
	call	__stack_chk_fail
.L161:
	leaq	32(%rsp), %rdi
	movq	%rax, %rbx
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.L167:
	movq	%rbx, %rdi
.LEHB25:
	call	_Unwind_Resume
.LEHE25:
.L162:
	movq	%rax, %rbx
.L153:
	leaq	280(%rsp), %rdi
	movq	$_ZTVSt9basic_iosIcSt11char_traitsIcEE+16, 280(%rsp)
	call	_ZNSt8ios_baseD2Ev
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L167
	call	_ZdlPv
	jmp	.L167
.L164:
	leaq	40(%rsp), %rdi
	movq	%rax, %r12
	call	_ZNSt13basic_filebufIcSt11char_traitsIcEED1Ev
	movq	%r12, %rax
.L152:
	movq	-24(%rbx), %rdx
	movq	%rax, %rbx
	movq	%rbp, 32(%rsp,%rdx)
	jmp	.L153
.L163:
	jmp	.L152
	.cfi_endproc
.LFE1862:
	.section	.gcc_except_table
.LLSDA1862:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1862-.LLSDACSB1862
.LLSDACSB1862:
	.uleb128 .LEHB18-.LFB1862
	.uleb128 .LEHE18-.LEHB18
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB19-.LFB1862
	.uleb128 .LEHE19-.LEHB19
	.uleb128 .L162-.LFB1862
	.uleb128 0
	.uleb128 .LEHB20-.LFB1862
	.uleb128 .LEHE20-.LEHB20
	.uleb128 .L163-.LFB1862
	.uleb128 0
	.uleb128 .LEHB21-.LFB1862
	.uleb128 .LEHE21-.LEHB21
	.uleb128 .L164-.LFB1862
	.uleb128 0
	.uleb128 .LEHB22-.LFB1862
	.uleb128 .LEHE22-.LEHB22
	.uleb128 .L161-.LFB1862
	.uleb128 0
	.uleb128 .LEHB23-.LFB1862
	.uleb128 .LEHE23-.LEHB23
	.uleb128 .L164-.LFB1862
	.uleb128 0
	.uleb128 .LEHB24-.LFB1862
	.uleb128 .LEHE24-.LEHB24
	.uleb128 .L161-.LFB1862
	.uleb128 0
	.uleb128 .LEHB25-.LFB1862
	.uleb128 .LEHE25-.LEHB25
	.uleb128 0
	.uleb128 0
.LLSDACSE1862:
	.text
	.size	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i, .-_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
	.section	.text.unlikely
.LCOLDE11:
	.text
.LHOTE11:
	.section	.rodata.str1.1
.LC12:
	.string	"connect.inp"
.LC13:
	.string	"./"
.LC14:
	.string	"connect.out"
	.section	.text.unlikely
.LCOLDB15:
	.section	.text.startup,"ax",@progbits
.LHOTB15:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1858:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1858
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	movl	$.LC12, %esi
	subq	$80, %rsp
	.cfi_def_cfa_offset 96
	leaq	32(%rsp), %rdi
	movq	%fs:40, %rax
	movq	%rax, 72(%rsp)
	xorl	%eax, %eax
.LEHB26:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE26:
	movl	$.LC13, %esi
	movq	%rsp, %rdi
.LEHB27:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE27:
	leaq	32(%rsp), %rsi
	movq	%rsp, %rdi
.LEHB28:
	call	_Z10ReadPointsNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_
.LEHE28:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L172
	call	_ZdlPv
.L172:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L173
	call	_ZdlPv
.L173:
	movq	%rbx, %rdi
	call	_Z17GetShortestLengthP5Point
	leaq	32(%rsp), %rdi
	movl	$.LC14, %esi
	movl	%eax, %ebx
.LEHB29:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE29:
	movl	$.LC13, %esi
	movq	%rsp, %rdi
.LEHB30:
	call	_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC2EPKcRKS3_.isra.27
.LEHE30:
	leaq	32(%rsp), %rsi
	movl	%ebx, %edx
	movq	%rsp, %rdi
.LEHB31:
	call	_Z9PrintFileNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES4_i
.LEHE31:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L174
	call	_ZdlPv
.L174:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L175
	call	_ZdlPv
.L175:
	xorl	%eax, %eax
	movq	72(%rsp), %rcx
	xorq	%fs:40, %rcx
	jne	.L193
	addq	$80, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 16
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
.L193:
	.cfi_restore_state
	call	__stack_chk_fail
.L188:
	movq	(%rsp), %rdi
	leaq	16(%rsp), %rdx
	movq	%rax, %rbx
	cmpq	%rdx, %rdi
	je	.L182
	call	_ZdlPv
.L182:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rdx
	cmpq	%rdx, %rdi
	je	.L183
.L191:
	call	_ZdlPv
.L183:
	movq	%rbx, %rdi
.LEHB32:
	call	_Unwind_Resume
.LEHE32:
.L187:
	movq	%rax, %rbx
	jmp	.L182
.L186:
	movq	(%rsp), %rdi
	movq	%rax, %rbx
	leaq	16(%rsp), %rax
	cmpq	%rax, %rdi
	je	.L178
	call	_ZdlPv
.L178:
	movq	32(%rsp), %rdi
	leaq	48(%rsp), %rax
	cmpq	%rax, %rdi
	jne	.L191
	jmp	.L183
.L185:
	movq	%rax, %rbx
	jmp	.L178
	.cfi_endproc
.LFE1858:
	.section	.gcc_except_table
.LLSDA1858:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1858-.LLSDACSB1858
.LLSDACSB1858:
	.uleb128 .LEHB26-.LFB1858
	.uleb128 .LEHE26-.LEHB26
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB27-.LFB1858
	.uleb128 .LEHE27-.LEHB27
	.uleb128 .L185-.LFB1858
	.uleb128 0
	.uleb128 .LEHB28-.LFB1858
	.uleb128 .LEHE28-.LEHB28
	.uleb128 .L186-.LFB1858
	.uleb128 0
	.uleb128 .LEHB29-.LFB1858
	.uleb128 .LEHE29-.LEHB29
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB30-.LFB1858
	.uleb128 .LEHE30-.LEHB30
	.uleb128 .L187-.LFB1858
	.uleb128 0
	.uleb128 .LEHB31-.LFB1858
	.uleb128 .LEHE31-.LEHB31
	.uleb128 .L188-.LFB1858
	.uleb128 0
	.uleb128 .LEHB32-.LFB1858
	.uleb128 .LEHE32-.LEHB32
	.uleb128 0
	.uleb128 0
.LLSDACSE1858:
	.section	.text.startup
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE15:
	.section	.text.startup
.LHOTE15:
	.section	.text.unlikely
.LCOLDB16:
	.section	.text.startup
.LHOTB16:
	.p2align 4,,15
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB2165:
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
.LFE2165:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.text.unlikely
.LCOLDE16:
	.section	.text.startup
.LHOTE16:
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_main
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC5:
	.long	0
	.long	1071644672
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
'''
s1 = '''.file	"1.cpp"
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
'''
##################
string  = ''' .file	"fact.cpp"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB0:
	.text
.LHOTB0:
	.p2align 4,,15
	.globl	_Z4factx
	.type	_Z4factx, @function
_Z4factx:
.LFB1048:
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
.LFE1048:
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
.LFB1049:
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
.LFE1049:
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
.LFB1050:
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
.LFE1050:
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
.LFB1058:
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
.LFE1058:
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
'''
###############
str2 = ''' .file	"bigzero1.cpp"
	.section	.text._ZStorSt13_Ios_OpenmodeS_,"axG",@progbits,_ZStorSt13_Ios_OpenmodeS_,comdat
	.weak	_ZStorSt13_Ios_OpenmodeS_
	.type	_ZStorSt13_Ios_OpenmodeS_, @function
_ZStorSt13_Ios_OpenmodeS_:
.LFB644:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	movl	-4(%rbp), %eax
	orl	-8(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE644:
	.size	_ZStorSt13_Ios_OpenmodeS_, .-_ZStorSt13_Ios_OpenmodeS_
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.globl	__powidf2
	.section	.text._ZSt3powdi,"axG",@progbits,_ZSt3powdi,comdat
	.weak	_ZSt3powdi
	.type	_ZSt3powdi, @function
_ZSt3powdi:
.LFB1138:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movsd	%xmm0, -8(%rbp)
	movl	%edi, -12(%rbp)
	movl	-12(%rbp), %edi
	movsd	-8(%rbp), %xmm0
	call	__powidf2
	movq	%xmm0, %rax
	movq	%rax, -24(%rbp)
	movsd	-24(%rbp), %xmm0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1138:
	.size	_ZSt3powdi, .-_ZSt3powdi
	.section	.rodata
.LC0:
	.string	"connect.inp"
.LC2:
	.string	"connect.out"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1169:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	.cfi_lsda 0x3,.LLSDA1169
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%r12
	pushq	%rbx
	subq	$1184, %rsp
	.cfi_offset 12, -24
	.cfi_offset 3, -32
	movq	%fs:40, %rax
	movq	%rax, -24(%rbp)
	xorl	%eax, %eax
	movq	$0, -1152(%rbp)
	movq	$0, -1144(%rbp)
	movq	$0, -1136(%rbp)
	movq	$0, -1120(%rbp)
	movq	$0, -1112(%rbp)
	movq	$0, -1104(%rbp)
	movq	$0, -1088(%rbp)
	movq	$0, -1080(%rbp)
	movq	$0, -1072(%rbp)
	leaq	-544(%rbp), %rax
	movq	%rax, %rdi
.LEHB0:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEEC1Ev
.LEHE0:
	leaq	-544(%rbp), %rax
	movl	$8, %edx
	movl	$.LC0, %esi
	movq	%rax, %rdi
.LEHB1:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	movl	$0, -1172(%rbp)
.L7:
	cmpl	$2, -1172(%rbp)
	jg	.L6
	leaq	-1088(%rbp), %rax
	movl	-1172(%rbp), %edx
	movslq	%edx, %rdx
	salq	$3, %rdx
	leaq	(%rax,%rdx), %rbx
	leaq	-1120(%rbp), %rax
	movl	-1172(%rbp), %edx
	movslq	%edx, %rdx
	salq	$3, %rdx
	leaq	(%rax,%rdx), %r12
	leaq	-1152(%rbp), %rax
	movl	-1172(%rbp), %edx
	movslq	%edx, %rdx
	salq	$3, %rdx
	addq	%rax, %rdx
	leaq	-544(%rbp), %rax
	movq	%rdx, %rsi
	movq	%rax, %rdi
	call	_ZNSirsERd
	movq	%r12, %rsi
	movq	%rax, %rdi
	call	_ZNSirsERd
	movq	%rbx, %rsi
	movq	%rax, %rdi
	call	_ZNSirsERd
	addl	$1, -1172(%rbp)
	jmp	.L7
.L6:
	leaq	-544(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEE5closeEv
.L14:
	movsd	-1152(%rbp), %xmm0
	movsd	-1136(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	movsd	%xmm0, -1192(%rbp)
	movsd	-1120(%rbp), %xmm0
	movsd	-1104(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	movapd	%xmm0, %xmm2
	addsd	-1192(%rbp), %xmm2
	movsd	%xmm2, -1192(%rbp)
	movsd	-1088(%rbp), %xmm0
	movsd	-1072(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	addsd	-1192(%rbp), %xmm0
	call	sqrt
	movq	%xmm0, %rax
	movq	%rax, -1168(%rbp)
	movsd	-1144(%rbp), %xmm0
	movsd	-1136(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	movsd	%xmm0, -1192(%rbp)
	movsd	-1112(%rbp), %xmm0
	movsd	-1104(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	movapd	%xmm0, %xmm3
	addsd	-1192(%rbp), %xmm3
	movsd	%xmm3, -1192(%rbp)
	movsd	-1080(%rbp), %xmm0
	movsd	-1072(%rbp), %xmm1
	subsd	%xmm1, %xmm0
	movl	$2, %edi
	call	_ZSt3powdi
	addsd	-1192(%rbp), %xmm0
	call	sqrt
	movq	%xmm0, %rax
	movq	%rax, -1160(%rbp)
	movsd	-1168(%rbp), %xmm0
	ucomisd	-1160(%rbp), %xmm0
	jbe	.L23
	movsd	-1152(%rbp), %xmm1
	movsd	-1144(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1152(%rbp)
	movsd	-1120(%rbp), %xmm1
	movsd	-1112(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1120(%rbp)
	movsd	-1088(%rbp), %xmm1
	movsd	-1080(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1088(%rbp)
	jmp	.L14
.L23:
	movsd	-1160(%rbp), %xmm0
	ucomisd	-1168(%rbp), %xmm0
	ja	.L22
	nop
	leaq	-1056(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEEC1Ev
.LEHE1:
	jmp	.L24
.L22:
	movsd	-1152(%rbp), %xmm1
	movsd	-1144(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1144(%rbp)
	movsd	-1120(%rbp), %xmm1
	movsd	-1112(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1112(%rbp)
	movsd	-1088(%rbp), %xmm1
	movsd	-1080(%rbp), %xmm0
	addsd	%xmm1, %xmm0
	movsd	.LC1(%rip), %xmm1
	divsd	%xmm1, %xmm0
	movsd	%xmm0, -1080(%rbp)
	jmp	.L14
.L24:
	movl	$32, %esi
	movl	$16, %edi
	call	_ZStorSt13_Ios_OpenmodeS_
	movl	%eax, %edx
	leaq	-1056(%rbp), %rax
	movl	$.LC2, %esi
	movq	%rax, %rdi
.LEHB2:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE4openEPKcSt13_Ios_Openmode
	movq	-1168(%rbp), %rax
	movq	%rax, -1192(%rbp)
	movsd	-1192(%rbp), %xmm0
	call	ceil
	leaq	-1056(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSolsEd
	leaq	-1056(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEE5closeEv
.LEHE2:
	movl	$0, %ebx
	leaq	-1056(%rbp), %rax
	movq	%rax, %rdi
.LEHB3:
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
.LEHE3:
	leaq	-544(%rbp), %rax
	movq	%rax, %rdi
.LEHB4:
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
.LEHE4:
	movl	%ebx, %eax
	movq	-24(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L18
	jmp	.L25
.L20:
	movq	%rax, %rbx
	leaq	-1056(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt14basic_ofstreamIcSt11char_traitsIcEED1Ev
	jmp	.L17
.L19:
	movq	%rax, %rbx
.L17:
	leaq	-544(%rbp), %rax
	movq	%rax, %rdi
	call	_ZNSt14basic_ifstreamIcSt11char_traitsIcEED1Ev
	movq	%rbx, %rax
	movq	%rax, %rdi
.LEHB5:
	call	_Unwind_Resume
.LEHE5:
.L25:
	call	__stack_chk_fail
.L18:
	addq	$1184, %rsp
	popq	%rbx
	popq	%r12
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1169:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA1169:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1169-.LLSDACSB1169
.LLSDACSB1169:
	.uleb128 .LEHB0-.LFB1169
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB1169
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L19-.LFB1169
	.uleb128 0
	.uleb128 .LEHB2-.LFB1169
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L20-.LFB1169
	.uleb128 0
	.uleb128 .LEHB3-.LFB1169
	.uleb128 .LEHE3-.LEHB3
	.uleb128 .L19-.LFB1169
	.uleb128 0
	.uleb128 .LEHB4-.LFB1169
	.uleb128 .LEHE4-.LEHB4
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB5-.LFB1169
	.uleb128 .LEHE5-.LEHB5
	.uleb128 0
	.uleb128 0
.LLSDACSE1169:
	.text
	.size	main, .-main
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1221:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	cmpl	$1, -4(%rbp)
	jne	.L28
	cmpl	$65535, -8(%rbp)
	jne	.L28
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
.L28:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1221:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB1222:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1222:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_main
	.section	.rodata
	.align 8
.LC1:
	.long	0
	.long	1073741824
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
'''
#print(string)
asmarr = string.split('\n')
#print(asmarr)

rmhead = map(lambda s:s.lstrip(), asmarr)
print('----splited, striped----')
print(rmhead)

def is_not_inst(s):
    return (len(s) != 0 and s[0] != '.')
filtered = filter(is_not_inst, rmhead)
print('----remove dot cmd----')
for e in filtered: print e

def inst2str(s):
    splited_arr = s.split('\t')
    if splited_arr[0] == 'call':
        return splited_arr[1]
    return splited_arr[0]
inst_list = map(inst2str, filtered)
#inst_list = map(lambda s:s.split('\t')[0], filtered)
print('-------')
for e in inst_list: print e
#print(filtered)

def proc_dict(inst_list):
    proc_dict = {}
    now_proc = None
    for s in inst_list:
        if s[-1] == ':':
            proc_name = s[:-1] # remove trailing ':'
            now_proc = proc_name
            proc_dict[proc_name] = [] 
        else:
            #inst_seq = proc_dict[now_proc]
            #inst_seq.append(s)
            proc_dict[now_proc].append(s)
    return proc_dict


# side effect!: param seq changed.
def sequence(procdict):
    def _sequence(procdict, ret_seq, history_stack, now_proc):
        history_stack.append(now_proc)
        now_proc_seq = procdict[now_proc]
        for instruction in now_proc_seq:
            if (procdict.get(instruction) and 
                instruction not in history_stack):
                _sequence(procdict, ret_seq, history_stack, instruction)
            else:
                ret_seq.append(instruction)
        history_stack.pop()
        return ret_seq
    return _sequence(procdict,[],[],"main")

str1proc_dict = proc_dict(inst_list)
for k, v in str1proc_dict.iteritems():
    print k
    print v

str1seq = sequence(str1proc_dict)
str2seq = sequence(
            proc_dict(
              map(inst2str,
                  filter(is_not_inst, 
                         map(lambda s:s.lstrip(), 
                             str2.split('\n'))))))
print '-------str1 seq-------'
print(str1seq)
print '-------str2 seq-------'
print(str2seq)

import comparator
score = comparator.match_score(str1seq,str2seq)
print('score is ' + str(score))

'''
seq1 = sequence(
            proc_dict(
              map(inst2str,
                  filter(is_not_inst, 
                         map(lambda s:s.lstrip(), 
                             fgeeks.split('\n'))))))
print(seq1)
seq2 = sequence(
            proc_dict(
              map(inst2str,
                  filter(is_not_inst, 
                         map(lambda s:s.lstrip(), 
                             fgeeks.split('\n'))))))
print(seq2)
score = comparator.match_score(seq1,seq2)
base_len = min(len(seq1),len(seq2))
print('match score is ' + str(score))
print('/min_len similarity is ' + str(float(score)/float(base_len)))
print('/a+b_len * 2 similarity is ' + str(2 * float(score)/float(len(seq1)+len(seq2))))
'''
strs = [(fs1_1,'fs1_1'),
        (fs1_2,'fs1_2'),
        (fs1_3,'fs1_3'),
        (fs1_4,'fs1_4'),
        (fs2,'fs2'),
        (fs3,'fs3'),
        (fs4,'fs4'),
        (fgeeks,'fgeeks')]

for a in strs:
    for b in strs:
        seq1 = sequence(
                    proc_dict(
                      map(inst2str,
                          filter(is_not_inst, 
                                 map(lambda s:s.lstrip(), 
                                     a[0].split('\n'))))))
        seq2 = sequence(
                    proc_dict(
                      map(inst2str,
                          filter(is_not_inst, 
                                 map(lambda s:s.lstrip(), 
                                     b[0].split('\n'))))))
        score = comparator.match_score(seq1,seq2)
        base_len = min(len(seq1),len(seq2))
        print(a[1] + ' vs ' + b[1] + ' match score is\t\t\t' + str(score))
        print(a[1] + ' vs ' + b[1] + ' /min_len similarity is\t\t' + str(float(score)/float(base_len)))
        print(a[1] + ' vs ' + b[1] + ' /a+b_len * 2 similarity is\t' + str(2 * float(score)/float(len(seq1)+len(seq2))))
        print('------')



import unittest
class sequenceTest(unittest.TestCase):
    def test_no_proc_call(self):
        proc_dict = {'main':['1','2','3','4'],
                     'p'   :['10','20','30']}
        expected = ['1','2','3','4']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_no_recur(self):
        proc_dict = {'main':['1','2','3','4','p'],
                     'p'   :['10','20','30']}
        expected = ['1','2','3','4','10','20','30']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_call_more(self):
        proc_dict = {'main':['1','2','p1','4','p2'],
                     'p1'  :['10','20','30'],
                     'p2'  :['a','b','c']}
        expected = ['1','2','10','20','30','4',
                    'a','b','c']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_call_more_depth(self):
        proc_dict = {'main':['a','b','c','d'],
                     'a'   :['1','2','3'],
                     'b'   :['4','5'],
                     'c'   :['6']}
        expected = ['1','2','3','4','5','6','d']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_remove_recur(self):
        proc_dict = {'main':['1','main']}
        expected = ['1','main']
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    #@unittest.skip("not now")
    def test_remove_mutual_recur(self):
        proc_dict = {'main':['a'],
                     'a'   :['1','b'],
                     'b'   :['2','a']}
        expected = ['1','2','a'] # sort of... dfs.
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

    def test_remove_mutual_recur2(self):
        proc_dict = {'main':['a','b','a'],
                     'a'   :['1','2','a','a','3'],
                     'b'   :['7','8','a','b']}
        expected = ['1','2','a','a','3',
                    '7','8','1','2','a','a','3','b',
                    '1','2','a','a','3'] 
        actual = sequence(proc_dict)
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
    '''
    print '---------'
    result = sequence(proc_dict)
    print result
    print '\n'.join(result)
    '''

#import re
#is_proc_decl = re.compile('.*:')

#pattern = re.compile('.*:')
#result = pattern.findall(string)
#print(result)
