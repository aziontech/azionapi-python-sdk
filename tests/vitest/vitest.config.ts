import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    globalSetup: './globalSetup.ts',
    include: ['functional/**/*.test.ts'],
    testTimeout: 60_000,
    // Creating the virtualenvs installs the package requirements from PyPI.
    hookTimeout: 600_000,
  },
})
