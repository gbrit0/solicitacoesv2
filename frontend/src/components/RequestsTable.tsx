import React, { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Edit, Trash, Calendar, Filter, Search } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";

interface Request {
  id: string;
  type: 'compras' | 'almoxarifado';
  status: 'pendente' | 'aprovado' | 'rejeitado';
  requester: string;
  product: string;
  quantity: number;
  requestDate: string;
  needDate: string;
  observations: string;
  issueDate: string;
}

const RequestsTable: React.FC = () => {
  const [requests, setRequests] = useState<Request[]>([]);
  const [filteredRequests, setFilteredRequests] = useState<Request[]>([]);
  const [filters, setFilters] = useState({
    startDate: '',
    endDate: '',
    user: '',
    status: 'todos',
    type: 'todos'
  });
  const [searchTerm, setSearchTerm] = useState('');
  const { toast } = useToast();

  useEffect(() => {
    // Simular dados das solicitações
    const mockRequests: Request[] = [
      {
        id: '076477',
        type: 'compras',
        status: 'pendente',
        requester: 'Gabriel Brito Ribeiro',
        product: 'COXIM R-073',
        quantity: 23,
        requestDate: '09/04/2025',
        needDate: '24/04/2025',
        observations: 'Teste',
        issueDate: '09/04/2025'
      },
      {
        id: '076478',
        type: 'almoxarifado',
        status: 'aprovado',
        requester: 'Gabriel Brito Ribeiro',
        product: 'TERMINAL DE COMPRESSAO 70MM',
        quantity: 54,
        requestDate: '09/04/2025',
        needDate: '24/04/2025',
        observations: 'Teste',
        issueDate: '09/04/2025'
      },
      {
        id: '076479',
        type: 'compras',
        status: 'rejeitado',
        requester: 'Gabriel Brito Ribeiro',
        product: 'CURVA 90° ACO CARB SOLDAVEL 4"',
        quantity: 2,
        requestDate: '09/04/2025',
        needDate: '30/04/2025',
        observations: 'Teste',
        issueDate: '09/04/2025'
      }
    ];
    setRequests(mockRequests);
    setFilteredRequests(mockRequests);
  }, []);

  useEffect(() => {
    let filtered = requests;

    // Filtro por data
    if (filters.startDate) {
      filtered = filtered.filter(req => new Date(req.requestDate.split('/').reverse().join('-')) >= new Date(filters.startDate));
    }
    if (filters.endDate) {
      filtered = filtered.filter(req => new Date(req.requestDate.split('/').reverse().join('-')) <= new Date(filters.endDate));
    }

    // Filtro por usuário
    if (filters.user) {
      filtered = filtered.filter(req => req.requester.toLowerCase().includes(filters.user.toLowerCase()));
    }

    // Filtro por status
    if (filters.status && filters.status !== 'todos') {
      filtered = filtered.filter(req => req.status === filters.status);
    }

    // Filtro por tipo
    if (filters.type && filters.type !== 'todos') {
      filtered = filtered.filter(req => req.type === filters.type);
    }

    // Filtro por termo de pesquisa
    if (searchTerm) {
      filtered = filtered.filter(req => 
        req.product.toLowerCase().includes(searchTerm.toLowerCase()) ||
        req.id.includes(searchTerm) ||
        req.requester.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    setFilteredRequests(filtered);
  }, [requests, filters, searchTerm]);

  const handleEdit = (id: string) => {
    toast({
      title: "Editar Solicitação",
      description: `Editando solicitação ${id}`,
    });
  };

  const handleDelete = (id: string) => {
    setRequests(prev => prev.filter(req => req.id !== id));
    toast({
      title: "Solicitação Excluída",
      description: `Solicitação ${id} foi excluída com sucesso.`,
    });
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'pendente': return 'bg-yellow-500';
      case 'aprovado': return 'bg-green-500';
      case 'rejeitado': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  };

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'compras': return 'bg-blue-500';
      case 'almoxarifado': return 'bg-purple-500';
      default: return 'bg-gray-500';
    }
  };

  return (
    <div className="space-y-6">
      {/* Filtros */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Filter className="h-5 w-5" />
            <span>Filtros</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
            <div className="space-y-2">
              <Label htmlFor="startDate">Data Início</Label>
              <Input
                id="startDate"
                type="date"
                value={filters.startDate}
                onChange={(e) => setFilters(prev => ({ ...prev, startDate: e.target.value }))}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="endDate">Data Fim</Label>
              <Input
                id="endDate"
                type="date"
                value={filters.endDate}
                onChange={(e) => setFilters(prev => ({ ...prev, endDate: e.target.value }))}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="user">Usuário</Label>
              <Input
                id="user"
                placeholder="Nome do usuário"
                value={filters.user}
                onChange={(e) => setFilters(prev => ({ ...prev, user: e.target.value }))}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="status">Status</Label>
              <Select value={filters.status} onValueChange={(value) => setFilters(prev => ({ ...prev, status: value }))}>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione..." />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="todos">Todos</SelectItem>
                  <SelectItem value="pendente">Pendente</SelectItem>
                  <SelectItem value="aprovado">Aprovado</SelectItem>
                  <SelectItem value="rejeitado">Rejeitado</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="type">Tipo</Label>
              <Select value={filters.type} onValueChange={(value) => setFilters(prev => ({ ...prev, type: value }))}>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione..." />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="todos">Todos</SelectItem>
                  <SelectItem value="compras">Compras</SelectItem>
                  <SelectItem value="almoxarifado">Almoxarifado</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
          <div className="mt-4">
            <div className="relative">
              <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
              <Input
                placeholder="Pesquisar por produto, ID ou solicitante..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10"
              />
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Tabela */}
      <Card>
        <CardHeader>
          <CardTitle>Lista de Solicitações</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <table className="w-full border-collapse">
              <thead>
                <tr className="border-b bg-gray-50">
                  <th className="text-left p-3 font-medium">Status</th>
                  <th className="text-left p-3 font-medium">ID</th>
                  <th className="text-left p-3 font-medium">Tipo</th>
                  <th className="text-left p-3 font-medium">Solicitante</th>
                  <th className="text-left p-3 font-medium">Produto</th>
                  <th className="text-left p-3 font-medium">Quantidade</th>
                  <th className="text-left p-3 font-medium">Data de Necessidade</th>
                  <th className="text-left p-3 font-medium">Observações</th>
                  <th className="text-left p-3 font-medium">Emissão</th>
                  <th className="text-left p-3 font-medium">Ações</th>
                </tr>
              </thead>
              <tbody>
                {filteredRequests.map((request) => (
                  <tr key={request.id} className="border-b hover:bg-gray-50">
                    <td className="p-3">
                      <div className={`w-4 h-4 rounded-full ${getStatusColor(request.status)}`} title={request.status}></div>
                    </td>
                    <td className="p-3 font-mono">{request.id}</td>
                    <td className="p-3">
                      <Badge className={`${getTypeColor(request.type)} text-white`}>
                        {request.type === 'compras' ? 'Compras' : 'Almoxarifado'}
                      </Badge>
                    </td>
                    <td className="p-3">{request.requester}</td>
                    <td className="p-3">{request.product}</td>
                    <td className="p-3">{request.quantity.toFixed(2)}</td>
                    <td className="p-3">{request.needDate}</td>
                    <td className="p-3">{request.observations}</td>
                    <td className="p-3">{request.issueDate}</td>
                    <td className="p-3">
                      <div className="flex space-x-2">
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleEdit(request.id)}
                          className="h-8 w-8 p-0"
                        >
                          <Edit className="h-4 w-4" />
                        </Button>
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleDelete(request.id)}
                          className="h-8 w-8 p-0 text-red-600 hover:text-red-700"
                        >
                          <Trash className="h-4 w-4" />
                        </Button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          {filteredRequests.length === 0 && (
            <div className="text-center py-8 text-gray-500">
              Nenhuma solicitação encontrada com os filtros aplicados.
            </div>
          )}

          <div className="mt-4 flex justify-between items-center text-sm text-gray-600">
            <span>Mostrando {filteredRequests.length} de {requests.length} registros</span>
            <div className="flex space-x-2">
              <Button variant="outline" size="sm" disabled>Anterior</Button>
              <Button variant="outline" size="sm" className="bg-blue-600 text-white">1</Button>
              <Button variant="outline" size="sm" disabled>Próximo</Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default RequestsTable;
