	.file	"1-1.cpp"
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
