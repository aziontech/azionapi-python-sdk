import { describe, expect, inject, it } from 'vitest'
import { documentedEndpoints, listPackages, probe } from '../src/sdk'

const interpreters = inject('interpreters')
const packages = listPackages()

// These packages declare an `Accept` header parameter, which the generated
// ApiClient rejects at import time ("Invalid name, name may not be one of
// {'Accept', 'Content-Type', 'Authorization'}"), so their API modules cannot be
// imported. The defect is in the generated code and must be fixed in the
// generator input. When a regeneration fixes it, the guard below fails and the
// package must be removed from this list.
const KNOWN_BROKEN = new Set(['realtimepurge', 'storageapi'])

describe('generated Python SDK packages', () => {
  it('discovers every generated package', () => {
    expect(packages.length).toBeGreaterThanOrEqual(18)
  })

  for (const pkg of packages.filter((p) => !KNOWN_BROKEN.has(p.name))) {
    describe(pkg.name, () => {
      it('imports, builds an ApiClient and exposes every documented endpoint', async () => {
        const result = await probe(interpreters[pkg.name], ['inspect', pkg.name])
        expect(result.package).toBe(pkg.name)

        const apis: Record<string, string[]> = result.apis
        expect(Object.keys(apis).length).toBeGreaterThan(0)

        const documented = documentedEndpoints(pkg)
        expect(documented.length).toBeGreaterThan(0)
        for (const endpoint of documented) {
          expect(apis[endpoint.api], `${endpoint.api} class`).toBeDefined()
          expect(apis[endpoint.api], `${endpoint.api}.${endpoint.method}`).toContain(endpoint.method)
        }
      })
    })
  }

  for (const name of KNOWN_BROKEN) {
    it(`${name}: generated Accept header parameter still breaks the API module import`, async () => {
      await expect(probe(interpreters[name], ['inspect', name])).rejects.toThrow(/Invalid name, name may not be one of/)
    })
  }
})
