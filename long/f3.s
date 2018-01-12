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
