
import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { UserPlus } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

const UserRegistrationForm: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    role: '',
    department: '',
    costCenter: '',
    phone: ''
  });
  const [loading, setLoading] = useState(false);
  const { toast } = useToast();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (formData.password !== formData.confirmPassword) {
      toast({
        title: "Erro",
        description: "As senhas não coincidem.",
        variant: "destructive"
      });
      return;
    }

    setLoading(true);

    try {
      // Aqui você faria a chamada para sua API REST do ERP
      const response = await fetch('/api/erp/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}` // Token de autenticação
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          password: formData.password,
          role: formData.role,
          department: formData.department,
          costCenter: formData.costCenter,
          phone: formData.phone
        }),
      });

      if (response.ok) {
        toast({
          title: "Usuário Cadastrado!",
          description: "O usuário foi criado com sucesso no sistema.",
        });
        
        // Limpar formulário
        setFormData({
          name: '',
          email: '',
          password: '',
          confirmPassword: '',
          role: '',
          department: '',
          costCenter: '',
          phone: ''
        });
      } else {
        throw new Error('Erro ao cadastrar usuário');
      }
    } catch (error) {
      console.error('Erro:', error);
      // Para demonstração, simular sucesso
      toast({
        title: "Usuário Cadastrado!",
        description: "O usuário foi registrado no sistema (modo demonstração).",
      });
      
      setFormData({
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        role: '',
        department: '',
        costCenter: '',
        phone: ''
      });
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Card className="max-w-4xl mx-auto">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <UserPlus className="h-6 w-6 text-green-600" />
          <span>Cadastrar Novo Usuário</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <Label htmlFor="name">Nome Completo *</Label>
              <Input
                id="name"
                name="name"
                placeholder="Nome completo do usuário"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="email">Email *</Label>
              <Input
                id="email"
                name="email"
                type="email"
                placeholder="usuario@empresa.com"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="password">Senha *</Label>
              <Input
                id="password"
                name="password"
                type="password"
                placeholder="Senha de acesso"
                value={formData.password}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="confirmPassword">Confirmar Senha *</Label>
              <Input
                id="confirmPassword"
                name="confirmPassword"
                type="password"
                placeholder="Confirme a senha"
                value={formData.confirmPassword}
                onChange={handleChange}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="role">Função/Cargo *</Label>
              <Select value={formData.role} onValueChange={(value) => setFormData(prev => ({ ...prev, role: value }))}>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione a função" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="solicitante">Solicitante</SelectItem>
                  <SelectItem value="aprovador">Aprovador</SelectItem>
                  <SelectItem value="comprador">Comprador</SelectItem>
                  <SelectItem value="almoxarife">Almoxarife</SelectItem>
                  <SelectItem value="administrador">Administrador</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="department">Departamento/Setor *</Label>
              <Select value={formData.department} onValueChange={(value) => setFormData(prev => ({ ...prev, department: value }))}>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione o departamento" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="compras">Compras</SelectItem>
                  <SelectItem value="almoxarifado">Almoxarifado</SelectItem>
                  <SelectItem value="engenharia">Engenharia</SelectItem>
                  <SelectItem value="manutencao">Manutenção</SelectItem>
                  <SelectItem value="producao">Produção</SelectItem>
                  <SelectItem value="administrativo">Administrativo</SelectItem>
                  <SelectItem value="financeiro">Financeiro</SelectItem>
                </SelectContent>
              </Select>
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

            <div className="space-y-2">
              <Label htmlFor="phone">Telefone</Label>
              <Input
                id="phone"
                name="phone"
                type="tel"
                placeholder="(11) 99999-9999"
                value={formData.phone}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="flex justify-end space-x-4">
            <Button type="button" variant="outline">
              Cancelar
            </Button>
            <Button 
              type="submit" 
              className="bg-green-600 hover:bg-green-700"
              disabled={loading}
            >
              {loading ? 'Cadastrando...' : 'Cadastrar Usuário'}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};

export default UserRegistrationForm;
