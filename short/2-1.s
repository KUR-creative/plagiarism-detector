	.file	"2-1.cpp"
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
