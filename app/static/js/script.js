document.addEventListener('DOMContentLoaded', function() {
    // Elementos do DOM
    const form = document.getElementById('consultaForm');
    const modal = document.getElementById('resultadoModal');
    const modalClose = document.querySelector('.modal-close');
    const loading = document.getElementById('loading');
    const resultadoConteudo = document.getElementById('resultadoConteudo');

    // Event Listeners
    form.addEventListener('submit', handleFormSubmit);
    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });
    
    // Botão de limpeza
    const btnLimpar = document.getElementById('btnLimpar');
    if (btnLimpar) {
        btnLimpar.addEventListener('click', clearForm);
    }

    // Configurar alternância de cores dos campos de município
    setupMunicipalityFieldColors();
    
    // Inicializar sistema de temas
    initThemeSystem();

    // Fechar modal com ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('show')) {
            closeModal();
        }
    });

    async function handleFormSubmit(e) {
        e.preventDefault();
        
        // Limpar erros anteriores
        clearErrors();
        
        // Obter dados do formulário
        const formData = new FormData(form);
        
        // Validar campos obrigatórios
        const errors = validateForm(formData);
        if (errors.length > 0) {
            showValidationErrors(errors);
            return;
        }
        
        // Mostrar loading
        showLoading();
        
        try {
            // Enviar requisição
            const response = await fetch('/consultar', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            // Esconder loading
            hideLoading();
            
            // Mostrar resultado
            showResult(data);
            
        } catch (error) {
            hideLoading();
            showError('Erro de conexão. Tente novamente.');
        }
    }

    function validateForm(formData) {
        const errors = [];
        const fields = {
            'servico_id': 'Serviço',
            'municipio_prestador': 'Município do Prestador',
            'municipio_tomador': 'Município do Tomador',
            'municipio_execucao': 'Município da Execução'
        };

        for (const [fieldName, fieldLabel] of Object.entries(fields)) {
            const value = formData.get(fieldName);
            if (!value || value.trim() === '') {
                errors.push(`${fieldLabel} é obrigatório`);
            }
        }

        return errors;
    }

    function showValidationErrors(errors) {
        // Aplicar efeito de tremor nos campos vazios
        const fields = ['servico_id', 'municipio_prestador', 'municipio_tomador', 'municipio_execucao'];
        
        fields.forEach(fieldName => {
            const field = document.getElementById(fieldName);
            const value = field.value;
            
            if (!value || value.trim() === '') {
                field.classList.add('error');
                setTimeout(() => {
                    field.classList.remove('error');
                }, 500);
            }
        });

        // Mostrar modal com erros
        const errorData = {
            sucesso: false,
            erros: errors
        };
        showResult(errorData);
    }

    function showResult(data) {
        if (data.sucesso) {
            resultadoConteudo.innerHTML = `
                <div class="resultado-sucesso">
                    <div class="resultado-principal">
                        <div class="resultado-icone">
                            <svg viewBox="0 0 24 24" class="location-icon" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" fill="white" fill-opacity="0.9"/>
                                <circle cx="12" cy="9" r="2.5" fill="#10b981" stroke="white" stroke-width="1"/>
                                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        <h2 class="resultado-local-titulo">Local de Recolhimento</h2>
                        <div class="resultado-local-valor">${data.local_recolhimento}</div>
                    </div>
                    
                    <div class="resultado-resumo">
                        <p class="servico-nome">${data.servico}</p>
                    </div>
                    
                    <details class="resultado-detalhes">
                        <summary>Ver detalhes completos</summary>
                        <div class="detalhes-conteudo">
                            <div class="detalhe-item">
                                <span class="detalhe-label">Município do Prestador:</span>
                                <span class="detalhe-valor">${data.municipio_prestador}</span>
                            </div>
                            <div class="detalhe-item">
                                <span class="detalhe-label">Município do Tomador:</span>
                                <span class="detalhe-valor">${data.municipio_tomador}</span>
                            </div>
                            <div class="detalhe-item">
                                <span class="detalhe-label">Município da Execução:</span>
                                <span class="detalhe-valor">${data.municipio_execucao}</span>
                            </div>
                            <div class="base-legal">
                                <strong>Base Legal:</strong>
                                <p>${data.justificativa_legal}</p>
                            </div>
                        </div>
                    </details>
                </div>
            `;
        } else {
            resultadoConteudo.innerHTML = `
                <div class="resultado-erro">
                    <div class="erro-icone">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L2 22h20L12 2z" fill="white" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M12 9v4" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                            <path d="M12 17h.01" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <h3 class="erro-titulo">Erro na Consulta</h3>
                    <div class="erro-lista">
                        ${data.erros.map(erro => `<div class="erro-item">${erro}</div>`).join('')}
                    </div>
                </div>
            `;
        }
        
        openModal();
    }

    function showError(message) {
        resultadoConteudo.innerHTML = `
            <div class="resultado-erro">
                <div class="erro-icone">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2L2 22h20L12 2z" fill="white" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M12 9v4" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                        <path d="M12 17h.01" stroke="#ef4444" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                <h3 class="erro-titulo">Erro de Conexão</h3>
                <div class="erro-lista">
                    <div class="erro-item">${message}</div>
                </div>
            </div>
        `;
        openModal();
    }

    function openModal() {
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('show');
        document.body.style.overflow = 'auto';
    }

    function showLoading() {
        loading.classList.remove('hidden');
    }

    function hideLoading() {
        loading.classList.add('hidden');
    }

    function clearErrors() {
        const fields = document.querySelectorAll('.form-input, .form-select');
        fields.forEach(field => {
            field.classList.remove('error');
        });
    }

    // Melhorar UX com auto-complete e formatação
    const municipioInputs = document.querySelectorAll('input[name^="municipio"]');
    municipioInputs.forEach(input => {
        input.addEventListener('input', function() {
            // Capitalizar primeira letra de cada palavra (incluindo acentos)
            this.value = this.value.toLowerCase().replace(/(?:^|\s)([a-záàâãéêíóôõúç])/g, function(match, letter) {
                return match.replace(letter, letter.toUpperCase());
            });
        });
    });

    // Função para configurar alternância de cores dos campos de município
    function setupMunicipalityFieldColors() {
        const municipalityFields = {
            'municipio_prestador': 'filled-prestador',
            'municipio_tomador': 'filled-tomador',
            'municipio_execucao': 'filled-execucao'
        };

        Object.entries(municipalityFields).forEach(([fieldId, className]) => {
            const field = document.getElementById(fieldId);
            if (field) {
                // Verificar estado inicial
                updateFieldColor(field, className);

                // Adicionar listeners para mudanças
                field.addEventListener('input', function() {
                    updateFieldColor(this, className);
                });

                field.addEventListener('blur', function() {
                    updateFieldColor(this, className);
                });

                field.addEventListener('focus', function() {
                    updateFieldColor(this, className);
                });
            }
        });
    }

    function updateFieldColor(field, className) {
        // Remover todas as classes de preenchimento
        field.classList.remove('filled-prestador', 'filled-tomador', 'filled-execucao');
        
        // Adicionar classe se o campo estiver preenchido
        if (field.value.trim() !== '') {
            field.classList.add(className);
        }
    }
    
    // Função para limpar o formulário
    function clearForm() {
        // Limpar todos os campos do formulário
        const servicoSelect = document.getElementById('servico_id');
        const municipioPrestador = document.getElementById('municipio_prestador');
        const municipioTomador = document.getElementById('municipio_tomador');
        const municipioExecucao = document.getElementById('municipio_execucao');
        
        // Resetar valores
        if (servicoSelect) servicoSelect.value = '';
        if (municipioPrestador) municipioPrestador.value = '';
        if (municipioTomador) municipioTomador.value = '';
        if (municipioExecucao) municipioExecucao.value = '';
        
        // Remover classes de preenchimento dos campos de município
        const municipalityFields = [municipioPrestador, municipioTomador, municipioExecucao];
        municipalityFields.forEach(field => {
            if (field) {
                field.classList.remove('filled-prestador', 'filled-tomador', 'filled-execucao', 'error');
            }
        });
        
        // Remover classe de erro do select também
        if (servicoSelect) {
            servicoSelect.classList.remove('error');
        }
        
        // Fechar modal se estiver aberto
        if (modal.classList.contains('show')) {
            closeModal();
        }
        
        // Focar no primeiro campo
         if (servicoSelect) {
             servicoSelect.focus();
         }
     }
     
     // Sistema de Temas
     function initThemeSystem() {
         const themeToggle = document.getElementById('themeToggle');
         const sunIcon = document.getElementById('sunIcon');
         const moonIcon = document.getElementById('moonIcon');
         
         if (!themeToggle) return;
         
         // Carregar tema salvo ou usar padrão (claro)
         const savedTheme = localStorage.getItem('theme') || 'light';
         setTheme(savedTheme);
         
         // Event listener para o botão de toggle
         themeToggle.addEventListener('click', function() {
             const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
             const newTheme = currentTheme === 'light' ? 'dark' : 'light';
             setTheme(newTheme);
             localStorage.setItem('theme', newTheme);
         });
     }
     
     function setTheme(theme) {
         const sunIcon = document.getElementById('sunIcon');
         const moonIcon = document.getElementById('moonIcon');
         
         document.documentElement.setAttribute('data-theme', theme);
         
         if (sunIcon && moonIcon) {
             if (theme === 'dark') {
                 sunIcon.style.display = 'block';
                 moonIcon.style.display = 'none';
             } else {
                 sunIcon.style.display = 'none';
                 moonIcon.style.display = 'block';
             }
         }
     }
});