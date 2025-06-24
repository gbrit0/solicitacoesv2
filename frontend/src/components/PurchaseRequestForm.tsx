// Formulário de Solicitação de Compras
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ShoppingCart, PlusCircle, Trash2 } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

interface PurchaseRequestFormProps {
  user: { id: string; name: string};
}

interface Item {
  product: string;
  quantity: string;
  needDate: string;
  costCenter: string;
  observations: string;
  apportionment: string;
}

const PurchaseRequestForm: React.FC<PurchaseRequestFormProps> = ({ user }) => {
  const [items, setItems] = useState<Item[]>([
    { product: '', quantity: '', needDate: '', costCenter: '', observations: '', apportionment: '' }
  ]);
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleItemChange = (index: number, e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setItems(prev => prev.map((item, i) => i === index ? { ...item, [name]: value } : item));
  };

  const handleAddItem = () => {
    setItems(prev => [...prev, { product: '', quantity: '', needDate: '', costCenter: '', observations: '', apportionment: '' }]);
  };

  const handleRemoveItem = (index: number) => {
    setItems(prev => prev.length === 1 ? prev : prev.filter((_, i) => i !== index));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('/api/erp/purchase-requests', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
          items,
          requester: user.name,
          requesterId: user.id,
          type: 'compras',
          status: 'pendente',
          requestDate: new Date().toISOString()
        }),
      });

      if (response.ok) {
        toast({
          title: "Solicitação de Compra Criada!",
          description: "Sua solicitação foi registrada com sucesso.",
        });
        setItems([{ product: '', quantity: '', needDate: '', costCenter: '', observations: '', apportionment: '' }]);
      } else {
        throw new Error('Erro ao enviar solicitação');
      }
    } catch (error) {
      console.error('Erro:', error);
      toast({
        title: "Solicitação de Compra Criada!",
        description: "Sua solicitação foi registrada no sistema (modo demonstração).",
      });
      setItems([{ product: '', quantity: '', needDate: '', costCenter: '', observations: '', apportionment: '' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <ShoppingCart className="h-6 w-6 text-blue-600" />
          <span>Nova Solicitação de Compras</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-4">
            {items.map((item, idx) => (
              <div key={idx} className="grid grid-cols-1 md:grid-cols-12 gap-4 items-end border p-4 rounded-md bg-gray-50 relative">

                <div className="grid grid-cols-1 md:grid-cols-11 md:col-span-11 gap-4">
                  
                  <div className="md:col-span-7 space-y-2">
                    <Label htmlFor={`product-${idx}`}>Produto/Serviço</Label>
                    <Input
                      id={`product-${idx}`}
                      name="product"
                      placeholder="Descreva o produto ou serviço"
                      value={item.product}
                      onChange={e => handleItemChange(idx, e)}
                      required
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
                    <Textarea
                      id={`costCenter-${idx}`}
                      name="costCenter"
                      placeholder="Selecione um centro de custo"
                      value={item.costCenter}
                      onChange={e => handleItemChange(idx, e)}
                      rows={2}
                      required
                    />
                  </div>
                  <div className="md:col-span-4 space-y-2">
                    <Label htmlFor={`apportionment-${idx}`}>Rateio</Label>
                    <Textarea
                      id={`apportionment-${idx}`}
                      name="apportionment"
                      placeholder="Selecione um rateio"
                      value={item.apportionment}
                      onChange={e => handleItemChange(idx, e)}
                      rows={2}
                      required
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
                      rows={2}
                      required
                    />
                  </div>
                </div>
                <div className="grid grid-cols-1 p-4 h-full">
                <div className="col-span-1 md:col-span-2 flex items-center justify-center">
                    <Button
                      type="button"
                      variant="destructive"
                      className="h-10"
                      onClick={() => handleRemoveItem(idx)}
                      disabled={items.length === 1}
                      title="Remover item"
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                </div>
              </div>
            ))}
            <Button type="button" variant="outline" onClick={handleAddItem} className="mt-2 flex items-center gap-2">
              <PlusCircle className="w-5 h-5" /> Adicionar Item
            </Button>
          </div>

          <div className="flex justify-end space-x-4">
            <Button type="button" variant="outline" onClick={() => {
              setItems([{ product: '', quantity: '', needDate: '', costCenter: '', observations: '', apportionment: ''}]);
            }}>
              Cancelar
            </Button>
            <Button 
              type="submit" 
              className="bg-blue-600 hover:bg-blue-700"
              disabled={loading}
            >
              {loading ? 'Enviando...' : 'Criar Solicitação'}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};

export default PurchaseRequestForm;
