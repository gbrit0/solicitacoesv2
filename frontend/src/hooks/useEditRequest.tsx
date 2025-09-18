// Hook personalizado para gerenciar edição de solicitações
import { useState, useCallback } from 'react';
import IListaDeSolicitacoes from '@/interfaces/IListaDeSolicitacoes';
import http from '@/http/index';

interface UseEditRequestReturn {
  editData: IListaDeSolicitacoes | null;
  loading: boolean;
  error: string | null;
  loadRequestData: (id: string) => Promise<void>;
  clearData: () => void;
}

const useEditRequest = (): UseEditRequestReturn => {
  const [editData, setEditData] = useState<IListaDeSolicitacoes | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const loadRequestData = useCallback(async (id: string) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await http.get(`/solicitacoes/compras/${id}`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token') || ''}`
        }
      });
      
      if (response.data && response.data.data) {
        setEditData(response.data.data);
      } else {
        setError('Dados da solicitação não encontrados');
      }
    } catch (error) {
      console.error('Erro ao carregar solicitação:', error);
      setError('Erro ao carregar dados da solicitação');
    } finally {
      setLoading(false);
    }
  }, []);

  const clearData = useCallback(() => {
    setEditData(null);
    setError(null);
    setLoading(false);
  }, []);

  return {
    editData,
    loading,
    error,
    loadRequestData,
    clearData
  };
};

export default useEditRequest;

