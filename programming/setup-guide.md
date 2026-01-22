# Guia de Instalação - Qiskit + Jupyter

## 1. Download e Instalação do Anaconda

1. Acesse [anaconda.com/download](https://www.anaconda.com/download)
2. Clique em "Get Started" (botão verde)
3. Selecione seu sistema operacional (Windows/Mac/Linux)
4. Baixe o instalador (versão Python 3.11 ou superior)
5. Execute o instalador e siga as instruções padrão
6. Reinicie o computador após a instalação

## 2. Instalação do Qiskit

Após instalar o Anaconda, abra o **Anaconda Prompt** (ou Terminal no Mac/Linux) e execute:

```bash
# Criar ambiente virtual para Qiskit (recomendado)
conda create -n qiskit_env python=3.11
conda activate qiskit_env

# Instalar Qiskit
pip install qiskit qiskit-aer

# Instalar Qiskit IBM Runtime (para computadores quânticos da IBM)
pip install qiskit-ibm-runtime
```

Verificar instalação:

```bash
python -c "import qiskit; print(qiskit.__version__)"
```

## 3. Cadastro na IBM Quantum Platform

1. Acesse [quantum.ibm.com](https://quantum.ibm.com)
2. Clique em "Conectar" (canto superior direito)
3. Opções de cadastro:
   - Email
   - GitHub
   - IBMid
4. Complete o cadastro e confirme o email
5. **Guarde o token de autenticação** que você receberá

## 4. Instalar Jupyter Notebook

```bash
# Jupyter já vem com Anaconda, mas para garantir atualização:
conda install jupyter notebook

# Ou instale JupyterLab (versão mais moderna):
conda install jupyterlab
```

## 5. Iniciar Jupyter Notebook

```bash
# Ativar o ambiente
conda activate qiskit_env

# Iniciar Jupyter Notebook
jupyter notebook

# OU iniciar JupyterLab
jupyter lab
```

O Jupyter abrirá automaticamente no navegador (geralmente em `http://localhost:8888`)

## 6. Testar a Instalação

Crie uma nova célula no Jupyter e execute:

```python
# Verificar Qiskit
import qiskit
print(f"Qiskit versão: {qiskit.__version__}")

# Criar um circuito simples
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qr, cr)
circuit.h(qr[0])
circuit.measure(qr[0], cr[0])

print(circuit)
```

Se aparecer o circuito sem erros, a instalação está correta.

## 7. Conectar com IBM Quantum (Opcional)

Após cadastro, com seu token:

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# Salvar credenciais (execute uma única vez)
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    instance="ibm-q/open/main",
    token="SEU_TOKEN_AQUI"  # Substitua pelo seu token
)

# Carregar credenciais salvas
service = QiskitRuntimeService(channel="ibm_quantum")
```

## Resumo

| Etapa | Ação | Local |
|-------|------|-------|
| 1 | Download e instalação Anaconda | [anaconda.com](https://www.anaconda.com/download) |
| 2 | Executar comandos pip | Terminal/Anaconda Prompt |
| 3 | Cadastro IBM | [quantum.ibm.com](https://quantum.ibm.com) |
| 4 | Instalar Jupyter | Terminal |
| 5 | Abrir Jupyter | `jupyter notebook` |
| 6 | Testar instalação | Jupyter Notebook |
