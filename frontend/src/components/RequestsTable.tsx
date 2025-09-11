import React, { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Edit, Trash, Filter, Search } from 'lucide-react';
import { useToast } from "@/hooks/use-toast";
import { useNavigate } from 'react-router-dom';

import IListaDeSolicitacoes from '@/interfaces/IListaDeSolicitacoes';

import http from '@/http/index';
import { Navigate } from 'react-router-dom';

const RequestsTable: React.FC = () => {
  const [requests, setRequests] = useState<IListaDeSolicitacoes[]>([]);
  const [filteredRequests, setFilteredRequests] = useState<IListaDeSolicitacoes[]>([]);
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
    const fetchSolicitacoes = async () => {
      try {
        const response = await http.get(`/solicitacoes`, {
          headers: {
            'accept':'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
          }
        });
        setRequests(response.data.solicitacoes);
        setFilteredRequests(response.data.solicitacoes);
        // console.log("Solicitações carregadas:", response.data.solicitacoes);
      } catch (error) {
        console.error("Erro ao buscar solicitacoes:", error);
        toast({
          title: "Erro ao buscar as solicitações",
          description: "Não foi possível carregar a lista de solicitações. Contate o administrador!",
          variant: "destructive"
        })
      }
    }
    
    fetchSolicitacoes();
  }, [toast]);

  useEffect(() => {
    setCurrentPage(1); // Volta para a página 1 quando os filtros mudam
  }, [filters, searchTerm]);

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

    // Filtro por termo de pesquisa
    if (searchTerm) {
      filtered = filtered.filter(req => 
        req.product.toLowerCase().includes(searchTerm.toLowerCase()) ||
        String(req.solicitacao).includes(searchTerm) ||
        String(req.requester).toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    setFilteredRequests(filtered);
  }, [requests, filters, searchTerm]);

  const navigate = useNavigate();
  
  const handleEdit = (request: IListaDeSolicitacoes) => {
    toast({
      title: "Editar Solicitação",
      description: `Editando solicitação ${request.solicitacao}`,
    });
    navigate('/solicitacao_de_compra', {
      state: { requestData: request }
    });
  };

  const handleDelete = (request: IListaDeSolicitacoes) => {
    setRequests(prev => prev.filter(req => req.solicitacao !== request.solicitacao));
    toast({
      title: "Solicitação Excluída",
      description: `Solicitação ${request.solicitacao} foi excluída com sucesso.`,
    });
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Solicitação Bloqueada': return 'bg-gray-500';
      case 'Solicitação Pendente': return 'bg-green-500';
      case 'Solicitação Totalmente Atendida': return 'bg-red-500';
      case 'Solicitação Parcialmente Atendida Utilizada em Cotação': return 'bg-red-300';
      case 'Solicitação Parcialmente Atendida': return 'bg-yellow-500';
      case 'Solicitação em Processo de Cotação': return 'bg-gray-800';
      case 'Solicitação de Produto Importado': return 'bg-purple-500';
      case 'Elim. por Resíduo': return 'bg-yellow-500';
      case 'Solicitação Rejeitada': return 'bg-orange-500';
      case 'Solicitação em Compra Centralizada': return 'bg-purple-800';
      default: return 'bg-gray-300';
    }
  };

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'compras': return 'bg-blue-500';
      case 'almoxarifado': return 'bg-purple-500';
      default: return 'bg-gray-500';
    }
  };

  const [currentPage, setCurrentPage] = useState(1);
  const ITEMS_PER_PAGE = 5;

  // Calcula o número total de páginas
  const totalPages = Math.ceil(filteredRequests.length / ITEMS_PER_PAGE);

  // Calcula o índice inicial e final dos itens para a página atual
  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const endIndex = startIndex + ITEMS_PER_PAGE;

  // Cria um novo array com apenas os itens da página atual
  const paginatedRequests = filteredRequests.slice(startIndex, endIndex);

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
          <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
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
                  <SelectItem value="Solicitação Bloqueada">Solicitação Bloqueada</SelectItem>
                  <SelectItem value="Solicitação Pendente">Solicitação Pendente</SelectItem>
                  <SelectItem value="Solicitação Totalmente Atendida">Solicitação Totalmente Atendida</SelectItem>
                  <SelectItem value="Solicitação Parcialmente Atendida Utilizada em Cotação">Solicitação Parcialmente Atendida Utilizada em Cotação</SelectItem>
                  <SelectItem value="Solicitação Parcialmente Atendida">Solicitação Parcialmente Atendida</SelectItem>
                  <SelectItem value="Solicitação em Processo de Cotação">Solicitação em Processo de Cotação</SelectItem>
                  <SelectItem value="Solicitação de Produto Importado">Solicitação de Produto Importado</SelectItem>
                  <SelectItem value="Elim. por Resíduo">Elim. por Resíduo</SelectItem>
                  <SelectItem value="Solicitação Rejeitada">Solicitação Rejeitada</SelectItem>
                  <SelectItem value="Solicitação em Compra Centralizada">Solicitação em Compra Centralizada</SelectItem>
                </SelectContent>
              </Select>
            </div>
            {/* <div className="space-y-2">
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
            </div> */}
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
              {/* ... seu thead continua o mesmo ... */}
              <thead>
                <tr className="border-b bg-gray-50">
                  <th className="text-left p-3 font-medium">Status</th>
                  <th className="text-left p-3 font-medium">ID</th>
                  <th className="text-left p-3 font-medium">Solicitante</th>
                  <th className="text-left p-3 font-medium">Produto</th>
                  <th className="text-left p-3 font-medium">Quantidade</th>
                  <th className="text-left p-3 font-medium">Data de Necessidade</th>
                  <th className="text-left p-3 font-medium">Observações</th>
                  <th className="text-left p-3 font-medium">Ações</th>
                </tr>
              </thead>
              <tbody>
                {/* ALTERADO: Mapeie 'paginatedRequests' em vez de 'filteredRequests' */}
                {paginatedRequests.map((request) => (
                  <tr key={request.solicitacao} className="border-b hover:bg-gray-50">
                    <td className="p-3">
                      <div className={`w-4 h-4 rounded-full ${getStatusColor(request.status)}`} title={request.status}></div>
                    </td>
                    <td className="p-3 font-mono">{request.solicitacao}</td>
                    <td className="p-3">{request.requester}</td>
                    <td className="p-3">{request.product}</td>
                    <td className="p-3">{request.quantity}</td>
                    <td className="p-3">{request.needDate}</td>
                    <td className="p-3">{request.observations}</td>
                    <td className="p-3">
                      <div className="flex space-x-2">
                        {/* <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleEdit(request.id)}
                          className="h-8 w-8 p-0"
                        >
                          <Edit className="h-4 w-4" />
                        </Button> */}
                        <Button // Somente editar solicitações pendentes
                          size="sm"
                          variant="outline"
                          onClick={() => handleEdit(request)} // Passe o objeto 'request' inteiro
                          className="h-8 w-8 p-0"
                          // Adicione a lógica de disabled aqui
                          disabled={request.status !== 'Solicitação Pendente'}
                          >
                          <Edit className="h-4 w-4" />
                        </Button>
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleDelete(request)}
                          className="h-8 w-8 p-0 text-red-600 hover:text-red-700"
                          disabled={request.status !== 'Solicitação Pendente'}
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

          {/* SEÇÃO DE PAGINAÇÃO ATUALIZADA */}
          <div className="mt-4 flex justify-between items-center text-sm text-gray-600">
            {/* Mostra a contagem de registros na página atual vs o total filtrado */}
            <span>Mostrando {paginatedRequests.length} de {filteredRequests.length} registros</span>

            <div className="flex space-x-2 items-center">
              <Button 
                variant="outline" 
                size="sm" 
                onClick={() => setCurrentPage(prev => prev - 1)}
                disabled={currentPage === 1}
              >
                Anterior
              </Button>
              
              {/* Mostra o número da página atual e o total de páginas */}
              <span>Página {currentPage} de {totalPages > 0 ? totalPages : 1}</span>

              <Button 
                variant="outline" 
                size="sm" 
                onClick={() => setCurrentPage(prev => prev + 1)}
                disabled={currentPage === totalPages || totalPages === 0}
              >
                Próximo
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default RequestsTable;
