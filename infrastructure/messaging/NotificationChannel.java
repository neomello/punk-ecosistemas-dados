package infrastructure.messaging;

/**
 * NotificationChannel - Abstração de canais de notificação
 * 
 * Interface para diferentes canais de comunicação.
 * Mailchain é o canal principal (web3-native).
 * 
 * @author MELLØ // POST-HUMAN
 */
public interface NotificationChannel {

    /**
     * Envia notificação para um destinatário.
     * 
     * @param recipient Destinatário (wallet, ENS, email)
     * @param subject Assunto
     * @param content Conteúdo
     * @return true se enviado com sucesso
     */
    boolean send(String recipient, String subject, String content);

    /**
     * Verifica se o canal está disponível.
     * 
     * @return true se o canal está operacional
     */
    boolean isAvailable();

    /**
     * Retorna o tipo do canal.
     * 
     * @return tipo do canal
     */
    ChannelType getType();

    enum ChannelType {
        MAILCHAIN,  // Web3 native messaging
        WEBHOOK,    // HTTP callbacks
        INTERNAL    // Sistema interno
    }
}

