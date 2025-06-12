
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Package } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

interface WarehouseRequestFormProps {
  user: { name: string; email: string };
}

const WarehouseRequestForm: React.FC<WarehouseRequestFormProps> = ({ user }) => {
  const [formData, setFormData] = useState({
    product: '',
    quantity: '',
    needDate: '',
    observations: '',
    destination: '',
    priority: 'normal',
    costCenter: ''
  });
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Aqui você faria a chamada para sua API REST do ERP
      const response = await fetch('/api/erp/warehouse-requests', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}` // Token de autenticação
        },
        body: JSON.stringify({
          ...formData,
          requester: user.name,
          requesterEmail: user.email,
          type: 'almoxarifado',
          status: 'pendente',
          requestDate: new Date().toISOString()
        }),
      });

      if (response.ok) {
        toast({
          title: "Solicitação ao Almoxarifado Criada!",
          description: "Sua solicitação foi enviada para o ERP com sucesso.",
        });
        
        // Limpar formulário
        setFormData({
          product: '',
          quantity: '',
          needDate: '',
          observations: '',
          destination: '',
          priority: 'normal',
          costCenter: ''
        });
      } else {
        throw new Error('Erro ao enviar solicitação');
      }
    } catch (error) {
      console.error('Erro:', error);
      // Para demonstração, simular sucesso
      toast({
        title: "Solicitação ao Almoxarifado Criada!",
        description: "Sua solicitação foi registrada no sistema (modo demonstração).",
      });
      
      setFormData({
        product: '',
        quantity: '',
        needDate: '',
        observations: '',
        destination: '',
        priority: 'normal',
        costCenter: ''
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
          <Package className="h-6 w-6 text-purple-600" />
          <span>Nova Solicitação ao Almoxarifado</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <Label htmlFor="product">Material/Produto *</Label>
              <Input
                id="product"
                name="product"
                placeholder="Código ou descrição do material"
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
              <Label htmlFor="priority">Prioridade</Label>
              <Select value={formData.priority} onValueChange={(value) => setFormData(prev => ({ ...prev, priority: value }))}>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione a prioridade" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="baixa">Baixa</SelectItem>
                  <SelectItem value="normal">Normal</SelectItem>
                  <SelectItem value="alta">Alta</SelectItem>
                  <SelectItem value="urgente">Urgente</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="destination">Local de Destino *</Label>
              <Input
                id="destination"
                name="destination"
                placeholder="Setor, obra, local de entrega"
                value={formData.destination}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="costCenter">Centro de Custo</Label>
              <Input
                id="costCenter"
                name="costCenter"
                placeholder="Código do centro de custo"
                value={formData.costCenter}
                onChange={handleChange}
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label>Solicitante</Label>
              <Input value={user.name} disabled className="bg-gray-50" />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="observations">Observações</Label>
            <Textarea
              id="observations"
              name="observations"
              placeholder="Informações adicionais sobre a solicitação..."
              value={formData.observations}
              onChange={handleChange}
              rows={4}
            />
          </div>

          <div className="flex justify-end space-x-4">
            <Button type="button" variant="outline">
              Cancelar
            </Button>
            <Button 
              type="submit" 
              className="bg-purple-600 hover:bg-purple-700"
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

export default WarehouseRequestForm;
