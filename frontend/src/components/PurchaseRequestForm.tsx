// Formulário de Solicitação de Compras
import React, { useEffect, useState } from 'react';
import Select from "react-select";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ShoppingCart, PlusCircle, Trash2 } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

import IProduto from '@/interfaces/IProduto';
import IRateio from '@/interfaces/IRateio';
import ICentroDeCusto from '@/interfaces/ICentroDeCusto';

import IListaDeSolicitacoes from '@/interfaces/IListaDeSolicitacoes';
import IItemDeCompra from '@/interfaces/IItemDeCompra';

import http from '@/http/index';

import { useLocation, useNavigate } from 'react-router-dom';
import { getDate } from 'date-fns';

interface User {
  id: number;
  name: string;
  email: string;
  nome: string;
  sobrenome: string;
}

interface PurchaseRequestFormProps {
  user: User;
}

const PurchaseRequestForm: React.FC<PurchaseRequestFormProps> = ({ user }) => {
  // NOVO: Hooks para rota
  const location = useLocation();
  const navigate = useNavigate();

  // NOVO: Extrai os dados da solicitação para editar. Se não houver, será 'undefined'.
  const requestToEdit = location.state?.requestData;
  
  // NOVO: Define se o formulário está em modo de edição
  const isEditMode = Boolean(requestToEdit);
  if (isEditMode){
    console.log(requestToEdit)
  }

  // Função para obter a data padrão (hoje + 15 dias)
  const getDefaultDate = () => {
    const today = new Date();
    today.setDate(today.getDate() + 15);
    return today.toISOString().split("T")[0]; // formata para YYYY-MM-DD
  };

  const [items, setItems] = useState<IListaDeSolicitacoes[]>([
    { 
        requestDate: new Date().toISOString(), 
        requester: '',
        sc: '',
        items: [
          {
            recno: null,
            item: '',
            status: '',
            product: '',
            quantity: null,
            needDate: getDefaultDate(),
            observations: '',
            costCenter: '',
            apportionment: ''
          },
        ]

     }
  ]);
  const [loading, setLoading] = useState(false);

  const [produtos, setProdutos] = useState<IProduto[]>([]);
  const [rateios, setRateios] = useState<IRateio[]>([]);
  const [centrosDeCusto, setCentrosDeCusto] = useState<ICentroDeCusto[]>([]);

  const { toast } = useToast();


  // Busca os produtos da API quando o componente é montado
  useEffect(() => {
    const fetchProdutos = async () => {
      try {
        const response = await http.get(`/produtos`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
          }
        });
        setProdutos(response.data.data);
        // console.log("Produtos carregados:", response.data.data);
      } catch (error) {
        console.error("Erro ao buscar produtos:", error);
        toast({
            title: "Erro ao buscar produtos",
            description: "Não foi possível carregar a lista de produtos. Contate o administrador!",
            variant: "destructive"
        });
      }
    };

    const fecthRateios = async () => {
      try {
        const response = await http.get(`/rateios`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
          }
        });
        setRateios(response.data.rateios);
        // console.log("Rateios carregados:", response.data.rateios);
      } catch (error) {
        console.error("Erro ao buscasr rateios:", error);
        toast({
          title: "Erro ao buscar rateios",
          description: "Não foi possível carregar a lista de rateios. Contate o administrador!",
          variant: "destructive"
        })
      }
    }
    

    const fecthCentrosDeCusto = async () => {
      try {
        const response = await http.get(`/centros_de_custo`, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
          }
        });
        setCentrosDeCusto(response.data.centrosDeCusto);
        // console.log("Centros de Custo carregados:", response.data.centrosDeCusto);
      } catch (error) {
        console.error("Erro ao buscasr rateios:", error);
        toast({
          title: "Erro ao buscar centros de custo",
          description: "Não foi possível carregar a lista de centros de custo. Contate o administrador!",
          variant: "destructive"
        })
      }
    }

    fetchProdutos();
    fecthRateios();
    fecthCentrosDeCusto();

  }, [toast]); // Adicionado toast como dependência

  useEffect(() => {
    if (isEditMode && requestToEdit.items) {
      // Preenche o estado 'items' com os dados da solicitação a ser editada
      // Certifique-se que a estrutura dos dados bate com a interface 'Item'
      setItems(requestToEdit.items);
    }
  }, [isEditMode, requestToEdit]); // Roda apenas quando esses valores mudarem

  const handleItemChange = (index: number, e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setItems(prev => prev.map((item, i) => i === index ? { ...item, [name]: value } : item));
  };

  const handleAddItem = () => {
    setItems(prev => [...prev, { product: '', quantity: '', needDate: getDefaultDate(), costCenter: '', observations: '', apportionment: '' }]);
  };

  const handleRemoveItem = (index: number) => {
    setItems(prev => prev.length === 1 ? prev : prev.filter((_, i) => i !== index));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    const requestData = {
      items,
      requester: user.name,
      requesterId: user.id,
      type: 'compras',
      status: 'pendente',
      requestDate: new Date().toISOString()
    };

    try {
      let response;
      if (isEditMode) {
        // LÓGICA DE EDIÇÃO
        response = await fetch(`/api/erp/purchase-requests/${requestToEdit.solicitacao}`, { // URL com o ID
          method: 'PUT', // Método PUT para atualizar
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify(requestData),
        });
      } else {
        // LÓGICA DE CRIAÇÃO (a que você já tinha)
        response = await fetch('/api/erp/purchase-requests', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify(requestData),
        });
        response = http.post('/solicitacoes/compras', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
          }
        })
      }

      if (response.ok) {
        toast({
          title: isEditMode ? "Solicitação Atualizada!" : "Solicitação Criada!",
          description: `Sua solicitação foi ${isEditMode ? 'atualizada' : 'registrada'} com sucesso.`,
        });
        // Após sucesso, volta para a página da lista
        navigate('/solicitacoes'); 
      } else {
        throw new Error(isEditMode ? 'Erro ao atualizar solicitação' : 'Erro ao enviar solicitação');
      }
    } catch (error) {
      console.error('Erro:', error);
      toast({
        title: "Erro na Operação",
        description: "Não foi possível salvar a solicitação. Tente novamente.",
        variant: "destructive"
      });
    } finally {
      setLoading(false);
    }
  };

  const productOptions = produtos.map(p => ({
    value: p.sb1_recno,
    label: p.produto,
  }));
  
  const rateiosOptions = rateios.map(p => ({
    value: p.rateio,
    label: p.descricao,
  }));
  
  const centroDeCustoOptions = centrosDeCusto.map(p => ({
    value: p.ctt_recno,
    label: p.centro_de_custo,
  }));

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <ShoppingCart className="h-5 w-5 text-blue-600" />
            <span>
              {isEditMode ? `Editando Solicitação #${requestToEdit.sc}` : 'Nova Solicitação de Compras'}
            </span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-4">
              {items.map((item, idx) => (
                <div key={idx} className="grid grid-cols-1 md:grid-cols-12 gap-4 items-start border p-4 rounded-lg bg-gray-50/50 relative">

                  <div className="grid grid-cols-1 md:grid-cols-11 md:col-span-11 gap-4">

                    <div className="md:col-span-7 space-y-2">
                      <Label htmlFor={`product-${idx}`}>Produto/Serviço</Label>
                      <Select
                        inputId={`product-${idx}`}
                        name="product"
                        options={productOptions}
                        value={productOptions.find(opt => opt.value === item.product) || null}
                        onChange={(selectedOption) =>
                          setItems((prev) =>
                            prev.map((it, i) =>
                              i === idx ? { ...it, product: selectedOption?.value || "" } : it
                            )
                          )
                        }
                        placeholder="Selecione ou pesquise um produto..."
                        isClearable
                        isSearchable
                        noOptionsMessage={() => "Nenhum produto encontrado"}
                      />
                    </div>
                    <div className="md:col-span-2 space-y-2">
                      <Label htmlFor={`quantity-${idx}`}>Quantidade</Label>
                      <Input
                        id={`quantity-${idx}`}
                        name="quantity"
                        type="number"
                        step="0.01"
                        placeholder="0.00"
                        value={item.quantity}
                        onChange={e => handleItemChange(idx, e)}
                        required
                      />
                    </div>
                    <div className="md:col-span-2 space-y-2">
                      <Label htmlFor={`needDate-${idx}`}>Data de Necessidade</Label>
                      <Input
                        id={`needDate-${idx}`}
                        name="needDate"
                        type="date"
                        value={item.needDate}
                        onChange={e => handleItemChange(idx, e)}
                        required
                      />
                    </div>
                    <div className="md:col-span-4 space-y-2">
                      <Label htmlFor={`costCenter-${idx}`}>Centro de Custo</Label>
                      <Select
                        inputId={`costCenter-${idx}`}
                        name="costCenter"
                        options={centroDeCustoOptions}
                        value={centroDeCustoOptions.find(opt => opt.value === item.costCenter) || null} // Use item.costCenter
                        onChange={(selectedOption) =>
                          setItems((prev) =>
                            prev.map((it, i) =>
                              i === idx ? { ...it, costCenter: selectedOption?.value || "" } : it // Mude costCenter
                            )
                          )
                        }
                        placeholder="Selecione ou pesquise um centro de custos..."
                        isClearable
                        isSearchable
                        noOptionsMessage={() => "Nenhum centro de custo encontrado"}
                      />
                    </div>
                    <div className="md:col-span-4 space-y-2">
                      <Label htmlFor={`apportionment-${idx}`}>Rateio</Label>
                      <Select
                        inputId={`apportionment-${idx}`}
                        name="apportionment"
                        options={rateiosOptions}
                        value={rateiosOptions.find(opt => opt.value === item.apportionment) || null} // Use item.apportionment
                        onChange={(selectedOption) =>
                          setItems((prev) =>
                            prev.map((it, i) =>
                              i === idx ? { ...it, apportionment: selectedOption?.value || "" } : it // Mude apportionment
                            )
                          )
                        }
                        placeholder="Selecione ou pesquise um rateio..."
                        isClearable
                        isSearchable
                        noOptionsMessage={() => "Nenhum rateio encontrado"}
                      />
                    </div>
                    <div className="md:col-span-3 space-y-2">
                      <Label htmlFor={`observations-${idx}`}>Observações</Label>
                      <Textarea
                        id={`observations-${idx}`}
                        name="observations"
                        placeholder="Informações adicionais..."
                        value={item.observations}
                        onChange={e => handleItemChange(idx, e)}
                        rows={1}
                      />
                    </div>
                  </div>
                  <div className="md:col-span-1 flex items-center justify-center pt-6">
                    <Button
                      type="button"
                      variant="destructive"
                      size="icon"
                      onClick={() => handleRemoveItem(idx)}
                      disabled={items.length === 1}
                      title="Remover item"
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                </div>
              ))}
              <Button type="button" variant="outline" onClick={handleAddItem} className="mt-2 flex items-center gap-2">
                <PlusCircle className="w-5 h-5" /> Adicionar Item
              </Button>
            </div>

            <div className="flex justify-end space-x-4 pt-4">
              <Button type="button" variant="ghost" onClick={() => {
                setItems([{ product: '', quantity: '', needDate: getDefaultDate(), costCenter: '', observations: '', apportionment: '' }]);
                // setItems(isEditMode ? requestToEdit : [{ product: '', quantity: '', needDate: getDefaultDate(), costCenter: '', observations: '', apportionment: '' }]);
              }}>
                Cancelar
              </Button>
              <Button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700"
                disabled={loading}
              >
                {loading 
                  ? (isEditMode ? 'Salvando...' : 'Enviando...') 
                  : (isEditMode ? 'Salvar Alterações' : 'Criar Solicitação')
                }
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
    );
  };

export default PurchaseRequestForm;
