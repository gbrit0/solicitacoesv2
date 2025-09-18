// src/pages/PaginaEdicaoSolicitacao.tsx

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useToast } from "@/hooks/use-toast";
import http from '@/http/index';

// Importe seus componentes de UI
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Trash } from 'lucide-react';

// Crie interfaces para os dados que você vai buscar
interface IItemSolicitacao {
  recno: number;
  item: string;
  product: string; // Este será o código do produto
  quantity: number;
  needDate: string;
  observations: string;
  // Adicione outros campos como centro de custo, rateio, etc.
}

interface ISolicitacaoCompleta {
  sc: string;
  requester: string;
  requestDate: string;
  // Adicione outros campos do cabeçalho aqui
  items: IItemSolicitacao[];
}

interface IProduto {
  codigo: string;
  descricao: string;
}

interface ICentroCusto {
    id: string;
    nome: string;
}

const PaginaEdicaoSolicitacao: React.FC = () => {
  const { sc } = useParams<{ sc: string }>(); // Pega o 'sc' da URL
  const navigate = useNavigate();
  const { toast } = useToast();

  // Estado para armazenar os dados da solicitação que está sendo editada
  const [solicitacao, setSolicitacao] = useState<ISolicitacaoCompleta | null>(null);
  
  // Estados para as listas que preencherão os <Select>
  const [produtos, setProdutos] = useState<IProduto[]>([]);
  const [centrosDeCusto, setCentrosDeCusto] = useState<ICentroCusto[]>([]);
  // const [rateios, setRateios] = useState<IRateio[]>([]); // Se precisar

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!sc) return;

    const carregarDadosIniciais = async () => {
      try {
        setLoading(true);

        // Use Promise.all para buscar tudo em paralelo
        const [
          respostaSolicitacao, 
          respostaProdutos, 
          respostaCentrosCusto
        ] = await Promise.all([
          http.get(`/solicitacoes/${sc}`), // Endpoint para buscar UMA solicitação
          http.get('/produtos'),            // Endpoint para buscar TODOS os produtos
          http.get('/centros-de-custo')     // Endpoint para buscar os centros de custo
        ]);

        setSolicitacao(respostaSolicitacao.data);
        setProdutos(respostaProdutos.data);
        setCentrosDeCusto(respostaCentrosCusto.data);

      } catch (error) {
        console.error("Erro ao carregar dados para edição:", error);
        toast({
          title: "Erro ao carregar dados",
          description: "Não foi possível encontrar os dados da solicitação.",
          variant: "destructive"
        });
        navigate('/lista_de_solicitacoes'); // Volta para a lista se der erro
      } finally {
        setLoading(false);
      }
    };

    carregarDadosIniciais();
  }, [sc, navigate, toast]);

  const handleItemChange = (index: number, field: keyof IItemSolicitacao, value: any) => {
    if (!solicitacao) return;

    const novosItens = [...solicitacao.items];
    novosItens[index] = { ...novosItens[index], [field]: value };

    setSolicitacao({ ...solicitacao, items: novosItens });
  };

  const adicionarItem = () => {
    if (!solicitacao) return;
    
    const novoItem: IItemSolicitacao = {
      recno: Date.now(), // ID temporário
      item: String(solicitacao.items.length + 1).padStart(2, '0'),
      product: '',
      quantity: 1,
      needDate: '',
      observations: '',
    };

    setSolicitacao({ ...solicitacao, items: [...solicitacao.items, novoItem] });
  };

  const removerItem = (index: number) => {
    if (!solicitacao) return;
    const novosItens = solicitacao.items.filter((_, i) => i !== index);
    setSolicitacao({ ...solicitacao, items: novosItens });
  };
  
  const handleSave = async () => {
    // Lógica para enviar o objeto 'solicitacao' atualizado para a API
    try {
        await http.put(`/solicitacoes/${sc}`, solicitacao);
        toast({ title: "Sucesso!", description: `Solicitação ${sc} atualizada.` });
        navigate('/lista_de_solicitacoes');
    } catch (error) {
        toast({ title: "Erro", description: "Não foi possível salvar as alterações.", variant: "destructive" });
    }
  }

  if (loading) {
    return <div>Carregando...</div>;
  }

  if (!solicitacao) {
    return <div>Solicitação não encontrada.</div>;
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Editando Solicitação de Compra - SC: {solicitacao.sc}</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Renderiza o cabeçalho aqui, se necessário */}
        <div>
            <p><strong>Solicitante:</strong> {solicitacao.requester}</p>
            <p><strong>Data:</strong> {solicitacao.requestDate}</p>
        </div>

        {/* Mapeia os itens da solicitação */}
        {solicitacao.items.map((item, index) => (
          <div key={item.recno} className="grid grid-cols-6 gap-4 items-end p-4 border rounded-md">
            {/* Coluna Produto (com Select) */}
            <div className="col-span-2">
              <label>Produto</label>
              <Select 
                value={item.product} 
                onValueChange={(value) => handleItemChange(index, 'product', value)}
              >
                <SelectTrigger><SelectValue placeholder="Selecione um produto..." /></SelectTrigger>
                <SelectContent>
                  {produtos.map(p => (
                    <SelectItem key={p.codigo} value={p.codigo}>{p.descricao}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            
            {/* Coluna Quantidade */}
            <div>
              <label>Quantidade</label>
              <Input 
                type="number"
                value={item.quantity}
                onChange={(e) => handleItemChange(index, 'quantity', Number(e.target.value))}
              />
            </div>
            
            {/* Coluna Data Necessidade */}
            <div>
              <label>Data Nec.</label>
              <Input 
                type="date"
                value={item.needDate}
                onChange={(e) => handleItemChange(index, 'needDate', e.target.value)}
              />
            </div>
            
            {/* Outros campos como Centro de Custo... */}
            {/* ... */}
            
            {/* Botão Remover */}
            <div className="flex items-end">
                <Button variant="outline" size="icon" onClick={() => removerItem(index)}>
                    <Trash className="h-4 w-4" />
                </Button>
            </div>
          </div>
        ))}
        
        <div className="flex justify-between mt-6">
            <Button variant="outline" onClick={adicionarItem}>Adicionar Item</Button>
            <Button onClick={handleSave}>Salvar Alterações</Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default PaginaEdicaoSolicitacao;