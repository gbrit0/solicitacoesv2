# Funcionalidade de Edição de Solicitações

## Visão Geral

A funcionalidade de edição de solicitações permite carregar dados de uma solicitação existente no formulário `PurchaseRequestForm` e editá-los. O sistema diferencia entre modo de criação e modo de edição.

## Componentes Modificados

### 1. PurchaseRequestForm.tsx

**Novas Props:**
- `editData?: IListaDeSolicitacoes` - Dados da solicitação para edição
- `isEditMode?: boolean` - Flag para indicar modo de edição (padrão: false)
- `onCancel?: () => void` - Callback para cancelar edição

**Funcionalidades Adicionadas:**
- Carregamento automático de dados quando em modo de edição
- Título dinâmico (Nova/Editar Solicitação)
- Botões dinâmicos (Criar/Atualizar Solicitação)
- Lógica de submit diferenciada (POST para criação, PUT para edição)

### 2. RequestsTable.tsx

**Modificações:**
- Função `handleEdit` atualizada para navegar para página de edição
- Navegação com dados da solicitação no estado

### 3. Novos Componentes Criados

#### EditPurchaseRequestExample.tsx
Componente de exemplo que demonstra como usar o formulário em modo de edição com carregamento de dados.

#### useEditRequest.tsx
Hook personalizado para gerenciar estado de edição de solicitações.

#### EditRequest.tsx
Página dedicada para edição de solicitações.

## Como Usar

### 1. Uso Básico do Formulário em Modo de Edição

```tsx
import PurchaseRequestForm from '@/components/PurchaseRequestForm';

const MyComponent = () => {
  const user = { id: 1, name: 'Usuário', email: 'user@exemplo.com', nome: 'Usuário', sobrenome: 'Exemplo' };
  
  const editData = {
    requestDate: new Date(),
    requester: 'Usuário',
    sc: '12345',
    items: [
      {
        recno: '1',
        item: '1',
        status: 'Solicitação Pendente',
        sb1_recno: 123,
        product: '123',
        quantity: 5,
        needDate: '2025-01-15',
        observations: 'Observações',
        ctt_recno: '456',
        centro_de_custo: '456',
        ctj_recno: 789,
        rateio: '789'
      }
    ]
  };

  return (
    <PurchaseRequestForm
      user={user}
      editData={editData}
      isEditMode={true}
      onCancel={() => console.log('Cancelado')}
    />
  );
};
```

### 2. Usando o Hook useEditRequest

```tsx
import useEditRequest from '@/hooks/useEditRequest';

const MyComponent = () => {
  const { editData, loading, error, loadRequestData, clearData } = useEditRequest();

  const handleLoadRequest = async (requestId: string) => {
    await loadRequestData(requestId);
  };

  return (
    <div>
      {loading && <p>Carregando...</p>}
      {error && <p>Erro: {error}</p>}
      {editData && (
        <PurchaseRequestForm
          user={user}
          editData={editData}
          isEditMode={true}
          onCancel={clearData}
        />
      )}
    </div>
  );
};
```

### 3. Navegação da Tabela para Edição

A tabela de solicitações já está configurada para navegar para a página de edição:

```tsx
// Em RequestsTable.tsx
const handleEdit = (request: IListaDeSolicitacoes) => {
  navigate(`/editar-solicitacao/${request.sc}`, { 
    state: { 
      requestData: request,
      isEditMode: true 
    } 
  });
};
```

## Estrutura de Dados

### IListaDeSolicitacoes
```typescript
interface IListaDeSolicitacoes {
  requestDate: Date;
  requester: string;
  sc: string;
  items: IItemDeCompra[];
}
```

### IItemDeCompra
```typescript
interface IItemDeCompra {
  recno: string;
  item: string;
  status: string;
  sb1_recno: number;
  product: string;
  quantity: number;
  needDate: string;
  observations: string;
  ctt_recno: string;
  centro_de_custo: string;
  ctj_recno: number;
  rateio: string;
}
```

## API Endpoints

### Carregar Dados da Solicitação
```
GET /solicitacoes/compras/{id}
```

### Atualizar Solicitação
```
PUT /solicitacoes/compras/{id}
```

## Fluxo de Edição

1. **Usuário clica em "Editar" na tabela de solicitações**
2. **Navegação para página de edição** com dados da solicitação
3. **Carregamento do formulário** com dados preenchidos
4. **Usuário edita os campos** desejados
5. **Submissão** envia requisição PUT para API
6. **Feedback** de sucesso/erro para o usuário
7. **Retorno** para lista de solicitações

## Considerações Importantes

- Apenas solicitações com status "Solicitação Pendente" podem ser editadas
- O formulário preserva todos os campos originais quando carregado
- A validação é a mesma para criação e edição
- O sistema diferencia visualmente entre modo de criação e edição
- Erros de carregamento são tratados graciosamente

## Exemplo de Rota

Para usar a página de edição, adicione a rota no seu roteador:

```tsx
import EditRequest from '@/pages/EditRequest';

// No seu roteador
<Route path="/editar-solicitacao/:id" element={<EditRequest />} />
```

