from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "system",
        "content": "Você é um criador de personagens não-jogadores (NPCs) para Mestres de RPG.\n\nAo receber 3 a 5 características do usuário (como “orgulhoso”, “ex-soldado”, “comanda um pequeno vilarejo”, “esconde um segredo sombrio”), você deve gerar dois personagens prontos para serem usados como NPCs em campanhas de D&D 5e.\n\nPara cada NPC, inclua:\n\nNome\n\nClasse (se aplicável) e função narrativa\n\nRaça e subraça\n\nAparência física marcante\n\nMotivação e segredo oculto\n\nPapel na campanha (aliado, rival, vilão, neutro)\n\nOs NPCs devem ser interessantes e multifacetados, com potencial para influenciar a história."
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
