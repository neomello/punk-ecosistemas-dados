/**
 * Mailchain Integration
 * Web3-native messaging for PUNK Ecosistemas
 */

import { Mailchain } from "@mailchain/sdk";
import { config } from "dotenv";
import { resolve } from "path";

// Load .env from project root
config({ path: resolve(process.cwd(), "../.env") });

// ─────────────────────────────────────────────────────────────────────────────
// Types
// ─────────────────────────────────────────────────────────────────────────────

export type MessageType = "alert" | "report" | "audit" | "notification";

export interface PunkMessage {
  type: MessageType;
  subject: string;
  content: string;
  metadata?: Record<string, unknown>;
}

export interface SendResult {
  success: boolean;
  savedMessageId?: string;
  error?: string;
}

// ─────────────────────────────────────────────────────────────────────────────
// Mailchain Service
// ─────────────────────────────────────────────────────────────────────────────

export class MailchainService {
  private client: Mailchain | null = null;
  private fromAddress: string | null = null;

  async initialize(): Promise<boolean> {
    const secretPhrase = process.env.MAILCHAIN_SECRET_RECOVERY_PHRASE;

    if (!secretPhrase) {
      console.error("[!] MAILCHAIN_SECRET_RECOVERY_PHRASE not configured");
      return false;
    }

    try {
      this.client = Mailchain.fromSecretRecoveryPhrase(secretPhrase);
      const user = await this.client.user();
      this.fromAddress = user.address;
      console.log(`[+] Mailchain initialized: ${this.fromAddress}`);
      return true;
    } catch (error) {
      console.error("[!] Failed to initialize Mailchain:", error);
      return false;
    }
  }

  async send(to: string, message: PunkMessage): Promise<SendResult> {
    if (!this.client) {
      return { success: false, error: "Client not initialized" };
    }

    const formattedContent = this.formatMessage(message);

    try {
      const { data, error } = await this.client.sendMail({
        from: this.fromAddress!,
        to: [to],
        subject: this.formatSubject(message),
        content: {
          text: formattedContent,
          html: this.formatHtml(message),
        },
      });

      if (error) {
        return { success: false, error: error.message };
      }

      console.log(`[+] Message sent to ${to}`);
      return { success: true, savedMessageId: data?.savedMessageId };
    } catch (error) {
      return { success: false, error: String(error) };
    }
  }

  async sendAlert(to: string, title: string, details: string): Promise<SendResult> {
    return this.send(to, {
      type: "alert",
      subject: title,
      content: details,
    });
  }

  async sendReport(to: string, reportName: string, summary: string): Promise<SendResult> {
    return this.send(to, {
      type: "report",
      subject: reportName,
      content: summary,
    });
  }

  async sendAuditLog(to: string, action: string, details: string): Promise<SendResult> {
    return this.send(to, {
      type: "audit",
      subject: action,
      content: details,
      metadata: { timestamp: new Date().toISOString() },
    });
  }

  // ─────────────────────────────────────────────────────────────────────────
  // Formatters
  // ─────────────────────────────────────────────────────────────────────────

  private formatSubject(message: PunkMessage): string {
    const prefixes: Record<MessageType, string> = {
      alert: "◬ ALERT",
      report: "◈ REPORT",
      audit: "⦿ AUDIT",
      notification: "◇ INFO",
    };
    return `${prefixes[message.type]} | ${message.subject}`;
  }

  private formatMessage(message: PunkMessage): string {
    const timestamp = new Date().toISOString();
    return `
─────────────────────────────────────
PUNK ECOSISTEMAS | ${message.type.toUpperCase()}
─────────────────────────────────────

${message.content}

─────────────────────────────────────
Timestamp: ${timestamp}
Type: ${message.type}
─────────────────────────────────────

Ø((Ø))
    `.trim();
  }

  private formatHtml(message: PunkMessage): string {
    const colors: Record<MessageType, string> = {
      alert: "#FF6B00",
      report: "#3B82F6",
      audit: "#10B981",
      notification: "#6B7280",
    };

    return `
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d0d0d; color: #fff; padding: 20px; }
    .container { max-width: 600px; margin: 0 auto; }
    .header { border-left: 4px solid ${colors[message.type]}; padding-left: 16px; margin-bottom: 24px; }
    .type { color: ${colors[message.type]}; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }
    .subject { font-size: 24px; font-weight: bold; margin: 8px 0; }
    .content { background: #1a1a1a; padding: 20px; border-radius: 8px; white-space: pre-wrap; }
    .footer { margin-top: 24px; font-size: 12px; color: #666; text-align: center; }
    .signature { color: #3B82F6; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="type">${message.type}</div>
      <div class="subject">${message.subject}</div>
    </div>
    <div class="content">${message.content}</div>
    <div class="footer">
      PUNK ECOSISTEMAS<br>
      <span class="signature">Ø((Ø))</span>
    </div>
  </div>
</body>
</html>
    `.trim();
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// CLI / Test
// ─────────────────────────────────────────────────────────────────────────────

async function main() {
  console.log("─".repeat(50));
  console.log("  PUNK ECOSISTEMAS - Mailchain Test");
  console.log("─".repeat(50));

  const service = new MailchainService();
  const initialized = await service.initialize();

  if (!initialized) {
    console.log("\n[!] Configure MAILCHAIN_SECRET_RECOVERY_PHRASE no .env");
    process.exit(1);
  }

  // Test send
  const to = process.env.MAILCHAIN_NOTIFICATIONS_TO;
  
  if (!to) {
    console.log("\n[!] Configure MAILCHAIN_NOTIFICATIONS_TO no .env");
    process.exit(1);
  }

  console.log(`\n[>] Sending test message to ${to}...`);
  
  const result = await service.sendAlert(
    to,
    "Sistema Inicializado",
    "PUNK Ecosistemas está online.\n\nPrimeira coleta de dados executada com sucesso.\n\n- Google Search: 4 buscas\n- Maps: 3 unidades\n- Websites: 2 analisados"
  );

  if (result.success) {
    console.log(`[+] Message sent! ID: ${result.savedMessageId}`);
  } else {
    console.log(`[!] Failed: ${result.error}`);
  }

  console.log("\n" + "─".repeat(50));
}

// Run if called directly
main().catch(console.error);
