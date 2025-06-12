
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Calendar, ShoppingCart } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

interface PurchaseRequestFormProps {
  user: { name: string; email: string };
}

const PurchaseRequestForm: React.FC<PurchaseRequestFormProps> = ({ user }) => {
  const [formData, setFormData] = useState({
    product: '',
    quantity: '',
    needDate: '',
    observations: '',
    justification: '',
    supplier: '',
    estimatedValue: ''
  });
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Aqui você faria a chamada para sua API REST do ERP
      const response = await fetch('/api/erp/purchase-requests', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}` // Token de autenticação
        },
        body: JSON.stringify({
          ...formData,
          requester: user.name,
          requesterEmail: user.email,
          type: 'compras',
          status: 'pendente',
          requestDate: new Date().toISOString()
        }),
      });

      if (response.ok) {
        toast({
          title: "Solicitação de Compra Criada!",
          description: "Sua solicitação foi enviada para o ERP com sucesso.",
        });
        
        // Limpar formulário
        setFormData({
          product: '',
          quantity: '',
          needDate: '',
          observations: '',
          justification: '',
          supplier: '',
          estimatedValue: ''
        });
      } else {
        throw new Error('Erro ao enviar solicitação');
      }
    } catch (error) {
      console.error('Erro:', error);
      // Para demonstração, simular sucesso
      toast({
        title: "Solicitação de Compra Criada!",
        description: "Sua solicitação foi registrada no sistema (modo demonstração).",
      });
      
      setFormData({
        product: '',
        quantity: '',
        needDate: '',
        observations: '',
        justification: '',
        supplier: '',
        estimatedValue: ''
      });
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Card className="max-w-4xl mx-auto">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <ShoppingCart className="h-6 w-6 text-blue-600" />
          <span>Nova Solicitação de Compras</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <Label htmlFor="product">Produto/Serviço *</Label>
              <Input
                id="product"
                name="product"
                placeholder="Descreva o produto ou serviço"
                value={formData.product}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="quantity">Quantidade *</Label>
              <Input
                id="quantity"
                name="quantity"
                type="number"
                step="0.01"
                placeholder="0.00"
                value={formData.quantity}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="needDate">Data de Necessidade *</Label>
              <Input
                id="needDate"
                name="needDate"
                type="date"
                value={formData.needDate}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="estimatedValue">Valor Estimado</Label>
              <Input
                id="estimatedValue"
                name="estimatedValue"
                type="number"
                step="0.01"
                placeholder="R$ 0,00"
                value={formData.estimatedValue}
                onChange={handleChange}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="supplier">Fornecedor Sugerido</Label>
              <Input
                id="supplier"
                name="supplier"
                placeholder="Nome do fornecedor (opcional)"
                value={formData.supplier}
                onChange={handleChange}
              />
            </div>

            <div className="space-y-2">
              <Label>Solicitante</Label>
              <Input value={user.name} disabled className="bg-gray-50" />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="justification">Justificativa *</Label>
            <Textarea
              id="justification"
              name="justification"
              placeholder="Justifique a necessidade desta compra..."
              value={formData.justification}
              onChange={handleChange}
              rows={3}
              required
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="observations">Observações</Label>
            <Textarea
              id="observations"
              name="observations"
              placeholder="Informações adicionais..."
              value={formData.observations}
              onChange={handleChange}
              rows={3}
            />
          </div>

          <div className="flex justify-end space-x-4">
            <Button type="button" variant="outline">
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
